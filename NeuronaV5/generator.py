#!/usr/bin/python

from math import sin,cos,pi

def radians(deg):
    return (deg)*(pi/180)
 
with open("f.txt", "w") as f:
    for a in range(0, 360, 1):
        f.write("%.3f,%.3f,%.3f,%.3f,%.3f,%.3f,-1,%.3f\n" %(sin(radians(a)), sin(radians(a+1)), sin(radians(a+2)), sin(radians(a+3)), sin(radians(a+4)), sin(radians(a+5)), sin(radians(a+6))))
    for b in range(0, 360, 1):
        f.write("%.3f,%.3f,%.3f,%.3f,%.3f,%.3f,-1,%.3f\n" %(cos(radians(b)), cos(radians(b+1)), cos(radians(b+2)), cos(radians(b+3)), cos(radians(b+4)), cos(radians(b+5)), cos(radians(b+6))))
