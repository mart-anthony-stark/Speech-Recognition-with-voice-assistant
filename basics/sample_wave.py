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

audio_time = obj.getnframes() / obj.getframerate()
print(audio_time)

frames = obj.readframes(-1)
print(type(frames), type(frames[0]))
print(len(frames) / 2)
obj.close()

obj_new = wave.open("new_sample.wav", "wb")
obj_new.setnchannels(1)
obj_new.setsampwidth(2)
obj_new.setframerate(48000)
obj_new.writeframes(frames)
obj_new.close()
