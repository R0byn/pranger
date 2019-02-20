import scrapy


class IndexSpider(scrapy.Spider):
	name = "index"
	url_liste = []

	def start_requests(self):
		# start_urls = ['http://verbraucherinfo.ua-bw.de/lmk.asp?ref=3']

		urls = [
			'http://verbraucherinfo.ua-bw.de/lmk.asp?ref=3',
		]
		for url in urls:
			yield scrapy.Request(url=url, callback=self.parse)

	def parse(self, response):
		# self.log('URL: %s' % response.url)
		# page = response.url.split("/")[-2]
		# filename = 'index-%s.html' % page
		# with open(filename, 'wb') as f:
			# f.write(response.body)
		# self.log('Saved file %s' % filename)
		for menupunkt in response.css('div#aufklappmenue'):
			yield {
				#'RegBezirke': menupunkt.css('div.aussen span.menutag::text').getall(),
				'file_urls': menupunkt.css('div.aussen a.innen::attr(href)').getall()
			}