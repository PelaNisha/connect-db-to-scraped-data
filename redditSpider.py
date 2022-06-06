import scrapy

class WhiskeySpider(scrapy.Spider):
    name = 'first'
    start_urls = ['https://www.reddit.com/r/gameofthrones/']

    def parse(self, response):
        for product in response.css('div.rpBJOHq2PR60pnwJlUyP0'):
            yield{
                'title':product.css('span.FHCV02u6Cp2zYL0fhQPsO::text').get(),
                'no of comments':  product.css('div._2SdHzo12ISmrC8H86TgSCp._3wqmjmv3tb_k-PROt7qFZe ::text').get()
            }
        


