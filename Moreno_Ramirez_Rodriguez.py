## =========================================================================
## Autores :
## Camilo Andres Moreno Colorado
## Aldemar Yamid Ramirez Avila
## Héctor René Rodríguez Hernández 
## =========================================================================

#Imports 
import math, random, os

## -------------------------------------------------------------------------
## Variables globales
## -------------------------------------------------------------------------

tam=4
game=True

## -------------------------------------------------------------------------
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

## -------------------------------------------------------------------------
#funciones de juego
def crear_Matriz(tam):
    M = [[ 0 for j in range (tam)] for i  in range(tam) ]
    print("")
    return M
#end def

## -------------------------------------------------------------------------
def start(M):
    i = random.randint(0,3)
    j = random.randint(0,3)
    M[i][j] = 2
    a = random.randint(0,3)
    b = random.randint(0,3)
    while i == a and j ==b:
        a = random.randint(0,3)
        b = random.randint(0,3)
    #end whle
    M[a][b] = 2
    return M
#end def

## -------------------------------------------------------------------------
def arriba(M):
    for i in range(tam):
        j = 0 
        k = j+1 
        while j < tam and k < tam:
            if M[i][j] == 0 and M[i][k] != 0:
                M[i][j] = M[i][k]
                M[i][k] = 0  
            else: 
                if M[i][j] == M[i][k] and M[i][j] != 0:
                    M[i][j] = M[i][j]*2
                    M[i][k] = 0
                    j = j + 1
                    k = j + 1
                else: 
                    if  M[i][j] !=0 and M[i][k] != 0 :
                        j = j+1 
                        k = j+1
                    else: 
                        if M[i][k] == 0: 
                            k = k+1
    return M
#end def

## -------------------------------------------------------------------------
def izquierda(M):
    for j in range(tam):
        i = 0 
        k = i+1 
        while j < tam and k < tam:
            if M[i][j] == 0 and M[k][j] != 0:
                M[i][j] = M[k][j]
                M[k][j] = 0  
            else: 
                if M[i][j] == M[k][j] and M[i][j] != 0:
                    M[i][j] = M[i][j]*2
                    M[k][j] = 0
                    i = i + 1
                    k = i + 1
                else: 
                    if  M[i][j] !=0 and M[k][j] != 0  and M[i][j] != M[k][j]:
                        i = i + 1 
                        k = i + 1
                    else: 
                        if M[k][j] == 0: 
                            k = k + 1
    return M
#end def

## -------------------------------------------------------------------------
def derecha(M):
    for j in range(tam):
        i = tam -1
        k = i-1
        while j > -1 and k > -1:
            if M[i][j] == 0 and M[k][j] != 0:
                M[i][j] = M[k][j]
                M[k][j] = 0  
            else:
                if M[i][j] == M[k][j] and M[i][j] != 0:
                    M[i][j] = M[i][j]*2
                    M[k][j] = 0
                    i = i - 1
                    k = i - 1
                else: 
                    if  M[i][j] !=0 and M[k][j] != 0  and M[i][j] != M[k][j]:
                        i = i - 1 
                        k = i - 1
                    else: 
                        if M[k][j] == 0:
                            k = k - 1
    return M
#end def

## -------------------------------------------------------------------------
def abajo(M):
    for i in range(tam):
        j = tam - 1
        k = j - 1 
        while j > -1 and k > -1:
            if M[i][j] == 0 and M[i][k] != 0:
                M[i][j] = M[i][k]
                M[i][k] = 0  
            else: 
                if M[i][j] == M[i][k] and M[i][j] != 0:
                    M[i][j] = M[i][j]*2
                    M[i][k] = 0
                    j = j - 1
                    k = j - 1
                else: 
                    if  M[i][j] !=0 and M[i][k] != 0 :
                        j = j - 1 
                        k = j - 1
                    else: 
                        if M[i][k] == 0: 
                            k = k - 1
    return M
#end def

## -------------------------------------------------------------------------
def aleatorio(M):
    i = random.randint(0,3)
    j = random.randint(0,3)
    cont = 0
    while M[i][j] != 0:
        i = random.randint(0,3)
        j = random.randint(0,3)
    M[i][j] = 2
#end def 
def opciones(M):
    a = arriba(M)
    if a == M:
        return True
#end def


## -------------------------------------------------------------------------
## ---------------------------------- MAIN ---------------------------------
## -------------------------------------------------------------------------

#LLamado a funciones
M = crear_Matriz(tam)
start(M)
print("Bienvenidos a 2048")

#game
while game:
    Print(M)
    tecla = input("Please type a key: ")
    entrada = tecla.lower()
    if entrada== 'w':
        arriba(M)
    if entrada== 'd':
        derecha(M)
    if entrada== 'a':
        izquierda(M)
    if entrada== 's':
        abajo(M)
    if entrada== 'n':
        game = False
    aleatorio(M)
    os.system("cls")