import tkinter as tk
from tkinter import *
from tkinter import ttk
from functools import partial
import numpy as np
import minmax as algoritmos

class Tabla(tk.Frame):

    def __init__(self, master=None):
        super().__init__(master)
        self.master = master

        self.inicializar_gui()
    
    def inicializar_gui(self):

        #imagenboton=PhotoImage(file="boton.png")
        
        #------------------------------- fila 1 de botones----------------------------------------------------------
        celda0 = tk.Frame(master=self.master, relief=tk.RAISED, borderwidth=2)
        celda0.grid(row=0, column=1)
        #Botones Para esta madre 
        self.Boton0=tk.Button(master=celda0, text="0",command = partial(self.Marcar, "b0"),font=("times new roman", 15), bg="dimgrey",fg="cornsilk2",bd=0,cursor="hand2", width=10, height=1)
        self.Boton0.pack()
    
        celda4 = tk.Frame(master=self.master, relief=tk.RAISED, borderwidth=2)
        celda4.grid(row=0, column=3)
        self.Boton4=tk.Button(master=celda4, text="4",command = partial(self.Marcar, "b4"),font=("times new roman", 15), bg="dimgrey",fg="cornsilk2",bd=0,cursor="hand2",width=10, height=1)
        self.Boton4.pack()

        #------------------------------- fila 2 de botones----------------------------------------------------------
        celda3 = tk.Frame(master=self.master, relief=tk.RAISED, borderwidth=2)
        celda3.grid(row=3, column=1)
        self.Boton3=tk.Button(master=celda3, text="3",command=partial(self.Marcar, "b3"),font=("times new roman", 15), bg="dimgrey",fg="cornsilk2",bd=0,cursor="hand2",width=10, height=1)
        self.Boton3.pack()

        celda6 = tk.Frame(master=self.master, relief=tk.RAISED, borderwidth=2)
        celda6.grid(row=3, column=3)
        self.Boton6=tk.Button(master=celda6, text="6",command=partial(self.Marcar, "b6"),font=("times new roman", 15), bg="dimgrey",fg="cornsilk2",bd=0,cursor="hand2",width=10, height=1)
        self.Boton6.pack()

        #------------------------------- fila 3 de botones----------------------------------------------------------

        celda11 = tk.Frame(master=self.master, relief=tk.RAISED, borderwidth=2)
        celda11.grid(row=5, column=1)
        self.Boton11=tk.Button(master=celda11, text="11",command=partial(self.Marcar, "b11"),font=("times new roman", 14), bg="dimgrey",fg="cornsilk2",bd=0,cursor="hand2",width=10, height=1)
        self.Boton11.pack()

        celda8 = tk.Frame(master=self.master, relief=tk.RAISED, borderwidth=2)
        celda8.grid(row=5, column=3)
        self.Boton8=tk.Button(master=celda8, text="8",command=partial(self.Marcar, "b8"),font=("times new roman", 15), bg="dimgrey",fg="cornsilk2",bd=0,cursor="hand2",width=10, height=1)
        self.Boton8.pack()

        #------------------------------- columna 1 de botones----------------------------------------------------------

        celda1 = tk.Frame(master=self.master, relief=tk.RAISED, borderwidth=2)
        celda1.grid(row=2, column=0)
        self.Boton1=tk.Button(master=celda1, text="1",command=partial(self.Marcar, "b1"),font=("times new roman", 15), bg="dimgrey",fg="cornsilk2",bd=0,cursor="hand2",width=2, height=5)
        self.Boton1.pack()

        celda10 = tk.Frame(master=self.master, relief=tk.RAISED, borderwidth=2)
        celda10.grid(row=4, column=0)
        self.Boton10=tk.Button(master=celda10, text="10",command=partial(self.Marcar, "b10"),font=("times new roman", 15), bg="dimgrey",fg="cornsilk2",bd=0,cursor="hand2",width=2, height=5)
        self.Boton10.pack()

        #------------------------------- columna 2 de botones----------------------------------------------------------

        celda2 = tk.Frame(master=self.master, relief=tk.RAISED, borderwidth=2)
        celda2.grid(row=2, column=2)
        self.Boton2=tk.Button(master=celda2, text="2",command=partial(self.Marcar, "b2"),font=("times new roman", 15), bg="dimgrey",fg="cornsilk2",bd=0,cursor="hand2",width=2, height=5)
        self.Boton2.pack()

        celda9 = tk.Frame(master=self.master, relief=tk.RAISED, borderwidth=2)
        celda9.grid(row=4, column=2)
        self.Boton9=tk.Button(master=celda9, text="9",command=partial(self.Marcar, "b9"),font=("times new roman", 15), bg="dimgrey",fg="cornsilk2",bd=0,cursor="hand2",width=2, height=5)
        self.Boton9.pack()

        #------------------------------- columna 3 de botones----------------------------------------------------------

        celda5 = tk.Frame(master=self.master, relief=tk.RAISED, borderwidth=2)
        celda5.grid(row=2, column=4)
        self.Boton5=tk.Button(master=celda5, text="5",command=partial(self.Marcar, "b5"),font=("times new roman", 15), bg="dimgrey",fg="cornsilk2",bd=0,cursor="hand2",width=2, height=5)
        self.Boton5.pack()

        celda7 = tk.Frame(master=self.master, relief=tk.RAISED, borderwidth=2)
        celda7.grid(row=4, column=4)
        self.Boton7=tk.Button(master=celda7, text="7",command=partial(self.Marcar, "b7"),font=("times new roman", 15), bg="dimgrey",fg="cornsilk2",bd=0,cursor="hand2",width=2, height=5)
        self.Boton7.pack()

        #-------------------------------------------- puntos ------------------------------------------------------
        celda0 = tk.Frame(master=self.master, relief=tk.RAISED, borderwidth=2)
        celda0.grid(row=0, column=0)
        label0=tk.Label(master=celda0, text=" ",font=("times new roman", 3),bg="black",fg="black",bd=10)
        label0.pack()

        celda1 = tk.Frame(master=self.master, relief=tk.RAISED, borderwidth=2)
        celda1.grid(row=0, column=2)
        label1=tk.Label(master=celda1, text=" ",font=("times new roman", 3),bg="black",fg="black",bd=10)
        label1.pack()

        celda2 = tk.Frame(master=self.master, relief=tk.RAISED, borderwidth=2)
        celda2.grid(row=0, column=4)
        label2=tk.Label(master=celda2, text=" ",font=("times new roman", 3),bg="black",fg="black",bd=10)
        label2.pack()
        
        celda3 = tk.Frame(master=self.master, relief=tk.RAISED, borderwidth=2)
        celda3.grid(row=3, column=0)
        label3=tk.Label(master=celda3, text=" ",font=("times new roman", 3),bg="black",fg="black",bd=10)
        label3.pack()

        celda4 = tk.Frame(master=self.master, relief=tk.RAISED, borderwidth=2)
        celda4.grid(row=3, column=2)
        label4=tk.Label(master=celda4, text=" ",font=("times new roman", 3),bg="black",fg="black",bd=10)
        label4.pack()

        celda5 = tk.Frame(master=self.master, relief=tk.RAISED, borderwidth=2)
        celda5.grid(row=3, column=4)
        label5=tk.Label(master=celda5, text=" ",font=("times new roman", 3),bg="black",fg="black",bd=10)
        label5.pack()

        celda6 = tk.Frame(master=self.master, relief=tk.RAISED, borderwidth=2)
        celda6.grid(row=5, column=0)
        label6=tk.Label(master=celda6, text=" ",font=("times new roman", 3),bg="black",fg="black",bd=10)
        label6.pack()

        celda7 = tk.Frame(master=self.master, relief=tk.RAISED, borderwidth=2)
        celda7.grid(row=5, column=2)
        label7=tk.Label(master=celda7, text=" ",font=("times new roman", 3),bg="black",fg="black",bd=10)
        label7.pack()

        celda8 = tk.Frame(master=self.master, relief=tk.RAISED, borderwidth=2)
        celda8.grid(row=5, column=4)
        label8=tk.Label(master=celda8, text=" ",font=("times new roman", 3),bg="black",fg="black",bd=10)
        label8.pack()

    turno=0
    puntajeJ=0
    puntajeM=0
    estado_tablero= np.zeros(12)
    estado_cuadros= np.zeros(4)

    def actualizar_tablero(self,posicion):
        valor=1
        self.estado_tablero[posicion]=valor
    
    def es_un_cuadrado(self):
        valor=1
        if self.turno % 2 == 0:
                if ((self.estado_tablero[0] == self.estado_tablero[1] and self.estado_tablero[0] == self.estado_tablero[2] and self.estado_tablero[0] == self.estado_tablero[3] and self.estado_tablero[0] != 0) and self.estado_cuadros[0]==0):
                    self.puntajeJ+=1
                    self.estado_cuadros[0]=valor
                    celda0 = tk.Frame(master=self.master, relief=tk.RAISED, borderwidth=2)
                    celda0.grid(row=2, column=1)
                    label0=tk.Label(master=celda0, text="A",font=("times new roman", 50),bg="blue",fg="black",bd=20)
                    label0.pack()
                elif ((self.estado_tablero[2] == self.estado_tablero[4] and self.estado_tablero[2] == self.estado_tablero[5] and self.estado_tablero[2] == self.estado_tablero[6] and self.estado_tablero[2] != 0) and self.estado_cuadros[1]==0):
                    self.puntajeJ+=1
                    self.estado_cuadros[1]=valor
                    celda0 = tk.Frame(master=self.master, relief=tk.RAISED, borderwidth=2)
                    celda0.grid(row=2, column=3)
                    label0=tk.Label(master=celda0, text="X",font=("times new roman", 50),bg="blue",fg="black",bd=20)
                    label0.pack()
                elif ((self.estado_tablero[3] == self.estado_tablero[9] and self.estado_tablero[3] == self.estado_tablero[10] and self.estado_tablero[3] == self.estado_tablero[11] and self.estado_tablero[3] != 0) and self.estado_cuadros[2]==0):
                    self.puntajeJ+=1
                    self.estado_cuadros[2]=valor
                    celda0 = tk.Frame(master=self.master, relief=tk.RAISED, borderwidth=2)
                    celda0.grid(row=4, column=1)
                    label0=tk.Label(master=celda0, text="D",font=("times new roman", 50),bg="blue",fg="black",bd=20)
                    label0.pack()
                elif ((self.estado_tablero[6] == self.estado_tablero[7] and self.estado_tablero[6] == self.estado_tablero[8] and self.estado_tablero[6] == self.estado_tablero[9] and self.estado_tablero[6] != 0) and self.estado_cuadros[3]==0):
                    self.puntajeJ+=1
                    self.estado_cuadros[3]=valor
                    celda0 = tk.Frame(master=self.master, relief=tk.RAISED, borderwidth=2)
                    celda0.grid(row=4, column=3)
                    label0=tk.Label(master=celda0, text="F",font=("times new roman", 50),bg="blue",fg="black",bd=20)
                    label0.pack()
        else:
            
            if ((self.estado_tablero[0] == self.estado_tablero[1] and self.estado_tablero[0] == self.estado_tablero[2] and self.estado_tablero[0] == self.estado_tablero[3] and self.estado_tablero[0] != 0) and self.estado_cuadros[0]==0):
                self.puntajeM+=1
                self.estado_cuadros[0]=valor
                celda0 = tk.Frame(master=self.master, relief=tk.RAISED, borderwidth=2)
                celda0.grid(row=2, column=1)
                label0=tk.Label(master=celda0, text="B",font=("times new roman", 50),bg="red",fg="black",bd=20)
                label0.pack()
            elif ((self.estado_tablero[2] == self.estado_tablero[4] and self.estado_tablero[2] == self.estado_tablero[5] and self.estado_tablero[2] == self.estado_tablero[6] and self.estado_tablero[2] != 0) and self.estado_cuadros[1]==0):
                self.puntajeM+=1
                self.estado_cuadros[1]=valor
                celda0 = tk.Frame(master=self.master, relief=tk.RAISED, borderwidth=2)
                celda0.grid(row=2, column=3)
                label0=tk.Label(master=celda0, text="M",font=("times new roman", 50),bg="red",fg="black",bd=20)
                label0.pack()
            elif ((self.estado_tablero[3] == self.estado_tablero[9] and self.estado_tablero[3] == self.estado_tablero[10] and self.estado_tablero[3] == self.estado_tablero[11] and self.estado_tablero[3] != 0) and self.estado_cuadros[2]==0):
                self.puntajeM+=1
                self.estado_cuadros[2]=valor
                celda0 = tk.Frame(master=self.master, relief=tk.RAISED, borderwidth=2)
                celda0.grid(row=4, column=1)
                label0=tk.Label(master=celda0, text="N",font=("times new roman", 50),bg="red",fg="black",bd=20)
                label0.pack()
            elif ((self.estado_tablero[6] == self.estado_tablero[7] and self.estado_tablero[6] == self.estado_tablero[8] and self.estado_tablero[6] == self.estado_tablero[9] and self.estado_tablero[6] != 0) and self.estado_cuadros[3]==0):
                self.puntajeM+=1
                self.estado_cuadros[3]=valor
                celda0 = tk.Frame(master=self.master, relief=tk.RAISED, borderwidth=2)
                celda0.grid(row=4, column=3)
                label0=tk.Label(master=celda0, text="O",font=("times new roman", 50),bg="red",fg="black",bd=20)
                label0.pack()

    
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
    
    def esta_ocupado_cuadro(self):
        ocupada = True
        if self.estado_cuadros[0] == 0:
            ocupada = False
        elif self.estado_cuadros[1] == 0:
            ocupada = False
        elif self.estado_cuadros[2] == 0:
            ocupada = False
        elif self.estado_cuadros[3] == 0:
            ocupada = False
        

        print(ocupada)
        return ocupada
    
    def ganador(self):
        if (self.estado_tablero == 1).all() or (self.estado_cuadros == 1).all():
            text=""
            puntaje=0
            if self.puntajeJ > self.puntajeM:
                text = 'Ganador: Jugador '
                puntaje=self.puntajeJ
            elif self.puntajeM > self.puntajeJ:
                text = 'Ganador: Maquina '
                puntaje=self.puntajeM
            else:
                text = 'Empate: '
                puntaje=self.puntajeJ
            texto=text+str(puntaje)
            
            celda0 = tk.Frame(master=self.master, relief=tk.RAISED, borderwidth=2)
            celda0.grid(row=0, column=0)
            label0=tk.Label(master=celda0, text=texto,font=("times new roman", 20),bg="gray",fg="black",bd=10,width=22,height=12)
            label0.pack()

    def Marcar(self,b):
        

        if (b == "b0"):
            if self.turno % 2 == 0:
                self.Boton0['state']='disabled'
                self.Boton0['bg']='blue'
                
                self.actualizar_tablero(0)
                self.es_un_cuadrado()
                
            else:
                self.Boton0['state']='disabled'
                self.Boton0['bg']='red'
                
                self.actualizar_tablero(0)
                self.es_un_cuadrado()
                
        if (b=="b1"):
            if self.turno % 2 == 0:
                self.Boton1['state']='disabled'
                self.Boton1['bg']='blue'
                
                self.actualizar_tablero(1)
                self.es_un_cuadrado()
                
            else:
                self.Boton1['state']='disabled'
                self.Boton1['bg']='red'
                
                self.actualizar_tablero(1)
                self.es_un_cuadrado()
                
        if (b=="b2"):
            if self.turno % 2 == 0:
                self.Boton2['state']='disabled'
                self.Boton2['bg']='blue'
                
                self.actualizar_tablero(2)
                self.es_un_cuadrado()
                
            else:
                self.Boton2['state']='disabled'
                self.Boton2['bg']='red'
                self.es_un_cuadrado()
                self.actualizar_tablero(2)
                
                
        if (b=="b3"):
            if self.turno % 2 == 0:
                self.Boton3['state']='disabled'
                self.Boton3['bg']='blue'
                
                self.actualizar_tablero(3)
                self.es_un_cuadrado()
                
            else:
                self.Boton3['state']='disabled'
                self.Boton3['bg']='red'
                
                self.actualizar_tablero(3)
                self.es_un_cuadrado()
                
        if (b=="b4"):
            if self.turno % 2 == 0:
                self.Boton4['state']='disabled'
                self.Boton4['bg']='blue'
                
                self.actualizar_tablero(4)
                self.es_un_cuadrado()
                
            else:
                self.Boton4['state']='disabled'
                self.Boton4['bg']='red'
                
                self.actualizar_tablero(4)
                self.es_un_cuadrado()
                
        if (b=="b5"):
            if self.turno % 2 == 0:
                self.Boton5['state']='disabled'
                self.Boton5['bg']='blue'
                
                self.actualizar_tablero(5)
                self.es_un_cuadrado()
                
            else:
                self.Boton5['state']='disabled'
                self.Boton5['bg']='red'
                self.es_un_cuadrado()
                self.actualizar_tablero(5)
                
                
        if (b=="b6"):
            if self.turno % 2 == 0:
                self.Boton6['state']='disabled'
                self.Boton6['bg']='blue'
                self.es_un_cuadrado()
                self.actualizar_tablero(6)
                
                
            else:
                self.Boton6['state']='disabled'
                self.Boton6['bg']='red'
                self.es_un_cuadrado()
                self.actualizar_tablero(6)
                
                
        if (b=="b7"):
            if self.turno % 2 == 0:
                self.Boton7['state']='disabled'
                self.Boton7['bg']='blue'
                self.es_un_cuadrado()
                self.actualizar_tablero(7)
                
                
            else:
                self.Boton7['state']='disabled'
                self.Boton7['bg']='red'
                self.es_un_cuadrado()
                self.actualizar_tablero(7)
                
                
        if (b=="b8"):
            if self.turno % 2 == 0:
                self.Boton8['state']='disabled'
                self.Boton8['bg']='blue'
                self.es_un_cuadrado()
                self.actualizar_tablero(8)
                
                
            else:
                self.Boton8['state']='disabled'
                self.Boton8['bg']='red'
                self.es_un_cuadrado()
                self.actualizar_tablero(8)
                
                
        if (b=="b9"):
            if self.turno % 2 == 0:
                self.Boton9['state']='disabled'
                self.Boton9['bg']='blue'
                self.es_un_cuadrado()
                self.actualizar_tablero(9)
                
                   
            else:
                self.Boton9['state']='disabled'
                self.Boton9['bg']='red'
                self.es_un_cuadrado()
                self.actualizar_tablero(9)
                
                
        if (b=="b10"):
            if self.turno % 2 == 0:
                self.Boton10['state']='disabled'
                self.Boton10['bg']='blue'
                self.es_un_cuadrado()
                self.actualizar_tablero(10)
                
                
            else:
                self.Boton10['state']='disabled'
                self.Boton10['bg']='red'
                self.es_un_cuadrado()
                self.actualizar_tablero(10)
                
                
        if (b=="b11"):
            if self.turno % 2 == 0:
                self.Boton11['state']='disabled'
                self.Boton11['bg']='blue'
                self.es_un_cuadrado()
                self.actualizar_tablero(11)
                
                
            else:
                self.Boton11['state']='disabled'
                self.Boton11['bg']='red'
                
                self.actualizar_tablero(11)
                self.es_un_cuadrado()
        
        print((self.estado_tablero[0] == self.estado_tablero[1] and self.estado_tablero[0] == self.estado_tablero[2] and self.estado_tablero[0] == self.estado_tablero[3] and self.estado_tablero[0] != 0))
        print((self.estado_tablero[2] == self.estado_tablero[4] and self.estado_tablero[2] == self.estado_tablero[5] and self.estado_tablero[2] == self.estado_tablero[6] and self.estado_tablero[2] != 0))
        self.turno+=1
        self.ganador()
        print(self.estado_tablero)
        print(self.estado_cuadros)
        print(self.puntajeJ)
        print(self.puntajeM)

def main():
    app = tk.Tk()
    app.title('Organización Tabla')
    app.geometry('340x370')
    app.resizable(0,0)
    ventana = Tabla(app)
    ventana.mainloop()

if __name__ == "__main__":
    main()