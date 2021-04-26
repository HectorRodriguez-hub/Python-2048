from tkinter import *
import Logica2048 as h
import os
import Colores as c
#from Moreno_Ramirez_Rodriguez import arcade
#import tkinter as tk

## -------------------------------------------------------------------------
## Otra manera de escribir el cod
class interface:
    def __init__(self, ventana):
        self.ventana = ventana
        self.ventana.title("2048")
        #self.ventana.grid()
        self.cuadro_principal = Frame(self.ventana, bg ='red', width=600, height=600)
        self.cuadro_principal.grid(pady=(100, 0))
        self.make_GUI()
        self.game = h.arcade()
        self.play(4)
        self.ventana.mainloop()
        
    
    def make_GUI(self):
        
        # Celdas
        self.celdas = []
        for j in range(4):
            nuevo_dato = []
            for i in range(4):
                celda_marco = Frame(self.cuadro_principal, bg = '#C4C4C4', width = 150, height = 150)
                celda_marco.grid(row = i, column = j, padx = 5, pady = 5)
                celda_num = Label(self.cuadro_principal, bg = '#C4C4C4')
                celda_num.grid(row = i, column = j)
                celda_dato = {"cuadro": celda_marco, "numero": celda_num}
                nuevo_dato.append(celda_dato)
            self.celdas.append(nuevo_dato)
                
        # Puntaje
        puntaje_cuadro = Frame(self.ventana)
        puntaje_cuadro.place(relx = 0.5, y = 45, anchor = "center")
        Label(puntaje_cuadro, text = "Score", font = "black").grid(row = 0)
        self.puntaje_label = Label(puntaje_cuadro, text="0", font = 'black')
        self.puntaje_label.grid(row = 1)
    
    def update_GUI(self, M, score):
        for j in range(4):
            for i in range(4):
                value = M[i][j]
                if value == 0:
                    self.celdas[i][j]["cuadro"].configure(bg = "#c2b3a9")
                    self.celdas[i][j]["numero"].configure(bg = "#c2b3a9", text="")
                else:
                    self.celdas[i][j]["cuadro"].configure(bg = c.CELDA_COLORES[value])
                    self.celdas[i][j]["numero"].configure( bg = c.CELDA_COLORES[value],  fg = c.CELDA_NUM_COLORES[value], font = ("Helvetica", 40, "bold"), text = str(value))
        self.puntaje_label.configure(text = score) #Marcador
        #self.update_idletasks()
        
    def game_over(self, condicion):
        if condicion:
            game_over_cuadro = Frame(self.cuadro_principal, borderwidth=2)
            game_over_cuadro.place(relx=0.5, rely=0.5, anchor="center")
            Label( game_over_cuadro, text="You win!", bg="#ffcc00").pack()
        else:
            game_over_cuadro = Frame(self.main_grid, borderwidth=2)
            game_over_cuadro.place(relx=0.5, rely=0.5, anchor="center")
            Label( game_over_cuadro, text="Game over!", bg="#a39489").pack()
        
        
    def play(self, tam):
        #LLamado a funciones
        M = self.game.crear_Matriz(tam)
        self.game.start(M)
        print("Bienvenidos a 2048")

        #game
        while self.game.getGame():
            self.update_GUI(M,0)
            self.game.Print(M)
            tecla = input("Please type a key: ")
            entrada = tecla.lower()
            if entrada== 'w':
                self.game.arriba(M)
            if entrada== 'd':
                self.game.derecha(M)
            if entrada== 'a':
                self.game.izquierda(M)
            if entrada== 's':
                self.game.abajo(M)
            if entrada== 'n':
                self.game.setGame(False)
            self.game.aleatorio(M)
            os.system("cls")

'''

def crear_Matriz(tam):
    M = [[ 0 for j in range (tam)] for i  in range(tam) ]
    print("")
    return M

M = crear_Matriz(4)
M[1][1] = 2
M[1][3] = 2
M[0][0] = 2048
'''
root = Tk() #Se crea la raiz
game = interface(root)
