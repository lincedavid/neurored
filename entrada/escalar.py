import sys

def abrirArchivo(nombre):
    archivo = open(nombre, 'r')
    lineas = archivo.readlines()
    for i in lineas:
        
        i = i.strip(' \t\n\r')
        i = list(i.split(',')) #Comvertimos en una lista y la imprimimos
    return i

def escalar(a):
    #a = [41,39,50,40,43,38,44,35,39,35,29,49,50,59,63,32,39,47,53,60,57,52,70,90,74,62,55,84,94,70,108,139,120,97,126,149,158,124,140,109,114,77,120,133,110,92,97,78,99,107,112,90,98,125,155,190,236,189,174,178,136,161,171,149,184,155,276,224,213,279,268,287,238,213,257,293,212,246,353,339,308,247,257,322,298,273,312,249,286,279,309,401,309,328,353,354,327,324,285,243,241,287,355,460,364,487,452,391,500,451,375,372,302,316,398,394,431,431]
    #a = [2, 4, 5]
    b = list()
    minA = min(a)
    maxA = max(a)

    den = maxA - minA

    for i in a:
        num = i - minA
        r = float(num) / float(den)
        b.append(r)
    return b

def main():
    listA = abrirArchivo(sys.argv[1]) #Obtenemos la direccion del archivo a escalar
    listA = [int(i) for i in listA]
    #listA = ['a']	
    #print escalar(listA)
    print str(escalar(listA)).strip('[]') #lista pura
    #print ','.join(escalar(listA))

main()
