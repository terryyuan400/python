#!/usr/bin/env python

class MyData():
    def __init__(self,nm):
        self.name = nm
        print 'init'

m = MyData(1)
m.x = 4
m.y = 5
print m.x + m.y
