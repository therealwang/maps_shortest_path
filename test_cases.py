# -*- coding: utf-8 -*-
"""
Created on Fri Aug 03 17:24:00 2018

@author: yuwan
"""

import numpy as np

test_array = np.array([[   0.,  810.,  648.],
       [ 954.,    0.,  797.],
       [ 630.,  634.,    0.]])

addresses = ['3737 Chestnut St, Philadelphia, PA 19104',
         '401 E City Ave, Bala Cynwyd, PA',
         '1900 Arch St, Philadelphia, PA']

test_array_larger = np.array([[    0.,   810.,   648.,  8463.,  8891., 42624., 23467.],
       [  954.,     0.,   797.,  8715.,  9143., 42875., 23718.],
       [  630.,   634.,     0.,  8490.,  8918., 42650., 23493.],
       [ 8564.,  8748.,  8602.,     0.,  1958., 35070., 15913.],
       [ 8793.,  8977.,  8831.,  1843.,     0., 34550., 15393.],
       [42392., 42576., 42430., 34825., 34327.,     0., 20525.],
       [23459., 23643., 23497., 15893., 15394., 20790.,     0.]])

addresses_larger = ['3737 Chestnut St, Philadelphia, PA 19104',
         '401 E City Ave, Bala Cynwyd, PA',
         '1900 Arch St, Philadelphia, PA',
         '1406 Gerard St, Rockville, MD',
         '1600 Pennsylvania Ave NW, Washington, DC',
         'Atlanta, GA',
         'Chapel Hill, NC']