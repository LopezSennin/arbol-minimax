import copy
ambiente= [1,1,1,1,0,0,1,1,1,1,0,0]

class arbol():
    def __init__(self):
        self.raiz = 0
        self.hijos=[]

    def __str__(self):
        return [self.raiz, self.hijos]

    def raiz(self):
        return self.raiz

    def retornarNhijo(self, N):
        return self.hijos[N-1]

def pudePonerLinea(N,ambiente):
    if ambiente[N]==0:
        return True
    else: 
        return False

def contadorDeCeros(ambiente):
    contador = 0
    for i in range(len(ambiente)):
        if ambiente[i]==0:
            contador = contador + 1
    return contador

def cuadrosExistenetes(ambiente):
    cuadros = []
    cuadro1 = [0,1,2,3]
    cuadro2 = [2,4,5,6]
    cuadro3 = [3,9,10,11]
    cuadro4 = [6,7,8,9]
    contador = 0
    for i in cuadro1:
        if ambiente[i] == 1:
            contador = contador + 1
            if contador == 4:
                cuadros.append(cuadro1)
    contador = 0
    
    for i in cuadro2:
        if ambiente[i] == 1:
            contador = contador + 1
            if contador == 4:
                cuadros.append(cuadro2)
    contador = 0

    for i in cuadro3:
        if ambiente[i] == 1:
            contador = contador + 1
            if contador == 4:
                cuadros.append(cuadro3)
    contador = 0

    for i in cuadro4:
        if ambiente[i] == 1:
            contador = contador + 1
            if contador == 4:
                cuadros.append(cuadro4)
    contador = 0
    return cuadros


def cuadrosNoExistentes(ambiente):
    cuadros = []
    cuadro1 = [0,1,2,3]
    cuadro2 = [2,4,5,6]
    cuadro3 = [3,9,10,11]
    cuadro4 = [6,7,8,9]
    contador = 0
    contador2 = 0
    for i in cuadro1:
        contador2 = contador2 + 1
        if ambiente[i] == 1:
            contador = contador + 1
        if contador2 == 4:
            if contador != 4:
                cuadros.append(cuadro1)
                contador2 = 0
    contador = 0
    contador2 = 0
    for i in cuadro2:
        contador2 = contador2 + 1
        if ambiente[i] == 1:
            contador = contador + 1
        if contador2 == 4:
            if contador != 4:
                cuadros.append(cuadro2)
                contador2 = 0
    contador = 0
    contador2 = 0
    for i in cuadro3:
        contador2 = contador2 + 1
        if ambiente[i] == 1:
            contador = contador + 1
        if contador2 == 4:
            if contador != 4:
                cuadros.append(cuadro3)
                contador2 = 0
    contador = 0
    contador2 = 0
    for i in cuadro4:
        contador2 = contador2 + 1
        if ambiente[i] == 1:
            contador = contador + 1
        if contador2 == 4:
            if contador != 4:
                cuadros.append(cuadro4)
                contador2 = 0
    contador = 0
    contador2 = 0
    return cuadros


def numeroDeCoincidencias(ambiente, cuadro):
    contador = 0
    for i in cuadro:
        if ambiente[i] == 1:
            contador = contador + 1
    return contador


def listadoHojasPorNodo(arbol, Nnodo):
    lista = []
    for i in range(contadorDeCeros(arbol.raiz)-1):
        lista.append(arbol.hijos[Nnodo].hijos[i])
    return lista



#prueba numeroDeCoincidencias(ambiente, cuadro2)
#cuadro2 = [2,4,5,6]
#print(numeroDeCoincidencias(ambiente, cuadro2))

#Prueba cuadrosNoExistentes(ambiente)
#print(ambiente)
#print(cuadrosExistenetes(ambiente))
#print('-----------------------------')
#print(cuadrosNoExistentes(ambiente))



def ponerLinea(N,ambiente):
    ambientecopia = list(ambiente)
    ambientecopia[N]=1
    return ambientecopia

def llenarArbol(ambiente):
    arvol = arbol()
    arvol.raiz=ambiente
    control=0
    control2=0
    for i in range(12):
        if pudePonerLinea(i, ambiente):
            #print(i)

            arvol.hijos.append(arbol())
            arvol.hijos[control].raiz=ponerLinea(i, ambiente)
            for j in range(12):
                if pudePonerLinea(j, arvol.hijos[control].raiz):
                    arvol.hijos[control].hijos.append(arbol())

                    arvol.hijos[control].hijos[control2]=ponerLinea(j,arvol.hijos[control].raiz) # falta
                    control2 = control2 + 1
                    if j == 11:
                        control2 = 0
            control = control + 1
    '''print(ambiente)
    print(arvol.hijos[0].raiz)
    print(arvol.hijos[1].raiz)
    print(arvol.hijos[2].raiz)
    print(arvol.hijos[3].raiz)
    print(arvol.hijos[4].raiz)
    print(arvol.hijos[5].raiz)
    print(arvol.hijos[6].raiz)
    print(arvol.hijos[7].raiz)
    print(arvol.hijos[8].raiz)
    print(arvol.hijos[9].raiz)
    print(arvol.hijos[10].raiz)

    print("---------------------")

    print(arvol.hijos[1].hijos[0])
    print(arvol.hijos[1].hijos[1])
    print(arvol.hijos[1].hijos[2])
    print(arvol.hijos[1].hijos[3])
    print(arvol.hijos[1].hijos[4])
    print(arvol.hijos[1].hijos[5])
    print(arvol.hijos[0].hijos[6])
    print(arvol.hijos[0].hijos[7])
    print(arvol.hijos[0].hijos[8])
    print(arvol.hijos[0].hijos[9])
    '''



    
    
    return arvol

print(ambiente)
arvol = llenarArbol(ambiente)

print(listadoHojasPorNodo(arvol, 1))


'''
ambiente2=list(ambiente)
ambiente2[2]=5

arvol=arbol()
arvol.raiz=list(ambiente)
arvol.hijos.append(arbol())
arvol.hijos[0].raiz=ambiente2
arvol.hijos[0].hijos.append(arbol())
arvol.hijos[0].hijos[0].raiz=ambiente

arbol2 = copy.deepcopy(arvol)
arvol.hijos[0].hijos[0].raiz=ambiente2
print(arbol2.hijos[0].hijos[0].raiz)
print(arvol.hijos[0].hijos[0].raiz)
'''