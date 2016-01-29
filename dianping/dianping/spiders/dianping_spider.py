import scrapy,re,urllib2
from datetime import datetime, timedelta
from dianping.items import DianpingItem
from scrapy.selector import Selector
from scrapy.spider import Spider
from time import strftime

class DianpingSpider(scrapy.Spider):
	global gaga
	name = "dianping"
	allowed_domains = ["dianping.com"]
	response = urllib2.urlopen('https://ca.usastore.cn/huoguo.html')
	html = response.read()
	gaga = re.findall("shopid',(\d+)",html)
	gaga = sorted(set(gaga))
	start_urls = [ "http://www.dianping.com" ]
	
	
	def parse(self, response):
		d = datetime.today()
		for x in range(1,10):
			d = d - timedelta(1)
			print "http://www.dianping.com/shop/"+gaga[x]
			next_url = "http://www.dianping.com/shop/"+gaga[x]
			url = response.urljoin(next_url)
			yield scrapy.Request(url, self.parse_dir_contents)
			
	def parse_dir_contents(self, response):
		item = DianpingItem()		
		item['shop_id'] = re.search('shopId=(\d+)',response.body).group(1)
		item['shop_name'] = response.xpath('//*[@id="basic-info"]/h1/text()').extract()[0].strip()
		item['good_summary'] = []
		item['last_updated'] = strftime("%Y-%m-%d %H:%M:%S")
		for sel in response.xpath('//span[@class="good J-summary"]'):
			item['good_summary'].append(sel.xpath('a/text()').extract()[0])
		 
		yield item
		
		
	
	