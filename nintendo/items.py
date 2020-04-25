# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

from scrapy.item import Item, Field

class NintendoItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


# Switch 主机的信息
class MachineItem(Item):

    name = 'Nintendo Switch'
    price = Field()
    unit = Field()
    pointPresent = Field()
    stock = Field()
    costFee = Field()

    url = Field()
    server = Field()
    timestamp = Field()

