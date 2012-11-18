from sys import argv
from numpy import *
from numpy.random import *

tasa_de_aprendizaje = 0.008
capa = list()

class neu(object):
    
    def Entrada(self,n):
        entrada = uniform(low=-1, high=1, size=(1,n))
        entrada = append(entrada, -1.0)
        return entrada
    
    def W(self, n):
        return uniform(low=-1, high=1, size=(1,n+1))
        
    
    def Condicion(self, n, w):
        return uniform(low=-1, high=1, size=(1,n+1))
        
    def respuestaDeseada(self, condicion, entrada):
        valorcondi = entrada*condicion
        valorc = valorcondi.sum()
        if (valorc>=0): return 1
        else: return 0
        
    def Act(self, w, entrada):
        a = w*entrada
        act = a.sum()
        return act
    
    def Compara(self, act):
        global capa#=list()
        if(act>=0): 
            capa = append(capa, 1)
            return 1
        else:
            capa = append(capa, 0)
            return 0
        

    def Entrena(self, w, y, respdesea, entrada):
        global tasa_de_aprendizaje
        entrenar = tasa_de_aprendizaje * (respdesea - y) * entrada
        w += entrenar
        return w
    
    def Capa(self):
        global capa
        capa = append(capa, -1)
        return capa

    def __init__(self, n, num, ncapas):
        global capa
        p=0
        w = self.W(n)
        condicion = self.Condicion(n, w)
        print w
        print condicion
        for p in range(num):
            entrada = self.Entrada(n)
            act = self.Act(w, entrada)
            y = self.Compara(act)
            respdesea = self.respuestaDeseada(condicion, entrada)
            entrena = self.Entrena(w, y, respdesea, entrada)
            w = entrena
            for i in range(len(entrada)-1):
                print entrada[i],
            print y, respdesea
        print w
        print "Capa 1", capa
        entrada = empty(0)
        act = 0
        y = 0
        respdesea = 0
        entrena = 0
        w = empty(0)
        condicion = empty(0)
        for f in range(ncapas):
            w = self.W(num)
            condicion = self.Condicion(num, w)
            print w
            print condicion
            entrada = self.Capa()
            for h in range(num):
                entrada = self.Entrada(num)
                act = self.Act(w, entrada)
                y = self.Compara(act)
                respdesea = self.respuestaDeseada(condicion, entrada)
                entrena = self.Entrena(w, y, respdesea, entrada)
                w = entrena
                for t in range(len(entrada)-1):
                    print entrada[i],
                print y, respdesea
            print w
            print "Capa",i , ":", capa
            

            
            
        

n = neu(int(argv[1]), int (argv[2]), int (argv[3]))



