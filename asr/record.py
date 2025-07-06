import sounddevice as sd
from scipy.io.wavfile import write
import numpy as np

# --- Recording Parameters ---
samplerate = 44100  # Sample rate in Hz
channels = 1  # Mono
filename = "recorded_audio.wav"

# --- Recording ---
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

# --- Saving the file ---
myrecording = np.concatenate(recorded_chunks, axis=0)
write(filename, samplerate, myrecording)  # Save as WAV file

print(f"File saved as {filename}")
