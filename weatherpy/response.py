
from astronomy import Astronomy
from atmosphere import Atmosphere
from condition import Condition
from dateutil import parser
from forecast import Forecast
from image import Image
from location import Location
from units import Units
from wind import Wind
import urllib2
import xml.etree.ElementTree as etree


class Response(object):
    """
    The base class that handles interacting with the Yahoo weather API.

    This class is the main class you will be using to interact with the API.
    You must call the class with a user agent (as a string) and the WOEID of
    the location you want the weather from (as an integer or long). You can
    find the WOEID of the location you want the weather from at the
    following URL.

    http://woeid.rosselliot.co.nz/

    You can also call the Response class with a keyword argument metric. This
    will determine whether your response is in metric or imperial units. By
    default metric is set to true.

    Attributes:
        astronomy: An instance of the astronomy.Astronomy class representing
            forecast information about the current astronomical conditions.
        atmosphere: An instance of the atmosphere.Atmosphere class representing
            forecast information about the current atmospheric conditions.
        condition: An instance of the condition.Condition class representing
            current weather conditions.
        conditions_title: The forecast title and time as a string.
        description: The description of the response RSS feed as a string.
        forecasts: A list of forecast.Forecast objects, one for each forecast
            in the RSS feed.
        image: An instance of the image.Image class representing the image in
            the RSS feed.
        language: The language of the response RSS feed as a string.
        last_bulid_date: The last time the feed was updated as a non time-zone
            aware datetime.
        latitude: The latitude of the location as a float.
        link: The URL of the weather page of the forecast for this location as
            a string.
        location: An instance of the location.Location class representing the
            location of the forecast.
        location: An instance of the location.Location class representing the
            location of the forecast.
        longitude: The longitude of the location as a float.
        metric: A boolean indicating if you want metric units or not.
        pub_date: The date and time the forecast was posted as a time-zone
            unaware datetime.
        title: The title of the response RSS feed as a string.
        today: An instance of the forecast.Forecast class representing today's
            forecast.
        tomorrow: An instance of the forecast.Forecast class representing
            tomorrow's forecast.
        ttl: An integer representing the Time To Live in minutes. This is how
            long the feed should be cached.
        units: An instance of the units.Units class representing the units for
            various aspects of the forecast.
        user_agent: The user agent you wish to supply to the Yahoo weather API.
        wind: An instance of the wind.Wind class representing forecast
            information about the wind.
        woeid: The WOEID of the location you want the weather from.
    """

    base_url = 'http://weather.yahooapis.com/forecastrss'
    weather_namespace = '{http://xml.weather.yahoo.com/ns/rss/1.0}'
    geo_namespace = '{http://www.w3.org/2003/01/geo/wgs84_pos#}'

    def __init__(self, user_agent, woeid, metric=True):
        self.user_agent = user_agent
        assert isinstance(woeid, (int, long))
        self.woeid = str(woeid)
        self.metric = metric
        self._channel = self._get_xml(metric)
        self.title = self._parse_text('title')

        if self.title == 'Yahoo! Weather - Error':
            raise Exception('City not found for WOEID {0}'.format(self.woeid))

        self.description = self._parse_text('description')
        self.language = self._parse_text('language')
        self.ttl = int(self._parse_text('ttl'))
        self.last_build_date = self._parse_last_build_date()
        self.forecasts = self._parse_forecasts()
        self.conditions_title = self._channel.find('./item/title').text
        self.latitude = float(self._parse_text('lat', self.geo_namespace))
        self.longitude = float(self._parse_text('long', self.geo_namespace))
        self.link = self._parse_text('link')
        self.pub_date = parser.parse(self._parse_text('pubDate'))
        self.today = self.forecasts[0]
        self.tomorrow = self.forecasts[1]
        self.image = self._parse_image()

        self.location = self._parse_attributes(
            'location',
            Location,
            self.weather_namespace
        )

        self.units = self._parse_attributes(
            'units',
            Units,
            self.weather_namespace
        )

        self.wind = self._parse_attributes(
            'wind',
            Wind,
            self.weather_namespace
        )

        self.atmosphere = self._parse_attributes(
            'atmosphere',
            Atmosphere,
            self.weather_namespace
        )

        self.astronomy = self._parse_attributes(
            'astronomy',
            Astronomy,
            self.weather_namespace
        )

        self.condition = self._parse_attributes(
            'condition',
            Condition,
            self.weather_namespace
        )

    def _get_xml(self, metric):
        """Returns the channel element of the RSS feed"""
        self._opener = urllib2.build_opener()
        self._opener.addheaders = [('User-agent', self.user_agent)]

        if metric:
            url = self.base_url + '?w={0}&u=c'.format(self.woeid)
        else:
            url = self.base_url + '?w={0}'.format(self.woeid)

        return etree.parse(
            self._opener.open(url)
        ).getroot()[0]

    def _parse_text(self, element_name, namespace=''):
        """
        Returns the text, as a string, of the specified element in the specified
        namespace of the RSS feed.

        Takes element_name and namespace as strings.
        """
        try:
            text = self._channel.find('.//' + namespace + element_name).text
        except AttributeError:
            raise Exception(
                'Element, {0} not found in RSS feed'.format(element_name)
            )

        return text

    def _parse_attributes(self, element_name, package_class, namespace=''):
        """
        Returns an instance of the package_class instantiated with a
        dictionary of the attributes from element_name in the specified
        namespace of the RSS feed.
        """
        return package_class(
            self._channel.find(
                './/{0}{1}'.format(namespace, element_name)
            ).attrib
        )

    def _parse_forecasts(self):
        """
        Returns a list of instances of the forecast.Forecast class. Each
        instance of the class is instantiated with the attributes of the
        forecast elements in the RSS feed.
        """
        forecasts = self._channel.findall(
            './/{0}{1}'.format(self.weather_namespace, 'forecast')
        )
        return [Forecast(forecast.attrib) for forecast in forecasts]

    def _parse_image(self):
        """
        Returns an instance of the image.Image class for the RSS feed.
        """
        image = {
            'title': self._channel.find('./image/title').text,
            'width': int(self._channel.find('./image/width').text),
            'height': int(self._channel.find('./image/height').text),
            'link': self._channel.find('./image/link').text,
            'url': self._channel.find('./image/url').text
        }

        return Image(image)

    def _parse_last_build_date(self):
        """
        Returns the last build date of the RSS feed as datetime.datetime
        object. Returned datetime is not time-zone aware
        """
        date = self._channel.find('lastBuildDate').text
        date = parser.parse(date, ignoretz=True)
        return date
