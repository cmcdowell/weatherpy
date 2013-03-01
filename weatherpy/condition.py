
from dateutil import parser


class Condition(object):
    """
    The current weather conditions.

    Attributes:
        code: The condition code for the forecast. The possible values for the
            code are described at the following URL (integer).
            http://developer.yahoo.com/weather/#codes
        date: The date and time the forecast was posted, time-zone unaware
            (datetime).
        temperature: The current temperature in the units specified in the
            temperature variable of the Units class (int).
        text: A textual description of the conditions. E.g. Partly Cloudy
            (string).
    """

    def __init__(self, condition):
        self.temperature = int(condition['temp'])
        self.date = parser.parse(condition['date'], ignoretz=True)
        self.text = condition['text']
        self.code = int(condition['code'])
