import numpy as np
import matplotlib.pyplot as plt
import matplotx

data = np.genfromtxt("data.csv", delimiter=",")

data_he = data[2:, 1]
data_d = data[2:, 3]

cummulative_he_release = np.cumsum(data_he)

cummulative_he_release = cummulative_he_release[:-1]  # remove last TDS

next_tds_d_release = data_d[1:]


# plt.scatter(1 + np.arange(cummulative_he_release.size), cummulative_he_release)
# plt.scatter(1 + np.arange(next_tds_d_release.size), next_tds_d_release)

# plt.xlabel("TDS")
# plt.ylabel("Release")

# plt.ylim(bottom=0)

yellow_he = "#fd9b21"
blue_hydrgoen = "#3c78d8"

plt.figure(figsize=(6.4, 3))

labels = ["TDS 0-1", "1-2", "2-3", "3-4", "4-5"]
posx = np.arange(cummulative_he_release.size)
width = 0.35

plt.bar(
    posx - width / 2,
    cummulative_he_release,
    width,
    color=yellow_he,
    label="Cumulative He",
)
plt.bar(
    posx + width / 2,
    next_tds_d_release,
    width,
    color=blue_hydrgoen,
    label="D",
)

plt.xticks(posx, labels)

ax = plt.gca()
ax.spines.right.set_visible(False)
ax.spines.top.set_visible(False)

plt.ylabel("Release (m$^{-2}$)")
plt.legend(loc="upper left", frameon=False)

plt.tight_layout()

plt.figure(figsize=(6.4, 3))


ratio = next_tds_d_release / cummulative_he_release
plt.scatter(cummulative_he_release, next_tds_d_release, alpha=0.5)

x_reg = np.linspace(0, cummulative_he_release.max() * 1.2)
plt.plot(x_reg, 0.8 * x_reg, label="$y = 0.8 x$")

plt.xlabel("Cummulative He released (m$^{-2}$)")
plt.ylabel("D released (m$^{-2}$)")

plt.xlim(left=0)
plt.ylim(bottom=0)

matplotx.line_labels()

plt.tight_layout()

ax = plt.gca()
ax.spines.right.set_visible(False)
ax.spines.top.set_visible(False)
plt.show()
