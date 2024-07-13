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
