import requests
import sunlight

import elected_officials.settings
from scripts.settings import SUNLIGHT_API_KEY


sunlight.config.API_KEY = SUNLIGHT_API_KEY

def get_current_members_of_congress(*args, **kwargs):
    fields = {key: kwargs[key] for key in kwargs}
    members = sunlight.congress.all_legislators_in_office(**fields)

    return members
