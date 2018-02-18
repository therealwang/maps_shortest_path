# -*- coding: utf-8 -*-
"""
Created on Sun Feb 18 16:12:14 2018

@author: yuwan
"""

import pandas as pd
import googlemaps


gmaps = googlemaps.Client(key='YOUR_KEY_HERE')

print gmaps.geocode('1406 Gerard St, Rockville, MD')