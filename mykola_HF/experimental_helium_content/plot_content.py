import numpy as np
import matplotlib.pyplot as plt


data = np.genfromtxt("data.csv", delimiter=",")

data_he = data[2:, 1]
data_d = data[2:, 3]


yellow_he = "#fd9b21"
blue_hydrgoen = "#3c78d8"

posx = range(len(data_he))
labels = ["Initial TDS", "1", "2", "3", "4", "5"]

fig, axs = plt.subplots(2, 1, sharex=True)

plt.sca(axs[0])
plt.bar(posx, data_he, color=yellow_he)

plt.sca(axs[1])
plt.bar(posx, data_d, color=blue_hydrgoen)

plt.ylim(bottom=0)
plt.xticks(posx, labels)

for ax in axs:
    ax.spines.right.set_visible(False)
    ax.spines.top.set_visible(False)

plt.show()
