
from dateutil import parser


class Condition(object):
    """
    The current weather conditions.

    Attributes:
        code: The condition code for the forecast. The possible values for the
            code are described at the following URL (integer).
            http://developer.yahoo.com/weather/#codes
            If no code is found code will be None.
        date: The date and time the forecast was posted, time-zone unaware
            (datetime).
        temperature: The current temperature in the units specified in the
            temperature variable of the Units class (integer). If no value for the
            temperature is found, temperature will be None.
        text: A textual description of the conditions. E.g. Partly Cloudy
            (string).
    """

    def __init__(self, condition):
        try:
            self.temperature = int(condition['temp'])
        except ValueError:
            self.temperature = None
        self.date = parser.parse(condition['date'], ignoretz=True)
        self.text = condition['text']
        try:
            self.code = int(condition['code'])
        except ValueError:
            self.code = None
