import sounddevice as sd
from kokoro_onnx import Kokoro

kokoro = Kokoro("data/kokoro-v1.0.int8.onnx", "data/voices-v1.0.bin")
print("Loaded!")
samples, sample_rate = kokoro.create(
    "Hello, my name is Max. I am making a project called Off-Grid Survival Emotionally Intelligent Bot",
    voice="af_heart",
    speed=1.0,
    lang="en-us",
)

sd.play(samples, sample_rate)
sd.wait()
