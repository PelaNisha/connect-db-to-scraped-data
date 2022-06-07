import scrapy

class WhiskeySpider(scrapy.Spider):
	name = 'nagarik'
	start_urls = ['https://nagariknews.nagariknetwork.com/']

	def parse(self, response):
		for product in response.css('article.list-group-item'):
			yield{
				'title':product.css('a').attrib['title'],
				'description': product.css('p.d-lg-none').get(),
				'time' : product.css('time.npdate').attrib['data-pdate']
			}


class GorkhaSpider(scrapy.Spider):
	name = 'gorkha'
	start_urls = ['https://gorkhapatraonline.com/']

	def parse(self, response):
		for product in response.css('div.col-lg-6'):
			p = product.css('h2.item-title')
			yield{
				'description': product.css('p.clamp-base.clamp-3::text').get(),
				'link': p.css('a').attrib['href']
			}
