#Trabajo clase #11 Taller Progra
#Giancarlo VM
#1
#E:dos vectores
#S:producto de vectores
#R:vectores del mismo tamaño
def  prod_vector (v,w):
    if len(v)==len(w):
        return prodvecaux(v,w,0,0)
    else:
        return 'error'

def prodvecaux(v,w,i,vecprod):
    if i==len(v):
        return vecprod
    else:
        return prodvecaux(v,w,i+1,vecprod+v[i]*w[i])

#2
#E:vector 
#S:vector inverso
#R:vector de tamaño n
def vector_invert(v):
    if len(v)>2:
        return invertaux(v,[],0)
    else:
        return v

def invertaux(v,invertido,i):
    if i==len(v):
        return invertido
    else:
        return invertaux(v,[v[i]]+invertido,i+1)

#3
#E:dos vectores
#S:booleano que verifique si todos los elementos del primer vector estan contenidos en el otro vector
#R:vectores
def inn(v, w):
    return inn_aux(v, w,0)

def estaNum(num,lista,i):
    if i == len(lista):
        return False
    elif lista[i] != num:
        return estaNum(num,lista,i+1)
    elif lista[i] == num:
        return True

def inn_aux(lista1,lista2,i):
    if i == len(lista1):
        return True
    elif estaNum(lista1[i],lista2,0):
        return inn_aux(lista1,lista2,i+1)
    else:
        return False

#4
#E:matriz
#S:print de la matriz en consola
#R:matriz
def muestreM(matriz):
   if len(matriz) == 0:
      return
   print('[', end=' ')
   muestreM_aux(matriz[0])
   print(']', end=' ')
   print()
   muestreM(matriz[1:])

def muestreM_aux(fila):
   if len(fila) == 0:
      return
   print(fila[0], end=' ')
   muestreM_aux(fila[1:])
   
#5
#E:matriz
#S:diagonal de la matriz
#R:matriz de tamaño nxn, o matriz cuadrada
def diagonal(matriz):
    if len(matriz)==len(matriz[0]):
        return diagonalaux(matriz,[],0)
    else:
        return 'error'

def diagonalaux(matriz,diag,i):
    if matriz==[]:
        return diag
    else:
        return diagonalaux(matriz[1:],diag+[matriz[0][i]],i+1)
        
#6
#E:matriz
#S:vector con los maximos de cada una de las filas de matriz
#R:matriz nxm de enteros
def maximos(matriz):
    if len(matriz)==len(matriz[0]):
        return mayormatriz(matriz,0,0,matriz[0][0],[])
    else:
        return 'error'

                          
def mayormatriz(matriz,i,j,mayor,mayores):
    if i==len(matriz):
        return mayores
    if j==len(matriz):
        return mayormatriz(matriz,i+1,0,matriz[i][0],mayores+[mayor])
    elif matriz[i][j]>mayor:
        return mayormatriz(matriz,i,j+1,matriz[i][j],mayores)
    else:
        return mayormatriz(matriz,i,j+1,mayor,mayores)

def minimosmat(matriz):
    if len(matriz)==len(matriz[0]):
        return menormatriz(matriz,0,0,matriz[0][0],[])
    else:
        return 'error'

                          
def menormatriz(matriz,i,j,menor,menores):
    if i==len(matriz):
        return menores
    if j==len(matriz):
        return menormatriz(matriz,i+1,0,matriz[0][0],menores+[menor])
    elif matriz[i][j]<menor:
        return menormatriz(matriz,i,j+1,matriz[i][j],menores)
    else:
        return menormatriz(matriz,i,j+1,menor,menores)
