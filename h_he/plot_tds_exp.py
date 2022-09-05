import numpy as np
import matplotlib.pyplot as plt

yellow_he = "#fd9b21"
blue_hydrgoen = "#3c78d8"

data_he = np.genfromtxt("He TDS HF 21B.dat", delimiter="\t", skip_header=3)

T0 = data_he[:, 0]
des0 = data_he[:, 1]

T1 = data_he[:, 2]
des1 = data_he[:, 3]

T2 = data_he[:, 4]
des2 = data_he[:, 5]

T3 = data_he[:, 6]
des3 = data_he[:, 7]

T4 = data_he[:, 8]
des4 = data_he[:, 9]

T5 = data_he[:, 10]
des5 = data_he[:, 11]

data_d_1 = np.genfromtxt("1st I-TDS D HF.dat", delimiter="\t", skip_header=3)
data_d_2 = np.genfromtxt("2nd I-TDS D HF.dat", delimiter="\t", skip_header=3)
data_d_3 = np.genfromtxt("3rd I-TDS D HF.dat", delimiter="\t", skip_header=3)
data_d_4 = np.genfromtxt("4th I-TDS D HF.dat", delimiter="\t", skip_header=3)
data_d_5 = np.genfromtxt("5th I-TDS D HF.dat", delimiter="\t", skip_header=3)

tds_d = [
    [data_d_1[:, 0], data_d_1[:, 1]],
    [data_d_2[:, 0], data_d_2[:, 1]],
    [data_d_3[:, 0], data_d_3[:, 1]],
    [data_d_4[:, 0], data_d_4[:, 1]],
    [data_d_5[:, 0], data_d_5[:, 1]],
]

tds_he = [[T1, des1], [T2, des2], [T3, des3], [T4, des4], [T5, des5]]


tds_indices = [1, 2, 3, 4, 5]
labels = []
for ind in tds_indices:
    if ind == 1:
        label = "1st TDS"
    elif ind == 2:
        label = "2nd TDS"
    elif ind == 3:
        label = "3rd TDS"
    else:
        label = "{}th TDS".format(ind)

    labels.append(label)

fig, axs = plt.subplots(len(tds_indices), ncols=1, sharex="col", sharey="row")

for i, ind in enumerate(tds_indices):
    plt.sca(axs[i])
    indices = np.where(tds_he[i][0] > 800)
    plt.plot(tds_he[i][0][indices], tds_he[i][1][indices], color=yellow_he)
    plt.fill_between(
        tds_he[i][0][indices], 0, tds_he[i][1][indices], color=yellow_he, alpha=0.5
    )
    # plt.yscale("log")
    plt.ylim(0, 2e17)

    plt.ylabel(labels[i], rotation=0)
    plt.gca().yaxis.set_label_position("right")
    indices = np.where(tds_d[i][0] < 800)
    plt.plot(tds_d[i][0][indices], tds_d[i][1][indices], color=blue_hydrgoen)
    plt.fill_between(
        tds_d[i][0][indices], 0, tds_d[i][1][indices], color=blue_hydrgoen, alpha=0.5
    )


axs[0].annotate("D", (500, 5.1e16), color=blue_hydrgoen, fontsize=16)
axs[0].annotate("He", (1050, 7.3e16), color=yellow_he, fontsize=16)

fig.supxlabel("T (K)")

fig.supylabel("Desorption (m$^{-2}$ s$^{-1}$)")

for ax in axs:
    ax.spines.right.set_visible(False)
    ax.spines.top.set_visible(False)

plt.tight_layout()

plt.show()
