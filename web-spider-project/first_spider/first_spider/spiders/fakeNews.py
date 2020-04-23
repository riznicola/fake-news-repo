import scrapy
from first_spider.items import FakeNewsItem
from scrapy.loader import ItemLoader

class fake_news_spider(scrapy.Spider):
    name = 'fake_news'

    start_urls = [
        'https://www.segnidalcielo.it/?s='
    ]

    def parse(self, response):
        for titles in response.xpath("//article[@class='post-entry']"):
            l = ItemLoader(item=FakeNewsItem(), selector=titles)
            l.add_xpath('fake_news_title', ".//h4[@class='entry-title']/a")
            
            yield l.load_item()

        next_page = response.xpath('//a[@class="next page-numbers"]/@href').extract_first()
        if next_page is not None:
            next_page_link = response.urljoin(next_page)
            yield scrapy.Request(url=next_page_link, callback=self.parse)