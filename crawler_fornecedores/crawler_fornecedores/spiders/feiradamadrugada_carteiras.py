import scrapy
import re
import urllib
import os

from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors import LinkExtractor
from crawler_fornecedores.items import FeiraDaMadrugadaCarteiras

class FeiraDaMadrugadaCarteirasSpider(CrawlSpider):
	name = "feiradamadrugadacarteiras"
	site = "http://www.feiradamadrugadasp.com.br/"
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
		item['refCode'] = refCode[0].replace("#", "").upper()
		item['model'] = re.match(r"[a-zA-Z-#]*[0-9-]*", item['refCode']).group()
		item['price'] = response.selector.xpath("//div[@class='elementos']/div[@class='valores']/text()").extract()[0].strip()
		item['discountPrice'] = response.selector.xpath("//div[@class='elementos']/div[@class='valores']/span/span[@class='productSpecialPrice']/text()").extract()[0].strip()
		inStock = response.selector.xpath("//div[@class='marg_top10']/span/text()").extract()
		item['inStock'] = "0"
		if inStock:
			item['inStock'] = re.match(r"[a-zA-Z-#]*[0-9-]*", inStock[0]).group()
		item['description'] = response.selector.xpath("string(//div[@class='desc3']/p[1])").extract()[0].strip().encode("utf-8")
		item['dimensions'] = response.selector.xpath("//div[@class='desc3']/p[3]/text()").extract()[0].strip().encode("utf-8")

		therePhotos = response.selector.xpath("//div[@class='prod_info']/div[@class='thumb']/a/@href").extract()
		if therePhotos:
			item['photos'] = therePhotos

		#self.print_info(item)
		self.save_data(item)

	def save_data(self, item):
		path = '/tmp/test/'
		destDir = path + item['model']
		fileInfoName = item['refCode']
		fileDest = destDir + '/' + fileInfoName

		if not(os.path.exists(destDir)):
			os.mkdir(destDir)

		with open (fileDest + '.txt', 'w') as f:
			f.write(str(item['url'] + "\n"))
			f.write(str(item['refCode'] + "\n"))
			f.write(str(item['price'] + "\n"))
			f.write(str(item['discountPrice'] + "\n"))
			f.write(str(item['inStock'] + "\n"))
			f.write(str(item['description'] + "\n"))
			f.write(str(item['dimensions'] + "\n"))

		for listItem in enumerate(item['photos']):
			imageURL = self.site + listItem[1]

			with open (fileDest + "-0" + str(listItem[0]) + ".jpg", 'wb') as imageFile:
				imageFile.write(urllib.urlopen(imageURL).read())
				print "OK"

	def print_info(self, item):
		print item['url']
		print item['refCode']
		print item['price']
		print item['inStock']
		print item['description']
		print item['dimensions']
		print item['photos']
		print "=" * 100
