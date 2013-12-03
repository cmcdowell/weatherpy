
from dateutil import parser


class Forecast(object):
    """
    The weather forecast for a specific day.

    Attributes:
        day: The day of the week to which the forecast applies. Possible values
            are Mon, Tue, Wed, Thu, Fri, Sat, Sun (string).
        date: The date to which to forecast applies, time-zone unaware (datetime)
        low: The forecasted low temperature for the day in units specified in
           the temperature variable of the Units class (integer). If a value for
           forecasted low temperature is not found, low will be None.
        high: The forecasted high temperature for the day in units specified in
           the temperature variable of the Units class (integer). If a value for
           forecasted high temperature is not found, high will be None.
        text: A textual description of conditions (string).
    """

    def __init__(self, forecast):
        self.day = forecast['day']
        self.date = parser.parse(forecast['date'], ignoretz=True)
        try:
            self.low = int(forecast['low'])
        except ValueError:
            self.low = None
        try:
            self.high = int(forecast['high'])
        except ValueError:
            self.high = None
        try:
            self.code = int(forecast['code'])
        except ValueError:
            self.code = None
        self.text = forecast['text']
