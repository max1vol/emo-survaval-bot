import sounddevice as sd
from kokoro_onnx import Kokoro

kokoro = Kokoro("data/kokoro-v1.0.int8.onnx", "data/voices-v1.0.bin")

samples, sample_rate = kokoro.create(
    "It was the best of times, it was the worst of times",
    voice="af_heart",
    speed=1.0,
    lang="en-us",
)

sd.play(samples, sample_rate)
sd.wait()
