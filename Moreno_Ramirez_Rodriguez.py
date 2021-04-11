""" Autores :
Camilo Andres Moreno Colorado
Aldemar Yamid Ramirez Avila
Héctor René Rodríguez Hernández """

import math
#Variables globales
#Hola Ternuras
tam=4
game=True


def Print(M):
    for i in range(len(M)):
        for j in range(len(M[0])):
            
            if M[i][j] == math.inf:
                print("X","",end = "")
            else:
                #print("-","",end = "")
                print(M[i][j],"",end = "")
                
            #print(M[i][j],"",end = "")
        #end for
        print()
    print("----------------------------")
    #end for
#end def

def crear_Matriz(tam):
    M = [['x' for j in range(tam)]for i in range(tam)]
    print("")
    Print(M)





#LLamado a funciones
crear_Matriz(tam)



""" while game:
    tecla = input("Please type a key")
    if tecla== 'w':
        print("ES LA W :)") """
    