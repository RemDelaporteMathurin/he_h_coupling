import numpy as np
import matplotlib.pyplot as plt
import matplotx
from scipy.optimize import curve_fit


yellow_he = "#fd9b21"
blue_hydrgoen = "#3c78d8"

data = np.genfromtxt("high helium flux.dat", delimiter="\t", names=True)
he_retention = data["Ret_He"][2:]
he_ret_err = data["error_for_He"][2:]
d_retention = data["Ret_D_Sample"][2:]
d_ret_err = data["final_error_sum_of_two_for_D"][2:]


additional_d_relase = np.diff(d_retention[1:])
add_d_release_upper_bound, add_d_release_lower_bound = [], []

for i in range(len(d_retention[1:-1])):
    possibilities = [
        d_retention[i] - d_ret_err[i] - (d_retention[i + 1] - d_ret_err[i + 1]),
        d_retention[i] - d_ret_err[i] - (d_retention[i + 1] + d_ret_err[i + 1]),
        d_retention[i] + d_ret_err[i] - (d_retention[i + 1] - d_ret_err[i + 1]),
        d_retention[i] + d_ret_err[i] - (d_retention[i + 1] + d_ret_err[i + 1]),
    ]
    add_d_release_upper_bound.append(abs(d_retention[i] - max(possibilities)))
    add_d_release_lower_bound.append(abs(d_retention[i] - min(possibilities)))

plt.errorbar(
    he_retention[1:-1],
    additional_d_relase,
    xerr=he_ret_err[1:-1],
    yerr=[add_d_release_lower_bound, add_d_release_upper_bound],
    fmt="o",
)


def propto(x, a):
    return a * x


popt, pcov = curve_fit(
    propto, he_retention[1:-1], additional_d_relase, sigma=add_d_release_lower_bound
)
x_reg = np.linspace(0, he_retention[1:-1].max() * 1.2)
plt.plot(x_reg, popt * x_reg, label="$y = {:.2f} x$".format(popt[0]))

matplotx.line_labels()

plt.xlabel("He release (m$^{-2}$)")
plt.ylabel("Additional D release (m$^{-2}$)")


plt.tight_layout()

fig, axs = plt.subplots(2, 1, sharex=True)


labels = ["TDS 1-2", "2-3", "3-4", "4-5"]
posx = np.arange(additional_d_relase.size)
plt.sca(axs[0])
plt.bar(posx, he_retention[1:-1], yerr=he_ret_err[1:-1], color=yellow_he)

plt.ylabel("He release (m$^{-2}$)")


plt.sca(axs[1])
plt.bar(
    posx,
    additional_d_relase,
    yerr=[add_d_release_lower_bound, add_d_release_upper_bound],
    color=blue_hydrgoen,
)
plt.ylim(bottom=0)
plt.xticks(posx, labels)

plt.ylabel("Additional D release (m$^{-2}$)")
plt.show()
