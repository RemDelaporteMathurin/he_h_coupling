import numpy as np
import matplotlib.pyplot as plt


def plot_tds_exp(tds_nb: int, **kwargs):
    data = np.genfromtxt(
        "TDS_{}/Ialovega_WHeD_I-TDS_{}.txt".format(tds_nb, tds_nb), skip_header=2
    )
    return plt.errorbar(data[:, 0], data[:, 1], yerr=data[:, 2], **kwargs)


def plot_tds_model(tds_nb: int, **kwargs):
    data = np.genfromtxt(
        "TDS_{}/derived_quantities.csv".format(tds_nb), delimiter=",", names=True
    )
    t = data["ts"]
    indexes = np.where(t > 52)
    T_1 = data["Average_T_volume_1"][indexes]
    flux_left = data["Flux_surface_1_solute"][indexes]
    flux_right = data["Flux_surface_2_solute"][indexes]
    flux_total_1 = -flux_left - flux_right
    return plt.plot(T_1, flux_total_1, **kwargs)


def plot_trap_contrib(tds_nb: int, trap_index):
    data = np.genfromtxt(
        "TDS_{}/derived_quantities.csv".format(tds_nb), delimiter=",", names=True
    )
    t = data["ts"]
    indexes = np.where(t > 52)
    T = data["Average_T_volume_1"][indexes]
    trap = data["Total_{}_volume_1".format(trap_index)][indexes]
    diff_trap = -np.diff(trap) / np.diff(t[indexes])
    plt.plot(T[1:], diff_trap, linestyle="dashed", color="grey", linewidth=1)
    plt.fill_between(T[1:], diff_trap, alpha=0.3, color="grey")


tds1_color = "tab:blue"
tds2_color = "tab:orange"
tds5_color = "tab:green"

# experimental data

l_1 = plot_tds_exp(1, alpha=0.3, marker="o")
l_2 = plot_tds_exp(2, alpha=0.3, marker="o")
l_5 = plot_tds_exp(5, alpha=0.3, marker="o")


# models
plot_tds_model(1, linewidth=3, color=l_1[0].get_color())
plt.annotate("1st TDS", (425, 0.1e17), color=l_1[0].get_color())

plot_tds_model(2, linewidth=3, color=l_2[0].get_color())
plt.annotate("2nd TDS", (450, 0.5e17), color=l_2[0].get_color())

plot_tds_model(5, linewidth=3, color=l_5[0].get_color())
plt.annotate("5th TDS", (500, 1e17), color=l_5[0].get_color())

plt.xlim(300, 750)
plt.ylim(bottom=0, top=1.2e17)
plt.ylabel(r"D desorption flux (m$^{-2}$ s$^{-1}$)", weight="bold")
plt.xlabel(r"T (K)", weight="bold")
ax = plt.gca()
ax.spines["right"].set_visible(False)
ax.spines["top"].set_visible(False)
# plt.show()

fig, axs = plt.subplots(1, 3, sharex=True, sharey=True, figsize=(6.4, 4.8 / 2))

plt.sca(axs[0])
# plot TDS 1
# l = plt.errorbar(tds_1_data[:, 0], tds_1_data[:, 1], alpha=0.3, yerr=tds_1_data[:, 2], marker="o", color=tds1_color)
plot_tds_model(1, linewidth=3, color=tds1_color)
plot_trap_contrib(1, trap_index=4)

# plt.xlim(300, 750)
# plt.ylim(bottom=0, top=1.2e17)
plt.ylabel(r"D desorption flux (m$^{-2}$ s$^{-1}$)", weight="bold")
# plt.xlabel(r"T (K)")
ax = plt.gca()
ax.spines["right"].set_visible(False)
ax.spines["top"].set_visible(False)


plt.sca(axs[1])
# plot TDS 2
# l = plt.errorbar(tds_2_data[:, 0], tds_2_data[:, 1], alpha=0.3, yerr=tds_2_data[:, 2], marker="o", color=tds2_color)
plot_tds_model(2, linewidth=3, color=tds2_color)
plot_trap_contrib(2, trap_index=1)
plot_trap_contrib(2, trap_index=2)
plot_trap_contrib(2, trap_index=3)
plot_trap_contrib(2, trap_index=4)

# plt.xlim(300, 750)
# plt.ylim(bottom=0, top=1.2e17)
# plt.ylabel(r"Desorption flux (m$^{-2}$ s$^{-1}$)")
plt.xlabel(r"T (K)", weight="bold")
ax = plt.gca()
ax.spines["right"].set_visible(False)
ax.spines["top"].set_visible(False)


plt.sca(axs[2])
# plot TDS 2
# l = plt.errorbar(tds_5_data[:, 0], tds_5_data[:, 1], alpha=0.3, yerr=tds_5_data[:, 2], marker="o", color=tds3_color)
plot_tds_model(5, linewidth=3, color=tds5_color)
plot_trap_contrib(5, trap_index=1)
plot_trap_contrib(5, trap_index=2)
plot_trap_contrib(5, trap_index=3)
plot_trap_contrib(5, trap_index=4)

plt.xlim(300, 660)
# plt.ylim(bottom=0, top=1.2e17)
# plt.ylabel(r"Desorption flux (m$^{-2}$ s$^{-1}$)")
# plt.xlabel(r"T (K)")
ax = plt.gca()
ax.spines["right"].set_visible(False)
ax.spines["top"].set_visible(False)

plt.tight_layout()


plt.figure()

plot_tds_exp(tds_nb=5, alpha=0.3, marker="o")
plt.xlim(300, 750)
plt.ylim(bottom=0)

ax = plt.gca()
ax.spines["right"].set_visible(False)
ax.spines["top"].set_visible(False)
plt.xlabel(r"T (K)")
plt.ylabel(r"Desorption flux (m$^{-2}$ s$^{-1}$)")
plt.show()
