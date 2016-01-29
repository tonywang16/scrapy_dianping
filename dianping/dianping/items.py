# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.item import Item, Field

class DianpingItem(scrapy.Item):
	# define the fields for your item here like:
	# name = scrapy.Field()
	shop_id = scrapy.Field()
	shop_name = scrapy.Field()
	good_summary= scrapy.Field()
	last_updated = scrapy.Field(serializer=str)