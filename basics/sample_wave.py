import wave

# - wave file structure
# - number of channels
# - sample width
# - framerate/sample_rate
# - number of frames
# - values of a frame

obj = wave.open("sample.wav", "rb")
print("Number of channels", obj.getnchannels())
print("Sample width", obj.getsampwidth())
print("Framerate", obj.getframerate())
print("No. of frames", obj.getnframes())
print("Parameters", obj.getparams())
