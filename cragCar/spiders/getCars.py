import scrapy
from lxml import html
import requests
from cragCar.items import CragcarItem


class getCarList(scrapy.Spider):
	name = "cragCar"
	start_urls = ["http://www.craigslist.org/about/sites#US"]

	def __init__(self,urlToCrawl):
		
		# super(getCarList, self).__init__(*args, **kwargs)
		# self.proxy_pool = ['109.167.97.88']

		self.urlToCrawl = urlToCrawl
		self.carsXpath = "//div[@class='content']/p[@class='row']/a/@href"

	def parse(self,response):
		yield scrapy.Request(url=self.urlToCrawl,callback=self.scrapCars)

	def scrapCars(self,response):
		for href in response.xpath(self.carsXpath).extract():
			href = response.urljoin(href)
			yield scrapy.Request(url=href,callback=self.scrapParticularCar)

	def scrapParticularCar(self,response):
		item 				= CragcarItem()
		email 				= self.getEmailFromUrl(response.url)
		title 				= response.xpath("//span[@id='titletextonly']/text()").extract()
		title 				= title[0]
		prize 				= response.xpath("//span[@class='price']/text()").extract()
		try:prize 				= prize[0]
		except:prize = ''
		decription 			= self.list_to_string(response.xpath("//section[@id='postingbody']/text()").extract())
		postid				= response.xpath("//div[@class='postinginfos']/p[1]/text()").extract()
		postid 				= postid[0]
		postedDate 			= response.xpath(".//*[@id='pagecontainer']/section/section/div[2]/p[2]/time/text()").extract()
		print postedDate
		postedDate 			= postedDate[0]
		otherInfo 			= self.list_to_string(response.xpath("//p[@class='attrgroup']/span//text()").extract())
		image_path 			= response.xpath("//div[@class='tray']//img[@alt='image 1'][1]/@src").extract()
		try:image_path 		= image_path[0]
		except:image_path 	= ''




		item['title'] 		= title
		item['prize'] 		= prize
		item['image_path'] 	= image_path
		item['userEmail'] 	= email
		item['description'] = decription
		item['postid'] 		= postid
		item['postedDate'] 	= postedDate
		item['otherInfo'] 	= otherInfo
		item['postUrl'] 	= response.url
		yield item

	def list_to_string(self,allList):
		dummy = ''
		for text in allList:
			dummy = "%s %s"%(dummy,self.filter_my_string(text))
		return dummy

	def filter_my_string(self,strr):
		strr = str(strr)
		strr = strr.replace("\n","")
		strr = strr.replace("\r","")
		strr = strr.replace("'","")
		return strr

	def getEmailFromUrl(self,url):
		url 		= str(url)


		prefixUrl 	= url.split("/")[2]
		carId 		= url.split("/")[4].split('.')[0]
		makeUrl 	= "http://%s/reply/mil/cto/%s"%(prefixUrl,carId)

		data 		= requests.get(makeUrl)
		htmll 		= html.fromstring(data.content)

		email 		= htmll.xpath("//div[@class='anonemail']/text()")
		try:email 	= email[0]
		except:email = ''
		return email

