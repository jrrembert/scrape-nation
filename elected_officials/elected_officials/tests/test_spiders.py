import unittest

import requests

from elected_officials.spiders.governors_spider import GovernorSpider


class TestGovernorSpider(unittest.TestCase):

    def setUp(self):
        self.url = GovernorSpider.start_urls
        self.response = requests.get(self.url[0])

    def test_governor_site_available(self):
        self.assertEqual(response.status_code, 200)

    def test_governor_data_available(self):
        pass
