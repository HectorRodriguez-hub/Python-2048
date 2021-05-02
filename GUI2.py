## =========================================================================
## Autores :
## Camilo Andres Moreno Colorado
## Aldemar Yamid Ramirez Avila
## Héctor René Rodríguez Hernández 
## =========================================================================

from tkinter import *
import Logica2048 as h
import os
import Colores as c

## -------------------------------------------------------------------------
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
            Label( game_over_cuadro, text="You win!", bg="#ffcc00", font =("Helvetica", 48, "bold")).pack()
        else:
            game_over_cuadro = Frame(self.cuadro_principal, borderwidth=2)
            game_over_cuadro.place(relx=0.5, rely=0.5, anchor="center")
            Label( game_over_cuadro, text="Game over!", bg="#a39489", font =("Helvetica", 48, "bold") ).pack()
        
        
    def play(self, tam):
        #LLamado a funciones
        M = self.game.crear_Matriz(tam)
        self.game.start(M)
        print("Bienvenidos a 2048")
        aux = [self.game.copia(M), 0]
        game_over = True
        #game
        self.update_GUI(M,0)
        self.game.Print(M)
        while game_over:
            tecla = input("Please type a key: ")
            entrada = tecla.lower()
            if entrada == 'w' or entrada == 'd' or entrada == 'a' or entrada == 's' or entrada == 'n':
                M = self.game.copia(aux[0])
                C = self.game.copia(aux[0])
                ale = False
                if entrada== 'w':
                    aux = self.game.arriba(aux[0], aux[1])
                    ale = self.game.iguales(C,aux[0])
                if entrada== 'd':
                    aux = self.game.derecha(aux[0], aux[1])
                    ale = self.game.iguales(C,aux[0])
                if entrada== 'a':
                    aux = self.game.izquierda(aux[0], aux[1])
                    ale = self.game.iguales(C,aux[0])
                if entrada== 's':
                    aux = self.game.abajo(aux[0], aux[1])
                    ale = self.game.iguales(C,aux[0])
                if entrada== 'n':
                    game_over = False
                if not ale:
                    self.game.aleatorio(aux[0])
                game_over = self.game.opcional(aux[0])
                if any(2048 in row for row in aux[0]):
                    self.game_over(game_over)
                    game_over = False
                elif not game_over:
                    self.game_over(game_over)
                print(aux[1])
                self.update_GUI(aux[0], aux[1])
                self.game.Print(aux[0])
                os.system("cls")
        

## -------------------------------------------------------------------------
## ---------------------------------- MAIN ---------------------------------
## -------------------------------------------------------------------------

root = Tk() #Se crea la raiz
game = interface(root)
