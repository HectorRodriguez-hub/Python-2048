from tkinter import * 

class interface:
    def __init__(self, ventana):
        #inicialización de la ventana
        self.ventana = ventana
        self.ventana.title("2048") #Titulo a la venta
        self.ventana.geometry("700x500") #darle tamaño a la ventana 
        self.ventana.resizable(1,1) #Desactivar que se pueda redimensionar 
        #self.ventana.iconbitmap() #Icono de ventana - formato ico, xbm (linux)
        self.ventana.config(bg="red")

        boton = Button(self.ventana, text="")


        label = Button(self.ventana)
        label.config(width = 30 , height = 100 , text = "perros")
        label.pack()

root = Tk() #Se crea la raiz
game = interface(root)
root.mainloop() #Comienzo de la app While True
