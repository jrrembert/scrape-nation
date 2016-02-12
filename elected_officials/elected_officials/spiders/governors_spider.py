import scrapy


class GovernorSpider(scrapy.Spider):
    name = "Governor Spider"
    allowed_domains = ['en.wikipedia.org']
    start_urls = ['https://en.wikipedia.org/wiki/List_of_current_United_States_governors']

    def parse(self, response):
        governors_headings = response.xpath('//*[@id="mw-content-text"]/table[2]/tr[1]/th/text()').extract()
        governors = response.xpath("//table/tr")[2:52]
        state_names = response.xpath('//*[@id="mw-content-text"]/table[2]/tr/td/div[2]/a/text()').extract()
        governor_names = ""
        parties = ""
        took_office = ""
        term_end = ""
        self.logger.info('Response from {0}'.format(request.url))
