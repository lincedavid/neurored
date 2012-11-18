from numpy import *
from numpy.random import *
 
def Bin(n):#Aqui se toman las entradas en valores de 0 y 1
    bin = array([0])
    for i in range(n):
        bin = append(bin,int(input("Entrada: ")))
        i = i+1
    bin = delete(bin,[0])
    return bin
 
def Shuffle(n):#Aqui llena el arreglo de valores aleatorios entre 0 y 1
    pesos = uniform(low=0, high=1, size=(1,4))
    return pesos
 
def Suma(e,p):#Aqui multiplica las entradas con los pesos y suma el arreglo
    r = e*p
    resultado = r.sum()
    return resultado
 
def fin(m, u):#verifca si es acepta o rechaza conforme al valor umbral
    if(m>u):
        print "Acepta!"
    else:
        print "Rechaza!"
 
def main():
     
    n = 4
    u = 0.4
    bin = Bin(n)
    pesos = Shuffle(n)
    suma=Suma(bin,pesos)
     
    print "Numero de Entradas 4"
    print "Umbral : 0.4"
    print "Entradas " + str(bin)
    print "Pesos Aleatorios Entre 0 y 1 " + str(pesos)
    print "Suma " + str(suma)
    fin(suma,u)
  
main()
