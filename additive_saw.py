import numpy as np
from scipy.io.wavfile import write

def angle(freq, sample_rate, n, phase):
    return (2 * np.pi * freq * n / sample_rate) - phase

def gn(freq, amp, n, sample_rate):
    phase = 0

    return amp * np.sin(angle(freq, sample_rate, n, phase))

def generate_samples(freq, amp, sample_rate, duration):
    return np.array(list(map(lambda n: gn(freq, amp, n, sample_rate), range(duration * sample_rate))))

def generate_saw(freq, amp, n_harmonics, sample_rate, duration):
    samples = generate_samples(freq, amp, sample_rate, duration)

    for harmonic in range(2, n_harmonics + 1):
        harmonic_amp = amp / harmonic
        samples += generate_samples(freq * harmonic, harmonic_amp, sample_rate, duration)

    return samples


def create_wav_file(samples, sample_rate, filename):
    write(filename, sample_rate, samples)

amp = 0.25
freq = 300
sample_rate = 44100
harmonics = 100
duration = 3

samples = generate_saw(freq, amp, harmonics, sample_rate, 3)

create_wav_file(samples, sample_rate, "temp/saw.wav")

