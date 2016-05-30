# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class CragcarItem(scrapy.Item):
	title 			= scrapy.Field()
	prize 			= scrapy.Field()
	image_path 		= scrapy.Field()
	userEmail 		= scrapy.Field()
	description 	= scrapy.Field()
	postid			= scrapy.Field()
	postedDate 		= scrapy.Field()
	otherInfo 		= scrapy.Field()
	postUrl 		= scrapy.Field()
