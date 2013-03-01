from distutils.core import setup

setup(
    name = 'weatherpy',
    packages = ['weatherpy'],
    version = '1.0.2',
    description = 'Python wrapper for Yahoo weather API',
    author = 'Christopher McDowell',
    author_email = 'chris.p.mcdowell@gmail.com',
    url = 'https://github.com/cmcdowell/weatherpy',
    install_requires = ['python-dateutil'],
    classifiers = [
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Development Status :: 4 - Beta',
        'Operating System :: OS Independent',
        'License :: OSI Approved :: MIT License',
        'Intended Audience :: Developers',
        'Environment :: Other Environment',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Utilities',
    ],
    long_description = """\
Weatherpy, python wrapper for Yahoo weather API
-----------------------------------------------

Weatherpy is a package that allows you to simply and easily access Yahoo's
weather API. Give weatherpy a user agent and a WOEID and weatherpy will make
accessing elements of the RSS feed simple.

example.

    import weatherpy
    r = weatherpy.Response('Bob's weather script', 44544)
    print 'Wind: ', r.wind.speed, r.units.speed, r.wind.cardinal_direction()

gives

    Wind: 6 km/h N

Weatherpy is only tested with python 2.5+. Weatherpy is not compatible wihth
python 3.
""")
