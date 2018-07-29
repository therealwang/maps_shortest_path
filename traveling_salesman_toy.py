# -*- coding: utf-8 -*-
"""
Created on Sun Jul 29 19:42:00 2018

@author: yuwan
"""

import numpy as np
from sympy.utilities.iterables import multiset_permutations

def travelingSalesman_naive(dist_array):
    #naive, should work for small cases
    #pretty bad though, O(n!)
    l = len(dist_array)
    min_dist = np.inf
    for p in multiset_permutations(range(1, l)):
        test = 0
        for i,j in zip([0] + p, p + [0]):
            test += dist_array[i][j]
        if test < min_dist:
            min_dist = test
    return min_dist
