# -*- coding: utf-8 -*-
"""
Created on Sun Jul 29 19:34:23 2018

@author: yuwan
"""

import shortest_path
import numpy as np

test_array = np.array([[   0.,  810.,  648.],
       [ 954.,    0.,  797.],
       [ 630.,  634.,    0.]])

print shortest_path.travelingSalesman_naive(test_array)
print shortest_path.travelingSalesman_dp(test_array)