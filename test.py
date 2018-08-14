# -*- coding: utf-8 -*-
"""
Created on Sun Jul 29 19:34:23 2018

@author: yuwan
"""

'''
TODO: make test cases more readable
'''

import numpy as np
import timeit
from test_cases import *
from shortest_path import *
import TSP_closed

print travelingSalesman_naive(test_array, addresses) 
#2236
print timeit.timeit('lambda x: travelingSalesman_naive(test_array, addresses)', 
              number = 1000) 
#0.000242029200308


print travelingSalesman_dp(test_array, addresses)
 #2236
print timeit.timeit('lambda x: travelingSalesman_dp(test_array, addresses)', 
              number = 1000)
#0.0008329427

#Naive works better for small n, as expected, what about 7x7?


print travelingSalesman_naive(test_array_larger, addresses_larger) 
#89779
print timeit.timeit('lambda x: travelingSalesman_naive(test_array_larger, addresses_larger)',
              number = 1000) 
#0.0001359289


print travelingSalesman_dp(test_array_larger, addresses_larger)
 #2236
print timeit.timeit('lambda x: travelingSalesman_dp(test_array_larger, addresses_larger)', 
              number = 1000)
#0.00026921497

print travelingSalesman_nearest(test_array, addresses)
print travelingSalesman_nearest(test_array_larger, addresses_larger)
print timeit.timeit('lambda x: travelingSalesman_nearest(test_array_larger, addresses_larger)', 
              number = 1000)
#doesnt get the right answer, but even for n = 7 is faster



test_array = np.array([[   0.,  910.,  648.],
       [ 954.,    0.,  797.],
       [ 630.,  634.,    0.]])

duration = [0,0]
closing_1 = [1e5, 1e5]
closing_2 = [910, 1e5]

#in this case, we test when there is no closing time, and when location 1 closes
#much earlier. we expect to have to take the longer path (to make sure we get
#to location 1 before it closes)

print TSP_closed.travelingSalesman_closing(test_array, ['Home','Loc1','Loc2'], 
                                     duration, closing_1) 
#(2236.0, ['Home', 'Loc2', 'Loc1'])


print TSP_closed.travelingSalesman_closing(test_array, ['Home','Loc1','Loc2'], 
                                     duration, closing_2) 

#(2337.0, ['Home', 'Loc1', 'Loc2'])

#What if there is no valid path?

closing_3 = [1, 1e5]

print TSP_closed.travelingSalesman_closing(test_array, ['Home','Loc1','Loc2'], 
                                     duration, closing_3) 
#(-1, [])