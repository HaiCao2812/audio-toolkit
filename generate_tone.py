import numpy as np
import matplotlib.pyplot as plt

sample_rate = 44100
duration = 2.0
frequency = 440.0

t = np.linspace(0, duration, int(sample_rate * duration), endpoint = False)
tone =  np.sin(2 * np.pi * frequency * t)

print("number of samples:", len(tone))
print("first 5 values:", tone[:5])

plt.plot(t[:500], tone[:500])
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")
plt.title("440 Hz sine wave (first 500 samples)")
plt.show()