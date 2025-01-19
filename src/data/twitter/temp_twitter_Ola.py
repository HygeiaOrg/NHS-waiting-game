
from datetime import datetime
from meteostat import Point, Daily

# choose a time frame
start = datetime(2022, 9, 30)
end = datetime(2022, 10, 28)

# specify your location where data is to be collected ie longitude, latitude, elevation
london = Point(51.507351, -0.127758,  7.971)

data = Daily(london, start, end)
data = data.fetch()

print(data)

data.to_csv('temperature1.csv')




