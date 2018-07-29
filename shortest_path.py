# -*- coding: utf-8 -*-
"""
Created on Sun Feb 18 16:12:14 2018

@author: yuwan
"""

import pandas as pd
import numpy as np
import googlemaps
from googlemaps import distance_matrix as dm


'''
TODO: Travelling salesman approximations
TODO: Generate test cases
TODO: Interpretation of generic names?
'''

API_KEY = 'YOUR_KEY_HERE'
gmaps = googlemaps.Client(key=API_KEY)

def cleanMatrix(d, l):
    dist = np.zeros([l,l])
    dur = np.zeros([l,l])
    for r, i in zip(d['rows'],range(l)):
        for c, j in zip(r['elements'], range(l)):
            dist[i][j] = c['distance']['value']
            dur[i][j] = c['duration']['value']
    return dist, dur
        
    
def distanceMatrix(addresses):
    raw_matrix = dm.distance_matrix(gmaps, addresses, addresses)
    return cleanMatrix(raw_matrix, len(addresses))

def travelingSalesman(dist_array):
    #Naive - brute force
    return None


def main():
    l = ['3737 Chestnut St, Philadelphia, PA 19104',
         '401 E City Ave, Bala Cynwyd, PA',
         '1900 Arch St, Philadelphia, PA']
    dist, dur = distanceMatrix(l)
    return dist, dur
    
print main()