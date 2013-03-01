

class Atmosphere(object):
    """
    Summary of the current atmospheric conditions.

    Attributes:
        humidity: Current humidity as a percentage (float).
        visibility: Visibility in units specified in the distance variable of
            the Units class (float).
        pressure: Barometric pressure in units specified in the pressure
            variable of the Units class (float).
        rising: State of the barometric pressure. 0 for steady, 1 for rising,
            or 2 for falling (integer).
    """

    def __init__(self, atmosphere):
        self.humidity = float(atmosphere['humidity'])
        self.visiblity = float(atmosphere['visibility'])
        self.pressure = float(atmosphere['pressure'])
        self.rising = int(atmosphere['rising'])
