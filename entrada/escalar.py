import sys

def abrirArchivo(nombre):
    archivo = open(nombre, 'r')
    lineas = archivo.readlines()
    for i in lineas:
        
        i = i.strip(' \t\n\r')
        i = list(i.split(',')) #Comvertimos en una lista y la imprimimos
    return i

def escalar(a):
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
	
    #print escalar(listA)
    print str(escalar(listA)).strip('[]') #lista pura
    #print ', '.join(escalar(listA))

main()
