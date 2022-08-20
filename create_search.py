#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Example code for creating a Meltwater saved search in Python.
"""

# Install the requests library if it is not already installed -- pip3 install requests
import json
import requests

# Set up variables.
BASE_URL = "https://api.meltwater.com/v3/searches"
YOUR_MELTWATER_TOKEN = "oiAC1sHhqAJXHwCDIB26kr6lS7xE78lLgptJcJXA"

SEARCH = '("vaccine" OR "covid" OR "Coronavirus" OR "Quarantine" or "Pandemic")'
SEARCH_NAME = "DACSS604_Project"

headers = {"Content-Type": "application/json", "apikey": YOUR_MELTWATER_TOKEN}

# Meat of the API push.
r = requests.post(
    f"{BASE_URL}",
    headers=headers,
    data=json.dumps(
        {
            "search": {
                "type": "social",
                "category": "explore",
                "name": SEARCH_NAME,
                "query": {
                    "case_sensitivity": "no",
                    "not_keywords": ["Promotion", "offer", "marketing"],
                    "boolean": SEARCH,
                    "type": "boolean",
                },
            }
        }
    ),
)

print(r)
