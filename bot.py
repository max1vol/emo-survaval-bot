import whisper
import time
import sounddevice as sd
from scipy.io.wavfile import write
import numpy as np
from llama_cpp import Llama
import asyncio
import soundfile as sf
from kokoro_onnx import SAMPLE_RATE, Kokoro

# --- ASR ---
print("Loading Whisper")
start_load_time = time.time()
asr_model = whisper.load_model("tiny.en")
end_load_time = time.time()
print(f"ASR model loaded in: {end_load_time - start_load_time:.2f} seconds")

# --- LLM ---
print("Loading LLM")
llm = Llama.from_pretrained(
    repo_id="ggml-org/gemma-3-1b-it-GGUF", filename="*Q4_K_M.gguf", verbose=False
)

# --- TTS ---
print("Loading TTS")
kokoro = Kokoro("tts/data/kokoro-v1.0.onnx", "tts/data/voices-v1.0.bin")

# --- Conversation History ---
messages = [
    {
        "role": "system",
        "content": "You are a helpful assistant. NEVER use emoji. Be rather consice and friendly.",
    },
]


def record_audio(filename="recorded_audio.wav"):
    samplerate = 44100
    channels = 1

    print("Ready? Press Enter to start recording.")
    input()

    print("Recording... Press Enter to stop.")

    recorded_chunks = []

    def callback(indata, frames, time, status):
        if status:
            print(status)
        recorded_chunks.append(indata.copy())

    stream = sd.InputStream(
        samplerate=samplerate, channels=channels, callback=callback, dtype="int16"
    )

    with stream:
        input()

    print("Recording finished.")

    myrecording = np.concatenate(recorded_chunks, axis=0)
    write(filename, samplerate, myrecording)

    print(f"File saved as {filename}")
    return filename


def transcribe_audio(filename="recorded_audio.wav"):
    print("Transcribing...")
    start_transcribe_time = time.time()
    result = asr_model.transcribe(filename)
    end_transcribe_time = time.time()
    print(
        f"Transcription finished in: {end_transcribe_time - start_transcribe_time:.2f} seconds"
    )
    return result["text"]


def get_llm_response(user_input):
    global messages
    messages.append({"role": "user", "content": user_input})

    print("Running inference...")
    output = llm.create_chat_completion(messages=messages)

    response_text = output["choices"][0]["message"]["content"]
    messages.append({"role": "assistant", "content": response_text})

    return response_text


async def text_to_speech(text, output_filename="response_audio.wav"):
    stream = kokoro.create_stream(
        text,
        voice="af_nicole",
        speed=1.0,
        lang="en-us",
    )
    print("Streaming TTS audio...")
    with sf.SoundFile(
        output_filename, mode="w", samplerate=SAMPLE_RATE, channels=1
    ) as f:
        async for samples, sample_rate in stream:
            f.write(samples)
    return output_filename


def play_audio(filename):
    data, fs = sf.read(filename, dtype="float32")
    sd.play(data, fs)
    sd.wait()


async def main():
    while True:
        audio_file = record_audio()
        user_text = transcribe_audio(audio_file)
        print(f"You said: {user_text}")

        if user_text.lower().strip() == "exit":
            print("Exiting bot.")
            break

        llm_response = get_llm_response(user_text)
        print(f"Bot says: {llm_response}")

        tts_audio_file = await text_to_speech(llm_response)
        play_audio(tts_audio_file)


if __name__ == "__main__":
    asyncio.run(main())
