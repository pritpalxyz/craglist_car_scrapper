# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


import MySQLdb

class CragcarPipeline(object):

	def __init__(self):
		self.db = MySQLdb.connect("localhost","root","SERVER_PASS","craglist" )
		self.cursor = self.db.cursor()


	def process_item(self, item, spider):

		checksql = """ SELECT * FROM car where postUrl = '%s' """%(item['postUrl'])
		self.cursor.execute(checksql)
		oldPost = self.cursor.fetchone()
		if oldPost is None:
			sql = """ INSERT INTO car (title,prize,image_path,userEmail,description,postid,postedDate,otherInfo,postUrl) VALUES ('%s','%s','%s','%s','%s','%s','%s','%s','%s')"""%(item['title'],item['prize'],item['image_path'],item['userEmail'],item['description'],item['postid'],item['postedDate'],item['otherInfo'],item['postUrl'])
			self.cursor.execute(sql)
			self.db.commit()

		return item
