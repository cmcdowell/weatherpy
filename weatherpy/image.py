

class Image(object):
    """
    The image use to identify the RSS feed

    Attributes:
        height: The height of the image in  pixels (int).
        link: Link to Yahoo weather.
        title: The title of the image (string).
        url: The url of the image (string).
        width: The width of the image in pixels (int).
    """

    def __init__(self, image):
        self.title = image['title']
        self.width = image['width']
        self.height = image['height']
        self.link = image['link']
        self.url = image['url']

    def as_html(self):
        """
        Returns the image of the Yahoo rss feed as an html string
        """

        return '<a href="{0}"><img height="{1}" width="{2}" src="{3}" alt="{4}"></a>'.format(
            self.link, self.height, self.width, self.url, self.title)
