import scrapy

class fake_news_spider(scrapy.Spider):
    name = 'fake_news'

    start_urls = [
        'https://www.segnidalcielo.it/?s='
    ]

    def parse(self, response):
        for titles in response.xpath("//article[@class='post-entry']"):

            yield {
                'title_text' : titles.xpath("//h4[@class='entry-title']/a/@title").extract_first()
            }