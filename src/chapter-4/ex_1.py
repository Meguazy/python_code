import numpy as np
import matplotlib.pyplot as plt
import matplotlib

array = np.random.binomial(5, 0.5, size=100)
print(array)

print(array[1:])
print(array[:-1])

diff = array[1:] - array[:-1]

print(diff)

#Plotting
matplotlib.style.use("ggplot")
plt.plot(np.arange(99),diff)
plt.plot(np.arange(100),array)
plt.title("Diff")
plt.xlabel("x")
plt.ylabel("diff")
plt.show()