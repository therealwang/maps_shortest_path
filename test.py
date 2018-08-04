# -*- coding: utf-8 -*-
"""
Created on Sun Jul 29 19:34:23 2018

@author: yuwan
"""


import numpy as np
import timeit
from test_cases import *
from shortest_path import *

print travelingSalesman_naive(test_array) 
#2236
print timeit.timeit('lambda x: travelingSalesman_naive(test_array)', 
              number = 1000) 
#0.000242029200308


print travelingSalesman_dp(test_array)
 #2236
print timeit.timeit('lambda x: travelingSalesman_dp(test_array)', 
              number = 1000)
#0.0008329427

#Naive works better for small n, as expected, what about 7x7?


print travelingSalesman_naive(test_array_larger) 
#89779
print timeit.timeit('lambda x: travelingSalesman_naive(test_array_larger)',
              number = 1000) 
#0.0001359289


print travelingSalesman_dp(test_array_larger)
 #2236
print timeit.timeit('lambda x: travelingSalesman_dp(test_array_larger)', 
              number = 1000)
#0.00026921497
