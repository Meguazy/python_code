#Importing modules
import numpy as np
import matplotlib.pyplot as plt
import matplotlib

#Defining the constants
#The signal, the noise and the "instrument"
SIG_AMPLITUDE = 10; SIG_OFFSET = 2; SIG_PERIOD = 100
NOISE_AMPLITUDE = 3
N_samples = 5 * SIG_PERIOD
INSTRUMENT_RANGE = 9

#Builiding the sinewave
times = np.arange(N_samples).astype(float)
signal = SIG_AMPLITUDE * np.sin(2 * np.pi * times / SIG_PERIOD) + SIG_OFFSET
print(signal)
noise = NOISE_AMPLITUDE * np.random.normal(size=N_samples)
signal += noise

#Let's truncate everything outside of the instrument range
signal[signal > INSTRUMENT_RANGE] = INSTRUMENT_RANGE
signal[signal < -INSTRUMENT_RANGE] = -INSTRUMENT_RANGE

#Plotting
matplotlib.style.use("ggplot")
plt.plot(times,signal)
plt.title("Synthetic sine wave signal")
plt.xlabel("Time")
plt.ylabel("Signal + noise")
plt.ylim(ymin= -SIG_AMPLITUDE, ymax = SIG_AMPLITUDE)
plt.show()

#Saving the graph
plt.savefig("./graph/signal.pdf")
