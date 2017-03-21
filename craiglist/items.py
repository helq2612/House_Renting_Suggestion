# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class MeetupItem(scrapy.Item):
	# define the fields for your item here like:
	# name = scrapy.Field()
	pid = scrapy.Field()
	url =scrapy.Field()
	price = scrapy.Field()
	info = scrapy.Field()
	date = scrapy.Field()
	title = scrapy.Field()

	pid1 = scrapy.Field()
	pid2 = scrapy.Field()
	longitude = scrapy.Field()
	latitude = scrapy.Field()
	num_bedroom = scrapy.Field()
	num_bathroom = scrapy.Field()

