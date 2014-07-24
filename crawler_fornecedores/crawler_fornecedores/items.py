# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy

class CrawlerFornecedoresItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

class FeiraDaMadrugadaCarteiras(scrapy.Item):
	url = scrapy.Field()
	model = scrapy.Field()
	refCode = scrapy.Field()
	price = scrapy.Field()
	discountPrice = scrapy.Field()
	inStock = scrapy.Field()
	description = scrapy.Field()
	dimensions =scrapy.Field()
	photos = scrapy.Field()

class FeiraDaMadrugadaBolsasFemininas(scrapy.Item):
	url = scrapy.Field()
	model = scrapy.Field()
	refCode = scrapy.Field()
	price = scrapy.Field()
	discountPrice = scrapy.Field()
	inStock = scrapy.Field()
	description = scrapy.Field()
	typeOfMaterial = scrapy.Field()
	color = scrapy.Field()
	dimensions =scrapy.Field()
	photos = scrapy.Field()