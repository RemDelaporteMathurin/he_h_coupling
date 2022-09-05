import numpy as np
import matplotlib.pyplot as plt
import matplotx
from scipy.optimize import curve_fit

data = np.genfromtxt("high helium flux.dat", delimiter="\t", names=True)
he_retention = data["Ret_He"][2:]
he_ret_err = data["error_for_He"][2:]
d_retention = data["Ret_D_Sample"][2:]
d_ret_err = data["final_error_sum_of_two_for_D"][2:]


cummulative_he_release = np.cumsum(he_retention)
cummulative_he_err = np.cumsum(he_ret_err)

cummulative_he_release = cummulative_he_release[:-1]  # remove last TDS
cummulative_he_err = cummulative_he_err[:-1]

next_tds_d_release = d_retention[1:]
next_tds_d_err = d_ret_err[1:]

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
    yerr=cummulative_he_err,
)
plt.bar(
    posx + width / 2,
    next_tds_d_release,
    width,
    color=blue_hydrgoen,
    label="D",
    yerr=next_tds_d_err,
)

plt.xticks(posx, labels)

ax = plt.gca()
ax.spines.right.set_visible(False)
ax.spines.top.set_visible(False)

plt.ylabel("Release (m$^{-2}$)")
plt.legend(loc="upper left", frameon=False)
plt.ylim(bottom=0)

plt.tight_layout()

plt.figure(figsize=(6.4, 3))


ratio = next_tds_d_release / cummulative_he_release
plt.errorbar(
    cummulative_he_release,
    next_tds_d_release,
    alpha=0.5,
    fmt="o",
    xerr=cummulative_he_err,
    yerr=next_tds_d_err,
)


def propto(x, a):
    return a * x


popt, pcov = curve_fit(
    propto, cummulative_he_release, next_tds_d_release, sigma=next_tds_d_err
)

x_reg = np.linspace(0, cummulative_he_release.max() * 1.2)
plt.plot(x_reg, popt * x_reg, label="$y = {:.2f} x$".format(popt[0]))

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
