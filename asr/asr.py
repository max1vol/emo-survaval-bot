import whisper
import time

print("Loading Whisper")
start_load_time = time.time()
model = whisper.load_model("tiny.en")
end_load_time = time.time()
print(f"Model loaded in: {end_load_time - start_load_time:.2f} seconds")

print("Transcribing...")
start_transcribe_time = time.time()
result = model.transcribe("recorded_audio.wav")
end_transcribe_time = time.time()
print(
    f"Transcription finished in: {end_transcribe_time - start_transcribe_time:.2f} seconds"
)

print(result["text"])
