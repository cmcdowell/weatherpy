

class Astronomy(object):
    """
    Forcast information about the current astronomic conditions

    Attributes:
        sunrise: Today's sunrise time. The time is local time and in the format
            h:mm am/pm
        sunset: Today's sunset time. The time is local time and in the format
            h:mm am/pm
    """

    def __init__(self, astronomy):
        self.sunrise = astronomy['sunrise']
        self.sunset = astronomy['sunset']
