from scrapy import Spider


class JAVSpider(Spider):
    """Custom Spider class for JAV scrapers.

    Allow file containing `start_urls` to be specified on command line.
    Saves all other passed parameters into `custom_settings`.
    """
    start_urls = ()

    custom_settings = {
        'ITEM_PIPELINES': {
            'generics.pipelines.JSONWriterPipeline': 300,
        },
        'DOWNLOADER_MIDDLEWARES': {
            'generics.downloadermiddlewares.XPathRetryMiddleware': 540,
        }
    }

    def __init__(self, start=None, **kwargs):
        self.custom_settings.update(kwargs)

        if start is not None:
            try:
                with open(start) as f:
                    self.start_urls = tuple(l.strip() for l in f.readlines())
            except OSError:
                self.start_urls = (start,)
