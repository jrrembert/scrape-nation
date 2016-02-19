import datetime
import json

import scrapy

from elected_officials.items import GovernorItem


class GovernorSpider(scrapy.Spider):
    name = "governor_spider"
    allowed_domains = ['en.wikipedia.org']
    start_urls = ['https://en.wikipedia.org/wiki/List_of_current_United_States_governors']

    def __init__(self, *args, **kwargs):
        super(GovernorSpider, self).__init__(*args, **kwargs)

    def parse(self, response):
        governor_table = response.xpath('//*[@id="mw-content-text"]/table[2]')

        governors_headings = governor_table.xpath('tr[1]/th/text()').extract()
        state_names = governor_table.xpath('tr/td/div[2]/a/text()').extract()
        governor_names = governor_table.xpath('tr/td[3]/span/text()').extract()
        parties = governor_table.xpath('tr/td[4]/a/text()').extract()
        took_office = governor_table.xpath('tr/td[6]/span[2]/text()').extract()
        term_end = governor_table.xpath('tr/td[7]/text()').extract()

        with open('tests/fixtures/state_names_to_abbreviations.json', 'r') as f:
            state_abbreviations = json.load(f)

        item = GovernorItem()

        try:
            for i in xrange(50):
                name = ' '.join(reversed(governor_names[i].split(','))).lstrip()

                item['name'] = name
                item['state'] = state_names[i]
                item['state_abbreviation'] = state_abbreviations[state_names[i]]
                item['party'] = parties[i]
                item['took_office'] = took_office[i]
                item['term_end'] = term_end[i]
                item['last_updated'] = datetime.datetime.now()
                item['title'] = 'governor'

                yield item

        except IndexError as error:
            print("\033[91mError: {}\033[0m".format(error))
