#!/usr/bin/env python

import os

fname = raw_input("input file name:")
try:
    fobj = open(fname, 'r')
except IOError, e:
    print e
else:
    for eachline in fobj:
        print eachline,
    fobj.close()
