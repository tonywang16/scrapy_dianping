import scrapy
from tutorial.toutiao_items import ToutiaoItem
from datetime import datetime, timedelta,time


class ToutiaoSpider(scrapy.Spider):
	
	name = "toutiao"
	allowed_domains = ["toutiao.io"]
	start_urls = [
		"http://toutiao.io/"  
	]
	
	def parse(self, response):
		d = datetime.today()
		for x in range(0,3):
			d = d - timedelta(1)
			print "http://toutiao.io/prev/"+d.strftime('%Y-%m-%d')
			next_url = "http://toutiao.io/prev/"+d.strftime('%Y-%m-%d')
			url = response.urljoin(next_url)
			yield scrapy.Request(url, self.parse_dir_contents)
			
	def parse_dir_contents(self, response):
		for sel in response.xpath('//div[@class="post"]//h3[@class="title"]'):
			item = ToutiaoItem()
			item['title'] = sel.xpath('a/text()').extract()[0]
			item['link'] = sel.xpath('a/@href').extract()[0]
			yield item
			
	
	


