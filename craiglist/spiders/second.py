# -*- coding: utf-8 -*-
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor 
from craiglist.items import MeetupItem
from scrapy import Request, Selector
import csv

class SecondSpider(CrawlSpider):
	# crawl information on each poster webpage
	name = "second"				# spider name
	urlpool, pidpool = [], []	# url and pid pool
	# read csv file obtained by spider 'first'
	with open('first.csv') as f:
		rows = csv.reader(f)
		for row in rows:
			print row[3]
			urlpool.append(row[3])
			pidpool.append(row[5])
	
	DOWNLOAD_DELAY=1
	allowed_domains = ["corvallis.craigslist.org"]
	start_urls = urlpool[1:]

	def parse(self, response):
		print response.url
		item = MeetupItem()
		hxs = Selector(response)
		latitude = hxs.xpath("//div[@class='mapbox']/div/@data-latitude").extract()
		longitude = hxs.xpath("//div[@class='mapbox']/div/@data-longitude").extract()
		pid = hxs.xpath("//div[@class='postinginfos']/p[1]/text()").extract()
		num_bedroom = hxs.xpath("//p[@class='attrgroup']/span/b[1]/text()").extract()
		num_bathroom = hxs.xpath("//p[@class='attrgroup']/span/b[2]/text()").extract()
		if latitude != []:
			latitude = latitude[0]
		if longitude != []:
			longitude = longitude[0]
		if pid != []:
			pid = pid[0]
				
		item["pid1"] = pid
		item["url"] = response.url
		item["latitude"] = latitude
		item["longitude"] = longitude
		item["num_bedroom"] = num_bedroom
		item["num_bathroom"] = num_bathroom
		print "item = \n", item
		yield item
