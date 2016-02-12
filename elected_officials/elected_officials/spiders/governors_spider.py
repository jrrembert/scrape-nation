import scrapy


class GovernorSpider(scrapy.Spider):
    name = "Governor Spider"
    allowed_domains = ['en.wikipedia.org']
    start_urls = ['https://en.wikipedia.org/wiki/List_of_current_United_States_governors']

    def parse(self, response):
        governor_table = response.xpath('//*[@id="mw-content-text"]/table[2]')

        governors_headings = governor_table.xpath('tr[1]/th/text()').extract()
        state_names = governor_table.xpath('tr/td/div[2]/a/text()').extract()
        governor_names = governor_table.xpath('tr/td[3]/span/text()').extract()
        parties = governor_table.xpath('tr/td[4]/a/text()').extract()
        took_office = governor_table.xpath('tr/td[6]/span[2]/text()').extract()
        term_end = governor_table.xpath('tr/td[7]/text()').extract()
        #self.logger.info('Array lengths: {}, {}, {}, {}, {}'.format(len(state_names), len(governor_names), len(parties), len(took_office), len(term_end)))

        try:
            for x in xrange(50):
                print("{}: {}".format(governors_headings[0], state_names[x]))
                print("{}: {}".format(governors_headings[2], ' '.join(reversed(governor_names[x].split(',')))))
                print("{}: {}".format(governors_headings[3], parties[x]))
                print("{}: {}".format(governors_headings[5], took_office[x]))
                print("{}: {}".format(governors_headings[6], term_end[x]))

        except IndexError as error:
            print("Error: {}".format(error.msg))
