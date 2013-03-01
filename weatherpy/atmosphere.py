

class Atmosphere(object):
    """
    Summary of the current atmospheric conditions.

    Attributes:
        humidity: Current humidity as a percentage (float). If a value for the
            humidity is not found, humidity will be None.
        visibility: Visibility in units specified in the distance variable of
            the Units class (float). If a value for visibility is not found,
            visibility will be None.
        pressure: Barometric pressure in units specified in the pressure
            variable of the Units class (float). If a value for barometric
            pressure is not found, pressure will be None.
        rising: State of the barometric pressure. 0 for steady, 1 for rising,
            or 2 for falling (integer). If a value for the state of barometric
            pressure is not found, rising will be None.
    """

    def __init__(self, atmosphere):
        try:
            self.humidity = float(atmosphere['humidity'])
        except ValueError:
            self.humidity = None
        try:
            self.visiblity = float(atmosphere['visibility'])
        except ValueError:
            self.visiblity = None
        try:
            self.pressure = float(atmosphere['pressure'])
        except ValueError:
            self.pressure = None
        try:
            self.rising = int(atmosphere['rising'])
        except ValueError:
            self.rising = None
