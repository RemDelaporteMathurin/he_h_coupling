import numpy as np
import matplotlib.pyplot as plt

cb = np.genfromtxt("../mykola_HF/cb.csv", delimiter=",", names=True)
ib = np.genfromtxt("../mykola_HF/ib.csv", delimiter=",", names=True)


# plot
def radius(i):
    a_0 = 0.318e-9
    pi = np.pi
    return (
        ((3**0.5) / 4 * a_0)
        + (3 / (4 * pi) * (a_0**3) / 2 * abs(i) / 4) ** (1 / 3)
        - (3 / (4 * pi) * (a_0**3) / 2) ** (1 / 3)
    )


density = 8e18 * 4 * np.pi * radius(ib["ib"]) ** 2
density *= cb["cb"]
plt.plot(cb["arc_length"] * 1e9, density, linewidth=3)
plt.plot(cb["arc_length"] * 1e9, cb["cb"], linewidth=3)

plt.annotate(
    "Trap density", (cb["arc_length"][-1] * 1.01 * 1e9, density[-1]), color="tab:blue"
)
plt.annotate(
    "Bubbles", (cb["arc_length"][-1] * 1.01 * 1e9, cb["cb"][-1]), color="tab:orange"
)

plt.xlim(right=600)
plt.yscale("log")
plt.ylabel(r"Concentration (m$^{-3}$)")
plt.xlabel(r"depth (nm)")

ax = plt.gca()
ax.spines["right"].set_visible(False)
ax.spines["top"].set_visible(False)
plt.show()

plt.plot()
plt.plot(cb["arc_length"] * 1e9, 1e9 * radius(ib["ib"]), linewidth=3)
plt.yscale("log")
plt.xlim(right=100)
plt.show()
