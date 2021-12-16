
ambiente= [1,0,1,0,0,0,1,1,0,1,0]

class arbol():
    def __init__(self):
        self.raiz = 0
        self.hijos=[]

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
    arbol = arbol()
    arbol.raiz=ambiente
    control=0
    control2=0
    for i in range(12):
        if pudePonerLinea(i, ambiente):
            arbol.hijos.append(arbol())
            arbol.hijos[control].raiz=ponerLinea(i, ambiente)
            for j in range(12):
                arbol.hijos[control].hijos.append(arbol())
                arbol.hijos[control].hijos[control2]
                control2 = control2 + 1
                if j == 11:
                    control2 = 0
            control = control + 1
    pass