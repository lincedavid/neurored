from sys import argv
from numpy import *
from numpy.random import *


class neu(object):
    
    def Entrada(self,n):
        entrada = uniform(low=-1, high=1, size=(1,n))
        entrada = append(entrada, -1.0)
        #print "ENTRADA:", entrada
        return entrada
    
    def W(self, n):
        w = uniform(low=-1, high=1, size=(1,n+1))
        #print "PESOS:", w
        return w
    
    def Act(self, w, entrada):
        a = w*entrada
        #print a
        act = a.sum()
        #print "SUMATORIA PARA ACTIVACION:", act
        return act
    
    def Compara(self, act):
        if(act>=0):
            y = 1
            #print True
            #print y
        else:
            y = 0
            #print False
            #print y
        return y


    def __init__(self, n, num):
        p=0
        w = self.W(n) 
        for p in range(num):
            entrada = self.Entrada(n)
            act = self.Act(w, entrada)
            y = self.Compara(act)
            print entrada[0],entrada[1], y


n = neu(int(argv[1]), int (argv[2]))



