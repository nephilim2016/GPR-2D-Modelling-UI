#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 19 14:14:36 2019

@author: nephilim
"""

import numpy as np
from matplotlib.path import Path

def GetMask(data,xc,zc):
    data_mask = np.ones(data.shape)
    xzcrop = np.vstack((xc, zc)).T
    nr, nc = data_mask.shape
    zgrid, xgrid = np.mgrid[:nr, :nc]
    xzpix = np.vstack((xgrid.ravel(), zgrid.ravel())).T
    pth = Path(xzcrop, closed=False)
    mask = pth.contains_points(xzpix)
    mask = mask.reshape(data_mask.shape)
    return mask
