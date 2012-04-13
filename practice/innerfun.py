#!/usr/bin/env python

def foo():
    def bar():
        print 'in bar'

    print 'in foo'
    bar()

if __name__==" _main__":
    foo()
