from sys import argv
from numpy import *
from numpy.random import *


class neu(object):
    
    def Entrada(self,n):#crea las entradas
        entrada = uniform(low=-1, high=1, size=(1,n))#el size sirve para que sea vector de solo 1 dimension y la n cuantos valores tendra
        entrada = append(entrada, -1.0)#se le agrega el valor de menos 1 para evitar agregar valor umbral
        #print "ENTRADA:", entrada
        return entrada
    
    def W(self, n):#Creacion de pesos
        w = uniform(low=-1, high=1, size=(1,n+1))#low rango minimo y high maximo lo que hace es darme valores entre -1 y 1
        #print "PESOS:", w
        return w
    
    def Act(self, w, entrada):#multiplica y suma los vectores de peso y entrada
        a = w*entrada#multiplica vectores
        #print a
        act = a.sum()#suma el vector ya multiplicado
        #print "SUMATORIA PARA ACTIVACION:", act
        return act
    
    def Compara(self, act):#compara el valor de activacion si es 0 es verdadero si no es falso
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
        w = self.W(n) #primero se crean los pesos aleatoriamente
        for p in range(num):#hace las iteraciones
            entrada = self.Entrada(n)#crea entradas
            act = self.Act(w, entrada)#hace las operaciones para obtener la activacion
            y = self.Compara(act)#compara para obtener el valor de salida
            print entrada[0],entrada[1], y#imprime dos valores del vector y la salida


n = neu(int(argv[1]), int (argv[2]))
#toma los dos valores importantes que son n el numero de valores dentro del 
#vector y num que son el numero de veces que quiero que de un vector de 
#de entradas nuevo haga todo el proceso
