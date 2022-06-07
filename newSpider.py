import scrapy

class WhiskeySpider(scrapy.Spider):
	name = 'nagarik'
	start_urls = ['https://nagariknews.nagariknetwork.com/']

	def parse(self, response):
		for product in response.css('article.list-group-item'):
		  	x = list(product.css('a').attrib['title'])
		   	title = (''.join(item for tuple_ in x for item in tuple_))
			yield{
				'title':title,
				'description': product.css('p.d-lg-none').get(),
				'time' : product.css('time.npdate').attrib['data-pdate']
			}