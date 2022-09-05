import numpy as np
import matplotlib.pyplot as plt


data = np.genfromtxt("high helium flux.dat", delimiter="\t", names=True)
he_retention = data["Ret_He"][2:]
he_ret_err = data["error_for_He"][2:]
d_retention = data["Ret_D_Sample"][2:]
d_ret_err = data["final_error_sum_of_two_for_D"][2:]


yellow_he = "#fd9b21"
blue_hydrgoen = "#3c78d8"

posx = [0] + [i + 2 for i in range(len(he_retention) - 1)]

labels = ["Initial TDS", "1", "2", "3", "4", "5"]

fig, axs = plt.subplots(2, 1, sharex=True)

plt.sca(axs[0])
plt.bar(posx, he_retention, color=yellow_he, yerr=he_ret_err)

plt.ylim(bottom=0)
plt.ylabel("He release (m$^{-2}$)")

plt.sca(axs[1])
plt.bar(posx, d_retention, color=blue_hydrgoen, yerr=d_ret_err)
plt.ylabel("D release (m$^{-2}$)")


plt.ylim(bottom=0)
plt.xticks(posx, labels)

for ax in axs:
    ax.spines.right.set_visible(False)
    ax.spines.top.set_visible(False)

plt.show()
