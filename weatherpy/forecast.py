
from dateutil import parser


class Forecast(object):
    """
    The weather forecast for a specific day.

    Attributes:
        day: The day of the week to which the forecast applies. Possible values
            are Mon, Tue, Wed, Thu, Fri, Sat, Sun (string).
        date: The date to which to forecast applies, time-zone unaware (datetime)
        low: The forecasted low temperature for the day in units specified in
           the temperature variable of the Units class (integer).
        high: The forecasted high temperature for the day in units specified in
           the temperature variable of the Units class (integer).
        text: A textual description of conditions (string).
    """

    def __init__(self, forecast):
        self.day = forecast['day']
        self.date = parser.parse(forecast['date'], ignoretz=True)
        self.low = int(forecast['low'])
        self.high = int(forecast['high'])
        self.text = forecast['text']
