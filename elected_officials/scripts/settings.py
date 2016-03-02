# -*- coding: utf-8 -*-

SUNLIGHT_API_KEY = ""

try:
    LOCAL_SETTINGS
except NameError:
    try:
        from scripts.local_settings import *
    except:
        print("No local_settings.py file found - using settings from settings.py")
