#Introduction

Weatherpy is a package that allows you to simply and easily access [Yahoo's](http://developer.yahoo.com/weather)
weather API. Give weatherpy a user agent and a WOEID and weatherpy will make
accessing elements of the RSS feed simple. WOEID (Where On Earth Identifiers)
can be found [here](http://woeid.rosselliot.co.nz).  
  
lets have a look at some of the things you can do.

    import weatherpy
    r = weatherpy.Response('My test user agent, 444544, metric=False)
    print '{0}, {1} \n'.format(r.location.city, r.locaton.country) 
    print '\tWind: {0}{1}'.format(r.wind.speed, r.units.speed)
    print '\tSunrise: {0}'.format(r.astronomy.sunrise)
    print '\tSunset: {0}'.format(r.astronomy.sunset)
    print '\tConditions: {0}'.format(r.conditions.text)

Gives something like.

    Belast, UK

        Wind: 7mph
        Sunrise: 6:30 am
        Sunset: 11:40 pm
        Conditions: Partly Cloudy

#Installation

    pip install weatherpy

#Examples and Documentation

For a number of code example and documentation please visit weatherpy's
[github wiki](http://github.com/cmcdowell/weatherpy/wiki).

#Licence 

Weatherpy is licenced under the MIT licence. For the full licence look at the 
LICENCE.txt file.
