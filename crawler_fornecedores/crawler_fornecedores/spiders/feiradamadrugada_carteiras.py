import scrapy
import re

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
		item['refCode'] = refCode[0].replace("#", "")

		item['price'] = response.selector.xpath("//div[@class='elementos']/div[@class='valores']/text()").extract()[0].strip()
		item['discountPrice'] = response.selector.xpath("//div[@class='elementos']/div[@class='valores']/span/span[@class='productSpecialPrice']/text()").extract()[0].strip()
		inStock = response.selector.xpath("//div[@class='marg_top10']/span/text()").extract()[0]
		item['inStock'] = re.match(r"[a-zA-Z-#]*[0-9-]*", inStock).group()
		item['description'] = response.selector.xpath("string(//div[@class='desc3']/p[1])").extract()[0].strip()
		item['dimensions'] = response.selector.xpath("//div[@class='desc3']/p[3]/text()").extract()[0].strip()

		model = re.match(r"[a-zA-Z-#]*[0-9-]*", item['refCode']).group()

		print item['url']
		print item['refCode'].upper()
		print model
		print item['price']
		print item['discountPrice']
		print item['inStock']
		print item['description']
		print item['dimensions']
		print "=" * 100