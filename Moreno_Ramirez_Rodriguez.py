""" Autores :
Camilo Andres Moreno Colorado
Aldemar Yamid Ramirez Avila
Héctor René Rodríguez Hernández """

#Imports 
import math, random, os
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
#end def
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
    M[0][0] = 2 
    M[0][1] = 16
    M[0][2] = 8
    M[0][3] = 4

    M[1][0] = 4
    M[1][1] = 8
    M[1][2] = 16
    M[1][3] = 32

    M[2][0] = 8
    M[2][1] = 16
    M[2][2] = 32
    M[2][3] = 128

    M[3][0] = 16
    M[3][1] = 128
    M[3][2] = 0
    M[3][3] = 0
    return M
#end def
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
def iguales(C,M):
    for i in range(tam):
        for j in range(tam):
            if C[i][j] != M[i][j]:
                return False
    return True
#end def 
def opcional(M):
    print("entro opcional")
    C = copia(M)
    op = [True,True,True,True]
    print(op)
    print("opcional arriba")
    if iguales(C,arriba(M)):
        op[0] = False
        M = copia(aux)
    if iguales(C,abajo(M)):
        op[1] = False
        M = copia(aux)
    if iguales(C,derecha(M)):
        op[2] = False
        M = copia(aux)
    if iguales(C,izquierda(M)):
        op[3] = False
        M = copia(aux)
    print(op)
    if True in op:
        return True
    return False 
#end def
def aleatorio(M):
    print("entro aleatorio")
    vacios = []
    for i in range(tam):
        for j in range(tam):
            if aux[i][j] == 0:
                vacios.append([i,j])
    print("vacios", vacios)
    if len(vacios) > 0:
        print("entro agregar 2")
        ale = random.choice(vacios)
        aux[ale[0]][ale[1]] = 2
    else:
        print("va opcional")
        r = opcional(M)
        return r 
#end def
def copia(M):
  C = [[0 for i in range(tam)] for j in range(tam)]
  for i in range(tam):
    for j in range(tam):
      C[i][j] = M[i][j]
  return C
#end def

#LLamado a funciones
print("Bienvenidos a 2048")
M = crear_Matriz(tam)
start(M)
aux = copia(M)
conti = True
r = True
#game
while game and conti != False:
    M = copia(aux)
    Print(M)
    C = copia(aux)
    ale = True
    tecla = input("Please type a key: ")
    entrada = tecla.lower()
    if entrada== 'w':
        aux = arriba(aux)
        Print(aux)
        Print(C)
        if iguales(C,aux):
            ale = False
    if entrada== 'd':
        aux = derecha(aux)
        if iguales(C,aux):
            ale = False
    if entrada== 'a':
        aux = izquierda(aux)
        if iguales(C,aux):
            ale = False
    if entrada== 's':
        aux = abajo(aux)
        if iguales(C,aux):
            ale = False
    if ale == True:
        r = aleatorio(M)
    conti = r 
    os.system("pause")
    os.system("cls")