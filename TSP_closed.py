# -*- coding: utf-8 -*-
"""
Created on Tue Aug 14 17:51:39 2018

@author: yuwan
"""

'''
For our TSP, we will use the dp approach. However, for the closed version of
TSP, we take into consideration how long we expect to stay in any location
and when the location closes. As a result, we will only return valid paths

If there is no valid path, we should return "no path"
'''
import numpy as np


#similar implementation of dp from 


def travelingSalesman_closing(dist_array, addresses, duration, closing):
    #similar to travelingSalesman_dp, but include inputs for duration and closing
    #duration will be amount of time spent at each location
    #closing will be how much time until a store closes
    
    n = len(dist_array)
    dp = [[np.inf for i in range(n-1)] for j in range(2**(n-1))]
    outstr = [['0' for i in range(n-1)] for j in range(2**(n-1))]
    dp[0] = [0 for i in range(n-1)]
    for i in range(n-1):
        # initialize dp by going to every possible location first
        dp[2**i][i] = dist_array[0][i+1] + duration[i]
        outstr[2**i][i] = '0,{}'.format(i+1)
    
    subsets = range(1,2**(n-1))
    for subset in sorted(subsets, key = lambda x: bin(x).count('1')):
        #iterate over all bitmask accordingly
        for i in range(n-1):
            if not  (1 << (i)) & subset:
                # if we dont want to check node i, skip it
                continue
            for k in range(n-1):
                #check all other visited nodes in subset except i, and see which 
                #node we should come from to minimize the path that ends with i
                
                if k == i or not (1 << (k)) & subset:
                    # if we already visited k or k is i, then we dont need to
                    # test if we can get through to i via k faster
                    continue
                
                #distance from visiting every node in subset except i and ending with k
                #if the minimum, then C(S,i) is minimum path that starts at 0, 
                #ends with i, and visits every node in this subset
                temp = dp[subset - (1<<i)][k] + dist_array[k+1][i+1] + duration[i]
                if temp < dp[subset][i] and temp < closing[i]:
                    #only allow a path if we can spend required time before location closes
                    dp[subset][i] = temp
                    outstr[subset][i] = outstr[subset - (1<< i)][k] + ',{}'.format(i+1)
                
    #finish the loop for all shortest paths that start at 0 and end at every other node 
    out = [path + dist_array[i+1][0] 
                for i, path in zip(range(n-1),dp[2**(n-1)-1])]
    
    ind = out.index(min(out))
    if min(out) == np.inf:
        return -1, []
    else:
        return out[ind], [addresses[int(i)] for i in outstr[2**(n-1)-1][ind].split(',')]
