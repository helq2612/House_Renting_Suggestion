# -*- coding: utf-8 -*-
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor 
from craiglist.items import MeetupItem
from scrapy import Request, Selector
import time

class FirstSpider(CrawlSpider):
	# crawl information on the search webpage on Craigslist
	name = "first"									# spider name
	DOWNLOAD_DELAY = 0.5							# time delay, to avoid hitting servers too hard			
	allowed_domains = ["corvallis.craigslist.org"]
	start_urls = ['https://corvallis.craigslist.org/search/apa']
	rules = [
    	Rule(LinkExtractor(
    			allow=['/search/apa\?s=\d*'],    	# allow to go to next page on Craigslist
    			deny = (r'.*format\=rss.*')
    		),
    		callback='parse1',
    		follow=True
    	)
    ]
 	print "Let's crawl for fun!!!"


	def parse1(self, response):
		self.logger.info('You are now crawling: %s', response.url)
		hxs = Selector(response)
		contents = hxs.xpath("//ul[@class='rows']/*")
		print "========================================================="
		print "now you are crawling"
		print "========================================================="
		idx = 0
		for idx, content in enumerate(contents):
			print "*****************************************",idx,"*****************************************"
			item = MeetupItem()
			t1 = content.xpath("@data-pid").extract()[0]     		#get the data-pid
			s2 = '//*[@data-pid=\''+str(t1)+'\']/a/@href'			#form a string 
			t2 = content.xpath(s2).extract()[0]						#use data-pid to get the url
			
			# t3 = price
			s3 = '//*[@data-pid=\''+str(t1)+'\']/p/span/span[@class="result-price"]/text()'
			t3 = content.xpath(s3).extract()					#use data-pid to get the price
			if t3 != []:
				t3 = t3[0]
			# t4 = info
			s4 = '//*[@data-pid=\''+str(t1)+'\']/p/span/span[@class="housing"]/text()'
			t4 = content.xpath(s4).extract()	

			# t5 = time
			s5 = '//*[@data-pid=\''+str(t1)+'\']/p/time/text()'
			t5 = content.xpath(s5).extract()[0]	

			# t6 = title:
			s6 ='//*[@data-pid=\''+str(t1)+'\']/p/a/text()'
			t6 = content.xpath(s6).extract()[0]	

			## get the sub link of each poster, then request it, to get new result
			link = "https://corvallis.craigslist.org"+t2

			## assign to item
			item["pid"] = t1
			item["url"] = link			
			item["price"] = t3
			item["info"] = t4
			item["date"] = t5
			item["title"] = t6
			idx += 1
			time.sleep(0.5)
			print "sleep 1 sec, item = \n", item
			if idx == 100: 		# this 100 can be substituded by len(contents)
				print "now test for next page"
				print "========================================================="
				break
			yield item

	




