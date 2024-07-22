erika = Rocket(
    radius=0.08,
    mass=20,
    inertia = (0,0,0),
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

nose_cone = erika.add_nose(length=0.4, kind="vonKarman", position=3.5)
tail = erika.add_tail(top_radius=0.0635, bottom_radius=0.042, length=0.06, position=-2.194656)

fin_set = erika.add_trapezoidal_fins(
    n=4,
    root_chord=0.120,
    tip_chord=0.060,
    span=0.110,
    position=-2.04956,
    cant_angle=0.5,
    airfoil=("NACA0012-radians.csv", "radians"),
)

