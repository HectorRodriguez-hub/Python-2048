## =========================================================================
## Autores :
## Camilo Andres Moreno Colorado
## Aldemar Yamid Ramirez Avila
## Héctor René Rodríguez Hernández 
## =========================================================================

import math, random, os, itertools
import time as t

## -------------------------------------------------------------------------
class arcade:
    def __init__(self):
        self.tam = 4
        
    def Print(self, M):
        for j in range(len(M)):
            for i in range(len(M[0])):
                
                if M[i][j] == math.inf:
                    print("X","",end = "")
                else:
                    print(M[i][j],"",end = "")
            #end for
            print()
        print("----------------------------")
        #end for
    #end def

    ## -------------------------------------------------------------------------
    #funciones de juego
    def crear_Matriz(self):
        M = [[ 0 for j in range (self.tam)] for i  in range(self.tam) ]
        print("")
        return M
    #end def

    ## -------------------------------------------------------------------------
    def start(self, M):
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
    def arriba(self, M, puntaje):
        for i in range(self.tam):
            j = 0 
            k = j+1 
            while j < self.tam and k < self.tam:
                if M[i][j] == 0 and M[i][k] != 0:
                    M[i][j] = M[i][k]
                    M[i][k] = 0  
                else: 
                    if M[i][j] == M[i][k] and M[i][j] != 0:
                        M[i][j] = M[i][j]*2
                        puntaje += M[i][j]
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
        return [M, puntaje]
    #end def
    
    ## -------------------------------------------------------------------------
    def izquierda(self, M, puntaje):
        for j in range(self.tam):
            i = 0 
            k = i+1 
            while j < self.tam and k < self.tam:
                if M[i][j] == 0 and M[k][j] != 0:
                    M[i][j] = M[k][j]
                    M[k][j] = 0  
                else: 
                    if M[i][j] == M[k][j] and M[i][j] != 0:
                        M[i][j] = M[i][j]*2
                        puntaje += M[i][j]
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
        return [M, puntaje]
    #end def
    
    ## -------------------------------------------------------------------------
    def derecha(self, M, puntaje):
        for j in range(self.tam):
            i = self.tam -1
            k = i-1
            while j > -1 and k > -1:
                if M[i][j] == 0 and M[k][j] != 0:
                    M[i][j] = M[k][j]
                    M[k][j] = 0  
                else:
                    if M[i][j] == M[k][j] and M[i][j] != 0:
                        M[i][j] = M[i][j]*2
                        puntaje += M[i][j]
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
        return [M, puntaje]
    #end def
    
    ## -------------------------------------------------------------------------
    def abajo(self, M, puntaje):
        for i in range(self.tam):
            j = self.tam - 1
            k = j - 1 
            while j > -1 and k > -1:
                if M[i][j] == 0 and M[i][k] != 0:
                    M[i][j] = M[i][k]
                    M[i][k] = 0  
                else: 
                    if M[i][j] == M[i][k] and M[i][j] != 0:
                        M[i][j] = M[i][j]*2
                        puntaje += M[i][j]
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
        return [M, puntaje]
    #end def
    
    ## -------------------------------------------------------------------------
    def iguales(self, C, M):
        for i in range(self.tam):
            for j in range(self.tam):
                if C[i][j] != M[i][j]:
                    return False
        return True
    #end def 
    
    ## -------------------------------------------------------------------------
    def opcional(self, M):
        C = self.copia(M)
        op = [True,True,True,True]
        if self.iguales(M,  self.arriba(C, 0)[0]):
            op[0] = False
        if self.iguales(M,  self.abajo(C, 0)[0]):
            op[1] = False
        if self.iguales(M,  self.derecha(C, 0)[0]):
            op[2] = False
        if self.iguales(M,  self.izquierda(C, 0)[0]):
            op[3] = False
        if True in op:
            return True
        return False 
    #end def
    
    ## -------------------------------------------------------------------------
    def choose_combinations(self, select, max_puntaje):
        for i in range(4,1,-1):
            for c in itertools.combinations(select,i):
                if i == 4:
                    if c[0][1] == c[1][1] and c[1][1] == c[2][1] and c[2][1] == c[3][1] and c[3][1] == max_puntaje:
                        r = random.choice(c)
                        while not r[2]:
                            r = random.choice(c)
                        return r[0]
                    
                if i == 3:
                    if c[0][1] == c[1][1] and c[1][1] == c[2][1] and c[2][1] == max_puntaje:
                        r = random.choice(c)
                        while not r[2]:
                            r = random.choice(c)
                        return r[0]
                    
                if i == 2:
                    if c[0][1] == c[1][1] and c[1][1] == max_puntaje:
                        r = random.choice(c)
                        while not r[2]:
                            r = random.choice(c)
                        return r[0]
                if i == 1:
                    if c[0][1] == max_puntaje:
                        return c[0][0]
    #end def


    ## -------------------------------------------------------------------------

    def max_score(self, M, puntaje):
        #t.sleep(4)
        C = self.copia(M)
        select = [['w',puntaje, False],['a',puntaje, False],['s',puntaje, False],['d',puntaje, False]]
        #print('antes: ',select)
        if not self.iguales(M,  self.arriba(C, 0)[0]):
            H = self.copia(M)
            select[0][1] += self.arriba(H,0)[1]
            select[0][2] = True
        C = self.copia(M)
        if not self.iguales(M,  self.abajo(C, 0)[0]):
            H = self.copia(M)
            select[2][1] += self.abajo(H,0)[1]
            select[2][2] = True
        C = self.copia(M)
        if not self.iguales(M,  self.derecha(C, 0)[0]):
            H = self.copia(M)
            select[3][1] += self.derecha(H,0)[1]
            select[3][2] = True
        C = self.copia(M)
        if not self.iguales(M,  self.izquierda(C, 0)[0]):
            H = self.copia(M)
            select[1][1] += self.izquierda(H,0)[1]
            select[1][2] = True
        
        #print("despues: ",select)
        '''
        if select[3][2]:
            print(select[3][0])
            return select[3][0]
        if select[2][2]:
            print(select[2][0])
            return select[2][0]
        if select[0][2]:
            print(select[0][0])
            return select[0][0]
        if select[1][2]:
            print(select[1][0])
            return select[1][0]
        
        '''
        max_puntaje = max(select[0][1],select[1][1],select[2][1],select[3][1])
        #print('puntaje: ', max_puntaje)
        
        return self.choose_combinations(select, max_puntaje)
    #end def

    ## -------------------------------------------------------------------------
    def aleatorio(self, M):
        vacios = []
        num_proba = [2, 2, 2, 2, 2, 2, 4, 4] 
        for i in range(self.tam):
            for j in range(self.tam):
                if M[i][j] == 0:
                    vacios.append([i,j])
        if len(vacios) > 0:
            ale = random.choice(vacios)
            M[ale[0]][ale[1]] = random.choice(num_proba)
        
    ## =========================================================================
    def copia(self, M):
        C = [[0 for i in range(self.tam)] for j in range(self.tam)]
        for i in range(self.tam):
            for j in range(self.tam):
                C[i][j] = M[i][j]
        return C
    