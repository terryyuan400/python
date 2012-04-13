#!/usr/bin/env python

import os
sp = os.linesep

while True:
    fname = raw_input("input file name:")
    if os.path.exists(fname):
        print fname + " alreay exist."
        print "Error: %s alreay exist." % fname
    else:
        break

print "Enter lines:"
all = []
while True:
    entry = raw_input(">")
    if entry == '.':
        break
    else:
        all.append(entry)

fobj = open(fname, 'w')
fobj.writelines(['%s%s' %(x,sp) for x in all])
fobj.close()

