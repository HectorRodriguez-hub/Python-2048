""" Autores :
Camilo Andres Moreno Colorado
Aldemar Yamid Ramirez Avila
Héctor René Rodríguez Hernández """

#Imports 
import math, random
#Variables globales
tam=4
game=True
#funciones de impresion
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

#funciones de juego
def crear_Matriz(tam):
    M = [[ 0 for j in range (tam)] for i  in range(tam) ]
    print("")
    return M

def start(M):
    i = random.randint(0,3)
    j = random.randint(0,3)
    a = random.randint(0,3)
    b = random.randint(0,3)
    while i == a and j ==b:
        a = random.randint(0,3)
        b = random.randint(0,3)
    M[3][0] = 2
    M[1][0] = 2
    return M
#end def

def prueba(M):
    for j in range(tam):
        for i in range(tam):
            if i == 0 and j == 0:
                M[j][i] = M[j][i]+ M[j][i]
                M[j+1 ][i] = 0 
    return M            
#end def


#LLamado a funciones
M = crear_Matriz(tam)
Print(M)
start(M)
Print(M)
prueba(M)
Print(M)


""" while game:
    tecla = input("Please type a key")
    if tecla== 'w':
        print("ES LA W :)") """
    