#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 10 22:05:19 2019

@author: nephilim
"""
import hashlib

def md5(str_):
    m = hashlib.md5()
    m.update(str_.encode("utf8"))
    print(m.hexdigest())
    return m.hexdigest()
a='Nephilim'
md5(a)