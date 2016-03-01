import requests
import sunlight
import unittest

from scripts.settings import SUNLIGHT_API_KEY
from scripts.congress_sunlight import *


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
