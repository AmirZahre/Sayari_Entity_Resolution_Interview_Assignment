# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class BusinessResults(scrapy.Item):
    # define the fields for your item here like:
    business = scrapy.Field()
    additional_information = scrapy.Field()
    # pass


class Metadata(scrapy.Item):
    # define the fields for your item here like:
    date = scrapy.Field()
    website = scrapy.Field()
    # pass

# test
# class QuoteResults(scrapy.Item):
#     # define the fields for your item here like:
#     text = scrapy.Field()
#     author = scrapy.Field()
#     tags = scrapy.Field()
