from pymongo import MongoClient
import requests
import sunlight

from elected_officials.settings import MONGO_URI, MONGO_NAME
from scripts.settings import SUNLIGHT_API_KEY


sunlight.config.API_KEY = SUNLIGHT_API_KEY

def get_current_members_of_congress(*args, **kwargs):
    """ Thin wrapper around Sunlight's Congress API 'all_legislators_in_office'
        method.
    """
    # TODO: Do we need every field returned from this?
    # TODO: Further confirmation needed to ensure this is the method I want
    #       to call. Check total senator and rep numbers.
    return sunlight.congress.all_legislators_in_office(**kwargs)

def connect():
    """ Connect to a db and return a client instance. """

    client = MongoClient(MONGO_URI)
    db = client[MONGO_NAME]
    return db

def write_to_db(data, collection):
    db = connect()
    collection_obj = db[collection]

    # TODO: some logging here would be great
    for item in data:
        collection_obj.insert_one(dict(item))

    db.client.close()


if __name__ == '__main__':
    members = get_current_members_of_congress()
    write_to_db(members, 'congress')
