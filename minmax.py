import copy
import numpy as np
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
        lista.append(arbol.hijos[Nnodo].hijos[i].raiz)
    return lista







def ponerLinea(N,ambiente):
    ambientecopia = list(ambiente)
    ambientecopia[N]=1
    return ambientecopia

def llenarArbol(ambiente):
    arvol = arbol()
    arvol.raiz = ambiente
    arbolaux = arbol()
    arbolaux2 = arbol()
    for i in range(12):
        if pudePonerLinea(i, ambiente):
            arbolaux.raiz = ponerLinea(i, ambiente)
            for j in range(12):
                if pudePonerLinea(j, arbolaux.raiz):
                    arbolaux2.raiz = ponerLinea(j, arbolaux.raiz)
                    arbolaux.hijos.append(arbolaux2)
                arbolaux2 = arbol()
            arvol.hijos.append(arbolaux)
            arbolaux = arbol()
    return arvol

def imprimirArbol(arbol):
    print(arbol.raiz)
    for p in range(contadorDeCeros(arbol.raiz)):
        print(contadorDeCeros(arbol.raiz))
        print('Hijo'+ str(p) +'-------------------------------')
        print(arbol.hijos[p].raiz)
        for q in range(contadorDeCeros(arbol.hijos[p].raiz)):
            print(contadorDeCeros(arbol.hijos[p].raiz))
            print('Hoja' + str(q) + '-------------------------------')
            print(arbol.hijos[p].hijos[q].raiz)

def listadoHojasPorNodo1(arbol, Nnodo):
    for p in range(contadorDeCeros(arbol.raiz)):
        for q in range(contadorDeCeros(arbol.hijos[p].raiz)):
            arbol.hijos[p].hijos[q].raiz



def llenarArbol1(ambiente):
    arvol = arbol()
    arvol.raiz=ambiente
    control=0
    control2=0
    for i in range(12):
        if pudePonerLinea(i, ambiente):
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
    return arvol

def valorHoja(ambiente):
    cuadrosPosibleaux = cuadrosNoExistentes(ambiente)    # ---->  [[1,2,4,5,],[6,7,8,9],[4,6,2,5]]
    auxvalorAmbiente=[]
    for i in cuadrosPosibleaux:
        valorAux = numeroDeCoincidencias(ambiente, i)
        if valorAux== 0:
            auxvalorAmbiente.append(1)
        if valorAux== 1:
            auxvalorAmbiente.append(1)
        if valorAux== 2:
            auxvalorAmbiente.append(2)
        if valorAux== 3:
            auxvalorAmbiente.append(4)
        if valorAux== 4:
            auxvalorAmbiente.append(-1)
    return sum(auxvalorAmbiente)

#herisyuca 
def obtenerListaPuntajesdeHojas(listaHojas):
    listavaloresdeHojas=[]
    for i in listaHojas:
        puntajeAux=valorHoja(i)
        listavaloresdeHojas.append(puntajeAux)
    return listavaloresdeHojas

def minimax(ambiente):
    arvol = llenarArbol(ambiente)
    numeroDeHijos_aux = contadorDeCeros(ambiente)
    listaDePuntajeN1 = []
    for i in range(numeroDeHijos_aux):
        listaNodos_aux = listadoHojasPorNodo(arvol,i)
        listaPuntaje_aux = obtenerListaPuntajesdeHojas(listaNodos_aux)
        #print(listaNodos_aux)
        #print(listaPuntaje_aux)
        puntajeAux= min(listaPuntaje_aux)
        listaDePuntajeN1.append(puntajeAux)
    puntajeDefinitivo=max(listaDePuntajeN1)
    posicion = 0
    for j in range(len(listaDePuntajeN1)):
        if listaDePuntajeN1[j] == puntajeDefinitivo:
            posicion = j
            break
    return arvol.hijos[posicion].raiz




#ambiente3 = [1,1,1,1,0,0,1,0,1,0,1,0]
#arvol = llenarArbol(ambiente3)
#imprimirArbol(arvol)
#minimax(ambiente3)
#listaHojas=listadoHojasPorNodo(arvol, 1)
#print(listaHojas)

#print(obtenerListaPuntajesdeHojas(listaHojas))

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