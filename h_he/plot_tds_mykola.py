import numpy as np
import matplotlib.pyplot as plt


def plot_trap_contrib(data, trap_index):
    t = data["ts"]
    indexes = np.where(t > 52)
    T = data["Average_T_volume_1"][indexes]
    trap = data["Total_{}_volume_1".format(trap_index)][indexes]
    diff_trap = -np.diff(trap) / np.diff(t[indexes])
    plt.plot(T[1:], diff_trap, linestyle="dashed", color="grey", linewidth=1)
    plt.fill_between(T[1:], diff_trap, alpha=0.3, color="grey")


tds1_color = "tab:blue"
tds2_color = "tab:orange"
tds3_color = "tab:green"

# experimental data
tds_1_data = np.genfromtxt("1st TDS/Ialovega_WHeD_I-TDS_1.txt", skip_header=2)
l_1 = plt.errorbar(
    tds_1_data[:, 0], tds_1_data[:, 1], alpha=0.3, yerr=tds_1_data[:, 2], marker="o"
)

tds_2_data = np.genfromtxt("2nd TDS/Ialovega_WHeD_I-TDS_2.txt", skip_header=2)
l_2 = plt.errorbar(
    tds_2_data[:, 0], tds_2_data[:, 1], alpha=0.3, yerr=tds_2_data[:, 2], marker="o"
)

tds_5_data = np.genfromtxt("5th TDS/Ialovega_WHeD_I-TDS_5.txt", skip_header=2)
l_5 = plt.errorbar(
    tds_5_data[:, 0], tds_5_data[:, 1], alpha=0.3, yerr=tds_5_data[:, 2], marker="o"
)


# models
derived_quantities_tds_1 = np.genfromtxt(
    "1st TDS/derived_quantities.csv", delimiter=",", names=True
)
t = derived_quantities_tds_1["ts"]
indexes = np.where(t > 52)
T_1 = derived_quantities_tds_1["Average_T_volume_1"][indexes]
flux_left = derived_quantities_tds_1["Flux_surface_1_solute"][indexes]
flux_right = derived_quantities_tds_1["Flux_surface_2_solute"][indexes]
flux_total_1 = -flux_left - flux_right
plt.plot(T_1, flux_total_1, linewidth=3, color=l_1[0].get_color())
plt.annotate("1st TDS", (425, 0.1e17), color=l_1[0].get_color())

derived_quantities_tds_2 = np.genfromtxt(
    "2nd TDS/derived_quantities.csv", delimiter=",", names=True
)
t = derived_quantities_tds_2["ts"]
indexes = np.where(t > 52)
T_2 = derived_quantities_tds_2["Average_T_volume_1"][indexes]
flux_left = derived_quantities_tds_2["Flux_surface_1_solute"][indexes]
flux_right = derived_quantities_tds_2["Flux_surface_2_solute"][indexes]
flux_total_2 = -flux_left - flux_right
plt.plot(T_2, flux_total_2, linewidth=3, color=l_2[0].get_color())
plt.annotate("2nd TDS", (450, 0.5e17), color=l_2[0].get_color())


derived_quantities_tds_5 = np.genfromtxt(
    "5th TDS/derived_quantities.csv", delimiter=",", names=True
)
t = derived_quantities_tds_5["ts"]
indexes = np.where(t > 52)
T_5 = derived_quantities_tds_5["Average_T_volume_1"][indexes]
flux_left = derived_quantities_tds_5["Flux_surface_1_solute"][indexes]
flux_right = derived_quantities_tds_5["Flux_surface_2_solute"][indexes]
flux_total_5 = -flux_left - flux_right
plt.plot(T_5, flux_total_5, linewidth=3, color=l_5[0].get_color())
plt.annotate("5th TDS", (500, 1e17), color=l_5[0].get_color())
plt.xlim(300, 750)
plt.ylim(bottom=0, top=1.2e17)
plt.ylabel(r"Desorption flux (m$^{-2}$ s$^{-1}$)", weight="bold")
plt.xlabel(r"T (K)", weight="bold")
ax = plt.gca()
ax.spines["right"].set_visible(False)
ax.spines["top"].set_visible(False)
# plt.show()

fig, axs = plt.subplots(1, 3, sharex=True, sharey=True, figsize=(6.4, 4.8 / 2))

plt.sca(axs[0])
# plot TDS 1
# l = plt.errorbar(tds_1_data[:, 0], tds_1_data[:, 1], alpha=0.3, yerr=tds_1_data[:, 2], marker="o", color=tds1_color)
plt.plot(T_1, flux_total_1, linewidth=3, color=tds1_color)
plot_trap_contrib(derived_quantities_tds_1, 4)

# plt.xlim(300, 750)
# plt.ylim(bottom=0, top=1.2e17)
plt.ylabel(r"Desorption flux (m$^{-2}$ s$^{-1}$)", weight="bold")
# plt.xlabel(r"T (K)")
ax = plt.gca()
ax.spines["right"].set_visible(False)
ax.spines["top"].set_visible(False)


plt.sca(axs[1])
# plot TDS 2
# l = plt.errorbar(tds_2_data[:, 0], tds_2_data[:, 1], alpha=0.3, yerr=tds_2_data[:, 2], marker="o", color=tds2_color)
plt.plot(T_2, flux_total_2, linewidth=3, color=tds2_color)

plot_trap_contrib(derived_quantities_tds_2, 1)
plot_trap_contrib(derived_quantities_tds_2, 2)
plot_trap_contrib(derived_quantities_tds_2, 3)
plot_trap_contrib(derived_quantities_tds_2, 4)

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
plt.plot(T_5, flux_total_5, linewidth=3, color=tds3_color)
plot_trap_contrib(derived_quantities_tds_5, 1)
plot_trap_contrib(derived_quantities_tds_5, 2)
plot_trap_contrib(derived_quantities_tds_5, 3)
plot_trap_contrib(derived_quantities_tds_5, 4)

plt.xlim(300, 660)
# plt.ylim(bottom=0, top=1.2e17)
# plt.ylabel(r"Desorption flux (m$^{-2}$ s$^{-1}$)")
# plt.xlabel(r"T (K)")
ax = plt.gca()
ax.spines["right"].set_visible(False)
ax.spines["top"].set_visible(False)

plt.tight_layout()

plt.show()
