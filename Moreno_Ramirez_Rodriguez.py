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
    for j in range(len(M)):
        for i in range(len(M[0])):
            
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
    M[0][0] = 2
    M[0][1] = 2
    M[0][2] = 2
    M[0][3] = 2
    M[1][0] = 2
    M[1][1] = 2
    M[1][2] = 2
    M[1][3] = 2
    M[2][0] = 2
    M[2][1] = 2
    M[2][2] = 2
    M[2][3] = 2
    M[3][0] = 2
    M[3][1] = 2
    M[3][2] = 2
    M[3][3] = 2

    return M
#end def

def arriba(M):
    for i in range(tam):
        j = 0 
        k = j+1 
        while j < tam and k < tam:
            if M[i][j] == M[i][k] and M[i][j] != 0:
                M[i][j] = M[i][j]*2
                M[i][k] = 0
                j = j+1
                k = j+1
            else:
                if M[i][j] == 0 and M[i][k] != 0:
                    M[i][j] = M[i][k]
                    M[i][k] = 0
                    k = k+1
                else:
                    k = k+1
    return M
#end def
def izquierda(M):
    for j in range(tam):
        i = 0 
        k = i+1 
        while i < tam and k < tam:
            if M[i][j] == M[k][j] and M[i][j] != 0:
                M[i][j] = M[i][j]*2
                M[k][j] = 0
                i = i+1
                k = k+1
            else:
                if M[i][j] == 0 and M[k][j] != 0:
                    M[i][j] = M[k][j]
                    M[k][j] = 0
                    k = k+1
                else:
                    k = k+1
    return M
#end def

#LLamado a funciones
M = crear_Matriz(tam)
Print(M)
start(M)
Print(M)
arriba(M)
Print(M)
izquierda(M)
Print(M)





""" while game:
    tecla = input("Please type a key")
    if tecla== 'w':
        print("ES LA W :)") """
    