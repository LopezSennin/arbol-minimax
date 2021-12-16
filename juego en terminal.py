import copy
ambiente= [1,0,1,0,0,0,1,1,0,1,0,1]

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

def ponerLinea(N,ambiente):
    ambientecopia = list(ambiente)
    ambientecopia[N]=1
    return ambientecopia

def llenarArbol(ambiente):
    arvol = arbol()
    arvol.raiz=ambiente
    arbolAux = arbol()
    control=0
    control2=0
    for i in range(12):
        if pudePonerLinea(i, ambiente):
            ambienteaux = ponerLinea(i, ambiente)
            arbolAux.raiz = ambienteaux
            for j in range(11):
                if pudePonerLinea(j, ambienteaux):
                    arbolAux.hijos.append(ponerLinea(j,ambienteaux))
                    
            arvol.hijos.append(arbolAux)
            arbolAux = arbol()
    return arvol

llenarArbol(ambiente)

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