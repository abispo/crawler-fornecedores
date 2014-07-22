import scrapy
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors import LinkExtractor
from crawler_fornecedores.items import FeiraDaMadrugadaCarteiras

class FeiraDaMadrugadaCarteirasSpider(CrawlSpider):
	name = "feiradamadrugadacarteiras"
	start_urls = [
		"http://www.feiradamadrugadasp.com.br/carteiras-femininas-c-2.html",
		"http://www.feiradamadrugadasp.com.br/carteiras-femininas-c-2.html?page=2",
		"http://www.feiradamadrugadasp.com.br/carteiras-femininas-c-2.html?page=3",
		"http://www.feiradamadrugadasp.com.br/carteiras-femininas-c-2.html?page=4"
	]

	rules = (
		Rule(LinkExtractor(allow=["http://www\.feiradamadrugadasp\.com\.br/carteira-"]), 'parse_page'),
	)

	def parse_page(self, response):
		item = FeiraDaMadrugadaCarteiras()
		
		item['url'] = response.url.split("?")[0]
		refCode = response.selector.xpath("//div[@class='elementos']/h1/text()").extract()[0].split(" ")[-1:]
		print refCode[0]

