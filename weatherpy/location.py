

class Location(object):
    """
    The location of the forecast

    Attributes:
        city: The name of the city (string).
        country: The two character country code for the country (string).
        region: The name of the state, territory, or region if given. Empty
            string if not given (string).
    """

    def __init__(self, location):
        self.city = location['city']
        self.region = location['region']
        self.country = location['country']
