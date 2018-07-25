# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class JjsItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    Name = scrapy.Field()
    Phone = scrapy.Field()
    Email = scrapy.Field()
    #Address = scrapy.Field()
    Address = scrapy.Field()
    Description = scrapy.Field()
    Website = scrapy.Field()
    Contact = scrapy.Field()
    Latitude = scrapy.Field()
    Longitude = scrapy.Field()
    Image_Url = scrapy.Field()
    Image_File = scrapy.Field()
    Hours = scrapy.Field()
    pass

