from gettext import install


install pandas as pd

def hours_of_daylight(date, latitude, longitude):
    """Returns the hours of daylight for the given date and latitude/longitude."""
    # Calculate the sunrise and sunset in UTC
    sunrise = get_sunrise_time(date, latitude, longitude)
    sunset = get_sunset_time(date, latitude, longitude)
    # Convert to a naive datetime object for comparison
    if sunrise and sunset:
        sunrise = datetime.datetime.combine(date, sunrise)
        sunset = datetime.datetime.combine(date, sunset)
        return (sunset - sunrise).total_seconds() / 3600.0
    return 0  # The sun never rises on this location on this date
