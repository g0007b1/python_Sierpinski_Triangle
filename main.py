import matplotlib.pyplot as plt
import numpy as np
fig = plt.figure()
ax_1 = fig.add_subplot(1, 1, 1)
ax_1.scatter([0, 5, 10], [0, 5, 0])
x_start = 4
y_start = 3

for i in range(1000):
    a = np.random.randint(1, 4)
    if a == 1:
        x_start = x_start/2
        y_start = y_start/2
        ax_1.scatter(x_start, y_start, color="blue")
    elif a == 2:
        x_start = (x_start+5)/2
        y_start = (y_start+5)/2
        ax_1.scatter(x_start, y_start, color="blue")
    elif a == 3:
        x_start = (x_start + 10)/2
        y_start = (y_start+0)/2
        ax_1.scatter(x_start, y_start, color="blue")

plt.show()
