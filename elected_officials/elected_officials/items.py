# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html
import scrapy


class ElectedOfficialsItem(scrapy.Item):
    name = scrapy.Field(serializer=str)
    state = scrapy.Field(serializer=str)
    state_abbreviation = scrapy.Field(serializer=str)
    party = scrapy.Field(serializer=str)


class GovernorItem(ElectedOfficialsItem):
    took_office = scrapy.Field(serializer=str)
    term_end = scrapy.Field(serializer=str)
