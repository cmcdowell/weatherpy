

class Wind(object):
    """
    Current forecast information about the wind.

    Attributes:
        chill: Wind chill in degrees (integer). If a value for wind chill is not
            found, chill will be None.
        direction: Wind direction in degrees (integer). If a value for wind
            direction is not found, direction will be None.
        speed: Wind speed in units specified in the speed attribute of the
            Units class (integer). If a value for wind speed is not found, speed
            will be None.
    """

    def __init__(self, wind):
        try:
            self.chill = int(wind['chill'])
        except ValueError:
            self.chill = None
        try:
            self.direction = int(wind['direction'])
        except ValueError:
            self.direction = None
        try:
            self.speed = float(wind['speed'])
        except ValueError:
            self.speed = None

    def cardinal_direction(self):
        """
        Returns the cardinal direction of the
        wind as a string. Possible returned values are N, E, S, W, and None.

        315 degrees to 45 degrees exclusive -> N
        45 degrees to 135 degrees exclusive -> E
        135 degrees to 225 degrees exclusive -> S
        225 degrees to 315 degrees exclusive -> W

        None if no direction found.
        """
        if self.direction is None:
            return None

        if self.direction > 360 or self.direction < 0:
            raise Exception('Direction out of range')

        if (315 <= self.direction) <= 360 or 0 <= (self.direction) < 45:
            return 'N'
        elif 45 <= self.direction < 135:
            return 'E'
        elif 135 <= self.direction < 225:
            return 'S'
        elif 225 <= self.direction < 315:
            return 'W'
