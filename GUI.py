# from tkinter import *
import tkinter as tk

## -------------------------------------------------------------------------
## Variables globales
## -------------------------------------------------------------------------
CELL_COLORS = {
    2: "#fcefe6",
    4: "#f2e8cb",
    8: "#f5b682",
    16: "#f29446",
    32: "#ff775c",
    64: "#e64c2e",
    128: "#ede291",
    256: "#fce130",
    512: "#ffdb4a",
    1024: "#f0b922",
    2048: "#fad74d"
}

CELL_NUMBER_COLORS = {
    2: "#695c57",
    4: "#695c57",
    8: "#ffffff",
    16: "#ffffff",
    32: "#ffffff",
    64: "#ffffff",
    128: "#ffffff",
    256: "#ffffff",
    512: "#ffffff",
    1024: "#ffffff",
    2048: "#ffffff"
}


## -------------------------------------------------------------------------

class interface(tk.Frame):
    def __init__(self):
        #inicialización de la ventana
        #self.ventana = ventana
        
        tk.Frame.__init__(self)
        self.grid()
        #self.grid()
        self.master.title("2048")
        
        self.main_grid = tk.Frame(self, bg ='red', width=600, height=600)
        self.main_grid.grid(pady=(100, 0))
        self.make_GUI()
        self.mainloop()
        
        '''
        self.ventana.title("2048") #Titulo a la venta
        self.ventana.geometry("600x600") #darle tamaño a la ventana 
        self.ventana.resizable(1,1) #Desactivar que se pueda redimensionar 
        #self.ventana.iconbitmap() #Icono de ventana - formato ico, xbm (linux)
        self.ventana.config(bg='#808080')
        '''
        
    
    def make_GUI(self):
        
        # Celdas
        self.cells = []
        for i in range(4):
            row = []
            for j in range(4):
                cell_frame = tk.Frame(self.main_grid, bg = "#c2b3a9", width = 150, height = 150)
                cell_frame.grid(row = i, column = j, padx = 5, pady = 5)
                cell_number = tk.Label(self.main_grid, bg = "#c2b3a9")
                cell_number.grid(row = i, column = j)
                cell_data = {"frame": cell_frame, "number": cell_number}
                row.append(cell_data)
            self.cells.append(row)
                
        # Puntaje
        score_frame = tk.Frame(self)
        score_frame.place(relx = 0.5, y = 45, anchor = "center")
        tk.Label(
            score_frame,
            text = "Score",
            font = "black"
        ).grid(row = 0)
        self.score_label = tk.Label(score_frame, text="0", font = 'black')
        self.score_label.grid(row = 1)
    
    def update_GUI(self, M, score):
        for i in range(4):
            for j in range(4):
                cell_value = M[i][j]
                if cell_value == 0:
                    self.cells[i][j]["frame"].configure(bg = "#c2b3a9")
                    self.cells[i][j]["number"].configure(bg = "#c2b3a9", text="")
                else:
                    self.cells[i][j]["frame"].configure(bg = CELL_COLORS[cell_value])
                    self.cells[i][j]["number"].configure(
                        bg = CELL_COLORS[cell_value], 
                        fg = CELL_NUMBER_COLORS[cell_value],
                        font = ("Helvetica", 40, "bold"),
                        text = str(cell_value)
                    )
        self.score_label.configure(text = score) #Marcador
        #self.update_idletasks()



def crear_Matriz(tam):
    M = [[ 0 for j in range (tam)] for i  in range(tam) ]
    print("")
    return M

# root = Tk() #Se crea la raiz
M = crear_Matriz(4)
M[1][1] = 2
M[1][3] = 2
M[0][0] = 2048
game = interface()
#game.update_GUI(M, 0)
#root.mainloop() #Comienzo de la app While True
