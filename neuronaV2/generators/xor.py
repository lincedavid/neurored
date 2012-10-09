#!/usr/bin/python

from random import randint
from sys import argv

quantity = int(argv[1])

with open("xor.txt", "w") as myFile:
    for i in range(quantity):
        x = randint(0,1)
        y = randint(0,1)
        z = x ^ y
        #print "%d,%d,-1,%d\n" % (x, y, z)
        myFile.write("%d,%d,-1,%d\n" % (x, y, z))
