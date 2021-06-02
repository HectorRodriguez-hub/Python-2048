## =========================================================================
## Autores :
## Camilo Andres Moreno Colorado
## Aldemar Yamid Ramirez Avila
## Héctor René Rodríguez Hernández 
## =========================================================================

import math, random, os

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

    def max_score(self, M, puntaje):
        C = self.copia(M)
        w = a = s = d = puntaje
        select = ('w','s','a','d')
        if not self.iguales(M,  self.arriba(C, 0)[0]):
            H = self.copia(M)
            w += self.arriba(H,0)[1]
        if not self.iguales(M,  self.abajo(C, 0)[0]):
            H = self.copia(M)
            s += self.abajo(H,0)[1]
        if not self.iguales(M,  self.derecha(C, 0)[0]):
            H = self.copia(M)
            d += self.derecha(H,0)[1]
        if not self.iguales(M,  self.izquierda(C, 0)[0]):
            H = self.copia(M)
            a += self.izquierda(H,0)[1]
        if w == a and a == s and s == d:
            return random.choice(select)
        max_puntaje = max(w,a,s,d)
        if max_puntaje == s:
            return 's'
        if max_puntaje == d:
            return 'd'
        if max_puntaje == a:
            return 'a' 
        if max_puntaje == w:
            return 'w'
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
    