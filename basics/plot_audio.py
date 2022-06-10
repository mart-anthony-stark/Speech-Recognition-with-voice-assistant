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
print(audio_time)