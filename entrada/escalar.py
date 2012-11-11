import sys

def abrirArchivo(nombre):
    archivo = open(nombre, 'r')
    lineas = archivo.readlines()
    for i in lineas:
        
        i = i.strip(' \t\n\r')
        i = list(i.split(',')) #Comvertimos en una lista y la imprimimos
    return i

def nomalizar(x, xmin, xmax):
    lower = -1.0
    first = (x - xmin)*2.0
    if(first == 0):
        return 0

    second = (xmax -xmin)
    third = first/second
    result = lower+third
    return result

def lista(list2):
    #list2 = [5.00, 74.0, 388.0, 123.0]                                                       
    #list2 = ['1926020', '1857670', '1798792', '1688540', '1636096','1533887', '1426044', '1425486', '1439480', '1423677', '1383676', '1360088', '1390745', '1435951', '1421990', '1392629','1318398']
    maximo = max(list2)
    minimo = min(list2)
    #minimo = 0
    a = list();
    for i in list2:
#        print nomalizar(float(i), float(minimo), float(maximo))
        a.append(nomalizar(float(i), float(minimo), float(maximo)))
    return a

def escalar(a):
    a = [1926020, 1857670, 1798792, 1688540, 1636096, 1533887, 1426044, 1425486, 1439480, 1423677, 1383676, 1360088, 1390745, 1435951, 1421990, 1392629, 1318398] #Esto hay que quitarlo

    b = list()
    minA = min(a)
    maxA = max(a)

    den = maxA - minA

    for i in a:
        num = i - minA
        r = float(num) / float(den)
        b.append(r)
    return b

archivo =  sys.argv[1]
listA = abrirArchivo(archivo)
#print listA
#print lista(listA) #Esta es cuando queremos normalizar con -1 y 1
print escalar(listA) #Este es para sacar de 0 a 1
#print lista()
