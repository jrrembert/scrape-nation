from pymongo import MongoClient
import requests
import sunlight
import unittest

from elected_officials.settings import MONGO_URI, MONGO_NAME
from scripts.settings import SUNLIGHT_API_KEY
from scripts.congress_sunlight import get_current_members_of_congress


class SunlightCongressTests(unittest.TestCase):

    def setUp(self):
        self.state = 'SC'

    def test_get_current_senators_for_state(self):
        """
        Get all currently serving senators for a specific state.
        """
        chamber = 'senate'
        sc_senators = get_current_members_of_congress(state=self.state,
                                                      chamber=chamber)
        self.assertEqual(2, len(sc_senators))

    def test_get_current_representatives_for_state(self):
        """
        Get all currently serving representatives for a specific state.
        """
        chamber = 'house'
        sc_representatives = get_current_members_of_congress(state=self.state,
                                                             chamber=chamber)
        self.assertEqual(7, len(sc_representatives))

class MongoTests(unittest.TestCase):

    def setUp(self):
        self.MONGO_NAME = "test_" + MONGO_NAME
        self.client = MongoClient(MONGO_URI)
        self.db = self.client[self.MONGO_NAME]
        self.collection_name = 'test_congress_collection'
        self.collection = self.db[self.collection_name]

    def tearDown(self):
        self.collection.drop()
        self.db.client.close()

    def test_db_is_available_and_documents_can_be_inserted(self):
        item = {
            'name': 'test_document'
        }
        doc_id = self.collection.insert_one(item).inserted_id
        self.assertIsNotNone(doc_id)
