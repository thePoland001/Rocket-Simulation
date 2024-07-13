env = Environment(latitude = 34.64146, longitude = -86.54371, elevation = 266.3)
tomorrow = datetime.datetime.today() + datetime.timedelta(days=1)

env.set_date(
    (tomorrow.year, tomorrow.month, tomorrow.day, 12)
)  
env.set_atmospheric_model(type = 'Forecast', file = "GFS")
