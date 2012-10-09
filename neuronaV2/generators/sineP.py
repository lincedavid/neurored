#!/usr/bin/python

from math import cos
from math import sin
from math import pi
from math import pow as pot
from math import factorial
from math import radians

def cosine(degrees):
    rads = radians(degrees)
    suma = 0
    for n in range(85):
        suma = suma + ((pot(-1,n)) * (pot(rads,2*n) / factorial(2*n)))
    return suma

def sine(degrees):
    rads = radians(degrees)
    suma = 0
    for n in range(85):
        suma = suma + ((pot(-1,n)) * (pot(rads,2*n+1) / factorial(2*n+1)))
    return suma

sines = list()
cosines = list()

for i in range(0,360,10):
    sines.append(round(sin(radians(i)),6))
    #cosines.append(round(cos(radians(i)),6))

print len(sines)
print sines
#print len(cosines)
#print cosines

with open("sine.txt", "w") as sineOutput:
    with open("cosine.txt", "w") as cosineOutput:
        for i in range(1,36):
            print sines[:len(sines)-i] + [",-1,", sines[(len(sines)-i)]]
        for i in range(2,36):
            print sines[:i] + [",-1,", sines[i]]
        for i in range(1,36):
            print sines[len(sines)-i:] + [",-1,", sines[(len(sines)-i-1)]]
        for i in range(2,36):
            print sines[i:] + [",-1,", sines[i]]
#            o
#            print "cos(%d) = %f\tcosine(%d) = %f\n" % (i, cos(radians(i)), i, cosine(i))
#            print "sin(%d) = %f\tsine(%d) = %f\n" % (i, sin(radians(i)), i, sine(i))
#            sineOutput.write("%f," % (sin(radians(i))))
#            cosineOutput.write("%f,"  % (cos(radians(i))))
#        sineOutput.write("-1,")
#        cosineOutput.write("-1,")



