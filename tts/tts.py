import soundfile as sf
from kokoro_onnx import Kokoro

print("hi")

kokoro = Kokoro("kokoro-v1.0.int8.onnx", "voices-v1.0.bin")

samples, sample_rate = kokoro.create(
    "Hello, my name is Max. I am making a project called Off-Grid Survival Emotionally Intelligent Bot",
    voice="af_heart",
    speed=1.0,
    lang="en-us",
)

sf.write("audio.wav", samples, sample_rate)
print("Created audio.wav")
