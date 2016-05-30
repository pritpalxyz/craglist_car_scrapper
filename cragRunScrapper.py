import requests
import urllib, urllib2
from lxml import html
import os

class cragCityClass():

	def __init__(self):
		self.starturl = "http://www.craigslist.org/about/sites#US"
		self.citiesList = []
		self.callMethods()

	def callMethods(self):
		self.openUrl(self.starturl)
		self.grabCities()

	def grabCities(self):
		for city in self.htmll.xpath("//div[@class='colmask'][1]//a/@href"):
			city = self.makeUrl(self.getcity(city))
			self.citiesList.append(city)
			print city
			makeCrawlStr = """ scrapy crawl cragCar  -a urlToCrawl="%s" """%(city)
			try:
				os.system(makeCrawlStr)
			except:
				print "some Error while parsing ",city

	def makeUrl(self,city):
		makeUrl = "http://%s.craigslist.org/search/cto"%(city)
		return makeUrl

	def getcity(self,url):
		url = str(url)
		url = url.split('.')[0].replace('//','')
		return url

	def openUrl(self,urlToOpen):
		print "Openning url :-> ",urlToOpen
		data = requests.get(urlToOpen)
		self.htmll = html.fromstring(data.content)



if __name__ == '__main__':
	obj = cragCityClass()