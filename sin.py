import numpy as np
from scipy.io.wavfile import write

def angle(freq, sample_rate, n, phase):
    return (2 * np.pi * freq * n / sample_rate) - phase

def gn(n, sample_rate):
    amp = 0.25
    freq = 300
    phase = 0

    return amp * np.sin(angle(freq, sample_rate, n, phase))

def generate_samples(sample_rate, duration, sample_callback):
    return np.array(list(map(lambda n: sample_callback(n, sample_rate), range(duration * sample_rate))))

def create_wav_file(samples, sample_rate, filename):
    write(filename, sample_rate, samples)

sample_rate = 44100
duration = 3
samples = generate_samples(sample_rate, 3, gn)
print(samples)

create_wav_file(samples, sample_rate, "temp/sin.wav")

