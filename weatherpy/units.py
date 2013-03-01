

class Units(object):
    """
    Unit information about various aspects of the forecast

    Attributes:
        temperature: Temperature degree units, F for Fahrenheit C for Celsius
            (string)
        pressure: The units of barometric pressure, in pounds per square inch
            or millibars (string).
        distance: The units of distance in miles of km (string).
        speed: The units of speed in mph or kph (string)
    """

    def __init__(self, units):
        self.temperature = units['temperature']
        self.pressure = units['pressure']
        self.distance = units['distance']
        self.speed = units['speed']
