#!/usr/bin/python

from random import randint
from sys import argv

quantity = int(argv[1])

with open("and.txt", "w") as myFile:
    for i in range(quantity):
        x = randint(0,1)
        y = randint(0,1)
        z = randint(0,1)
        a = x & y & z
        #print "%d,%d,%d,-1,%d\n" % (x, y, z, a)
        myFile.write("%d,%d,%d,-1,%d\n" % (x, y, z, a))
