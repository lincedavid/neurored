from random import uniform, randint
from sys import argv

class neurona(object):
    def tomarValores(self, cantidad):
        a = list()
        for i in range(cantidad):
            i = raw_input("Dame el valor del "+str(i+1)+" Axioma: ")
            a.append(int(i))
        return a

    def asignarValoresAxioma(self, cantidad):
        a = list() #lista de valores de los axiomas
        for i in range(cantidad):
            i = randint(0, 1)
            a.append(i)
        return a

    def asignarPesoSinapsis(self, lista):
        b = 0.0
        for i in lista:
            ra = float(uniform(0,1))
            b += float(i*ra) #Suma que dara la salida a la neurona si pasa el filtro
        return b

    def comprobarUmbral(self, sumatoria, umbral): #En toda funcion agregamos el self
        if sumatoria > umbral: return True
        else: return False

    def __init__(self, axiomas, umbral):
        print axiomas
        print self.asignarValoresAxioma(axiomas)#mandar llamar un metodo

objecto = neurona(int(argv[1]), float(argv[2]))
       
#axiomas = int(argv[1])
#umbral = float(argv[2])

#a = asignarValoresAxioma(axiomas)
#a = tomarValores(axiomas)
#b = asignarPesoSinapsis(a)
#c = comprobarUmbral(b, umbral)

#print "umbral es: "+ str(umbral)
#print a
#print b
#print c

