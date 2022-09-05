import matplotlib.pyplot as plt
from matplotlib import ticker
import numpy as np

tds_number = 1
if tds_number == 1:
    folder = "h_he/1st TDS"
    density_1 = 0
    density_2 = 0
    density_3 = 0
elif tds_number == 2:
    folder = "h_he/2nd TDS"
    density_1 = 2.2e-3
    density_2 = 1.8e-3
    density_3 = 2.0e-3
elif tds_number == 5:
    folder = "h_he/5th TDS"
    density_1 = 3.8e-3
    density_2 = 3.1e-3
    density_3 = 1.5e-3


labels = ["Trap 1", "Trap 2", "Trap 3"]
tds_2 = [2.2e-3, 1.8e-3, 2.0e-3]
tds_5 = [3.8e-3, 3.1e-3, 1.5e-3]

x = np.arange(len(labels))  # the label locations
width = 0.35  # the width of the bars

fig, ax = plt.subplots()
rects1 = ax.bar(x - width / 2, tds_2, width, label="2nd TDS", color="tab:orange")
rects2 = ax.bar(x + width / 2, tds_5, width, label="5th TDS", color="tab:green")

# Add some text for labels, title and custom x-axis tick labels, etc.
def latex_float(f):
    float_str = "{0:.1e}".format(f)
    if "e" in float_str:
        base, exponent = float_str.split("e")
        return r"{0} \times 10^{{{1}}}".format(base, int(exponent))
    else:
        return float_str


ax.set_ylabel("Density (at.fr.)")
ax.set_xticks(x)
ax.set_xticklabels(labels)
plt.ticklabel_format(axis="y", style="sci", scilimits=(0, 0), useMathText=True)

ax.legend()

ax.bar_label(rects1, padding=3, labels=["$" + latex_float(f) + "$" for f in tds_2])
ax.bar_label(rects2, padding=3, labels=["$" + latex_float(f) + "$" for f in tds_5])
ax = plt.gca()
ax.spines["right"].set_visible(False)
ax.spines["top"].set_visible(False)
fig.tight_layout()

plt.show()
