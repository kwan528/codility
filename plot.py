import numpy as np
from matplotlib import pyplot as plt
from numpy.linalg import norm

# **read the data from the file**
tm, pm1 = np.genfromtxt("PW1.dat", delimiter=",", skip_header=1).T

f, ax = plt.subplots(1, 1)
xs = np.linspace(0, 2 * np.pi, 101)
dy = dydx(x=xs, y=None, a=1, b=np.pi / 2.0)
ax.plot(xs, dy, "b--", label="dydx")
ax.legend()
ax.set_xlabel("x")
ax.set_xlim([0, 40])
ax.axhline(0.0, c="k", ls=":")
ax.set_title("Summary of field operations and seismicity at field X")
# EITHER show the plot to the screen
# plt.show()
# OR save a version of it to the disk
plt.savefig("lab8_plot.png", dpi=300)


# **Whats happening here?**
ax.arrow(
    2003.5,
    15,
    0.0,
    -0.75,
    length_includes_head=True,
    head_width=0.2,
    head_length=0.1,
    color="b",
)
ax.text(2003.0, 14.65, "M 3.5", ha="right", va="center", size=10, color="b")
