# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
from pymongo import MongoClient


class GovernorPipeline(object):

    governor_collection = 'governors'

    def __init__(self, mongo_uri, mongo_db):
        self.mongo_uri = mongo_uri
        self.mongo_db = mongo_db

    @classmethod
    def from_crawler(cls, crawler):
        return cls(mongo_uri=crawler.settings.get('MONGO_URI'),
                   mongo_db=crawler.settings.get('MONGO_NAME'))

    def open_spider(self, spider):
        self.client = MongoClient(
            self.mongo_uri,
            connectTimeoutMS=spider.settings.get('CONNECT_TIMEOUT') or 20000,
            socketTimeoutMS=spider.settings.get('SOCKET_TIMEOUT') or None,
            socketKeepAlive=spider.settings.get('SOCKET_KEEP_ALIVE') or False
        )
        self.db = self.client[self.mongo_db]

    def close_spider(self, spider):
        self.client.close()

    def process_item(self, item, spider):
        self.db[self.governor_collection].insert(dict(item))
        return item
