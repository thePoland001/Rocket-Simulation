from rocketpy import Environment, SolidMotor, Rocket, Flight
from rocketpy.utilities import apogee_by_mass
from rocketpy.utilities import liftoff_speed_by_mass
from rocketpy import Function
import copy
import datetime
import numpy as np
import matplotlib.pyplot as plt
from math import exp
from rocketpy import Fluid, LiquidMotor, CylindricalTank, MassFlowRateBasedTank

%config InlineBackend.figure_formats = ['svg']
%matplotlib inline

env = Environment(latitude = 34.64146, longitude = -86.54371, elevation = 266.3)

tomorrow = datetime.datetime.today() + datetime.timedelta(days=1)

env.set_date(
    (tomorrow.year, tomorrow.month, tomorrow.day, 12)
)

env.set_atmospheric_model(type = 'Forecast', file = "GFS")

# Define fluids
oxidizer_liq = Fluid(name="N2O_l", density=1220)
oxidizer_gas = Fluid(name="N2O_g", density=1.9277)
fuel_liq = Fluid(name="ethanol_l", density=789)
fuel_gas = Fluid(name="ethanol_g", density=1.59)

# Define tanks geometry
tanks_shape = CylindricalTank(radius = 0.1, height = 1.2, spherical_caps = True)

# Define tanks
oxidizer_tank = MassFlowRateBasedTank(
    name="oxidizer tank",
    geometry=tanks_shape,
    flux_time=5,
    initial_liquid_mass=32,
    initial_gas_mass=0.01,
    liquid_mass_flow_rate_in=0,
    liquid_mass_flow_rate_out=lambda t: 32 / 3 * exp(-0.25 * t),
    gas_mass_flow_rate_in=0,
    gas_mass_flow_rate_out=0,
    liquid=oxidizer_liq,
    gas=oxidizer_gas,
)

fuel_tank = MassFlowRateBasedTank(
    name="fuel tank",
    geometry=tanks_shape,
    flux_time=5,
    initial_liquid_mass=21,
    initial_gas_mass=0.01,
    liquid_mass_flow_rate_in=0,
    liquid_mass_flow_rate_out=lambda t: 21 / 3 * exp(-0.25 * t),
    gas_mass_flow_rate_in=0,
    gas_mass_flow_rate_out=lambda t: 0.01 / 3 * exp(-0.25 * t),
    liquid=fuel_liq,
    gas=fuel_gas,
)

liquid_motor = LiquidMotor(
    thrust_source=lambda t: 4000 - 100 * t**2,
    dry_mass=2,
    dry_inertia=(0.125, 0.125, 0.002),
    nozzle_radius=0.075,
    center_of_dry_mass_position=1.75,
    nozzle_position=0,
    burn_time=5,
    coordinate_system_orientation="nozzle_to_combustion_chamber",
)
liquid_motor.add_tank(tank=oxidizer_tank, position=1.0)
liquid_motor.add_tank(tank=fuel_tank, position=2.5)

erika = Rocket(
    radius=0.08,
    mass=43.5,
    inertia=(6.321, 6.321, 0.034),
    power_off_drag="powerOffDragCurve.csv",
    power_on_drag="powerOnDragCurve.csv",
    center_of_mass_without_motor=0.75,
    coordinate_system_orientation="tail_to_nose",
)

rail_buttons = erika.set_rail_buttons(
    upper_button_position=1.5,
    lower_button_position=-0.5,
    angular_position=45,
)

erika.add_motor(liquid_motor, position=-1.255)

nose_cone = erika.add_nose(length=0.5, kind="vonKarman", position=2.5)
tail = erika.add_tail(top_radius=0.0635, bottom_radius=0.042, length=0.06, position=-1.194656)

fin_set = erika.add_trapezoidal_fins(
    n=4,
    root_chord=0.120,
    tip_chord=0.060,
    span=0.110,
    position=-1.04956,
    cant_angle=0.5,
    airfoil=("NACA0012-radians.csv", "radians"),
)

erika.all_info()
