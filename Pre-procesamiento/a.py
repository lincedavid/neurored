import sys

def abrirArchivo(nombre):
    archivo = open(nombre, 'r')
    lineas = archivo.readlines()
    for i in lineas:
        
        i = i.strip(' \t\n\r')
        i = list(i.split(',')) #Comvertimos en una lista y la imprimimos
    return i

archivo =  sys.argv[1]
print abrirArchivo(archivo)
