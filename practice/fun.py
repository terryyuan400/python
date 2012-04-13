#!/usr/bin/python

def max(a, b):
    '''max function'''
    if a > b:
        print a, "is max"
        return a
    else:
        print b, "is max"
        return b

print max(4,7)
print max.__doc__
