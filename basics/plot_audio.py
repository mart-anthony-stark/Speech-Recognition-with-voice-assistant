from signal import signal
import wave
import matplotlib.pyplot as plt
import numpy as np

obj = wave.open('sample.wav', 'rb')

sample_freq = obj.getframerate()
n_samples = obj.getnframes()
signal_wave = obj.readframes(-1)

obj.close()

audio_time = n_samples / sample_freq
print(audio_time, "seconds")

signal_array = np.frombuffer(signal_wave, dtype=np.int16)

times = np.linspace(0, audio_time, num=n_samples)

plt.figure(figsize=(15, 5))
plt.plot(times, signal_array)
plt.title("Audio Signal")
plt.xlabel("Time in seconds")
plt.ylabel("Signal Wave")
plt.xlim(0, audio_time)
plt.show()