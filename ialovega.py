import FESTIM
from interpolated_expression import InterpolatedExpression
import numpy as np
import sympy as sp


atom_density_W = 6.3380e28

center = 10e-9
width = 4.5e-9
distribution = (
    1 / (width * (2 * 3.14) ** 0.5) * sp.exp(-0.5 * ((FESTIM.x - center) / width) ** 2)
)


def radius(i):
    a_0 = 0.318e-9
    pi = np.pi
    return (
        ((3**0.5) / 4 * a_0)
        + (3 / (4 * pi) * (a_0**3) / 2 * abs(i) / 4) ** (1 / 3)
        - (3 / (4 * pi) * (a_0**3) / 2) ** (1 / 3)
    )


def site_per_bubble(i):
    return 8e18 * 4 * np.pi * radius(i) ** 2


data_cb = np.genfromtxt("mykola_HF/cb.csv", delimiter=",", names=True)
data_ib = np.genfromtxt("mykola_HF/ib.csv", delimiter=",", names=True)

x_cb = data_cb["arc_length"]
y_cb = data_cb["cb"]

x_ib = data_ib["arc_length"]
y_ib = data_ib["ib"]

tds_number = 2

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
else:
    raise ValueError("Unknown tds_number")

density = y_cb * site_per_bubble(y_ib)

trap_distribution = InterpolatedExpression(x_cb, density)

flux = 2.5e19
implantation_time = 4.5e19 / flux

sim = FESTIM.Simulation()

sim.mesh = FESTIM.MeshFromRefinements(
    size=100e-6,
    initial_number_of_cells=100,
    refinements=[{"cells": 300, "x": 3e-6}, {"cells": 500, "x": 60e-9}],
)

sim.materials = FESTIM.Materials([FESTIM.Material(id=1, D_0=4.1e-7, E_D=0.39)])

k_0 = 4.1e-7 / (1.1e-10**2 * 6 * 6.3e28)
E_k = 0.39

trap_1 = FESTIM.Trap(
    k_0=k_0,
    E_k=E_k,
    p_0=1e13,
    E_p=1.08,
    density=density_1 * atom_density_W,
    materials=1,
)

trap_2 = FESTIM.Trap(
    k_0=k_0,
    E_k=E_k,
    p_0=1e13,
    E_p=1.2,
    density=density_2 * atom_density_W,
    materials=1,
)

trap_3 = FESTIM.Trap(
    k_0=k_0,
    E_k=E_k,
    p_0=1e13,
    E_p=1.42,
    density=density_3 * atom_density_W,
    materials=1,
)
trap_bubbles = FESTIM.Trap(
    k_0=k_0,
    E_k=E_k,
    p_0=1e13,
    E_p=1.42,
    density=trap_distribution,
    materials=1,
)
sim.traps = FESTIM.Traps([trap_1, trap_2, trap_3, trap_bubbles])

sim.sources = [
    FESTIM.Source(
        flux * distribution * (FESTIM.t <= implantation_time), field="solute", volume=1
    )
]

sim.T = FESTIM.Temperature(
    300
    + (FESTIM.t > implantation_time + 50) * (1 * (FESTIM.t - (implantation_time + 50)))
)

sim.boundary_conditions = [FESTIM.DirichletBC(value=0, surfaces=[1, 2], field=0)]

sim.settings = FESTIM.Settings(
    absolute_tolerance=1e10,
    relative_tolerance=1e-9,
    maximum_iterations=50,
    final_time=implantation_time + 400,
)

sim.dt = FESTIM.Stepsize(
    0.1,
    stepsize_change_ratio=1.1,
    t_stop=implantation_time + 30,
    stepsize_stop_max=5,
    dt_min=1e-5,
)

derived_quantities = FESTIM.DerivedQuantities(
    folder=folder, file="derived_quantities.csv"
)
derived_quantities.derived_quantities = [
    FESTIM.TotalVolume(1, volume=1),
    FESTIM.TotalVolume(2, volume=1),
    FESTIM.TotalVolume(3, volume=1),
    FESTIM.TotalVolume(4, volume=1),
    FESTIM.AverageVolume("T", volume=1),
    FESTIM.HydrogenFlux(surface=1),
    FESTIM.HydrogenFlux(surface=2),
]

sim.exports = FESTIM.Exports(
    [
        derived_quantities,
        FESTIM.XDMFExport(
            field="retention", label="retention", folder=folder, checkpoint=False
        ),
        FESTIM.XDMFExport(
            field="solute", label="mobile", folder=folder, checkpoint=False
        ),
    ]
)

sim.initialise()
sim.run()
