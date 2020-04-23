# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

#la classe item si tiene il testo e pulisce i dati (input_processor)
class FakeNewsItem(scrapy.Item):
    fake_news_title = scrapy.Field(
        input_processor= remove_tags,
        output_processor= TakeFirst()
    )

class FirstSpiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass
