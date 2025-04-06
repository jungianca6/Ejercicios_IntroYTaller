"""Giancarlo Vega Marin
   Carné:2020195338
   Examen Parcial #2 Intro Progra"""
#E:
#S:
#R:

#Problema 1

#E:numero
#S:eliminar digitos iguales que esten juntos
#R:numero entero

def elimine_juntos(num):
    if isinstance(num,int):
        return juntosaux(num,0,0)
    else:
        return 'error'

def juntosaux(num,exp,nuevonum):      #":" añadido
    while num!=0:
        if num%10==(num//10)%10:
            num//=100
        else:
            nuevonum+=(num%10*10**exp)
            num//=10
            exp+=1
    return nuevonum

#Problema 2
#E:lista
#S:cuantos caballos tuvieron mas de 100 puntos, menor de 99, nombre de caballos con mayor y mejor puntaje, promedio
#R:lista no nula y que sea lista

def derby(lista): #":" añadido
    if isinstance(lista,list):
        return derbyaux(lista,lista[0],lista[0],0,0,0,0)
    else:
        return 'error'

def derbyaux(lista,mayor,menor,puntuacionmayor,puntuacionmenor,suma,i):   #":" añadido
    if i==len(lista):
        return [puntuacionmayor,puntuacionmenor,mayor[0],menor[0],suma/len(lista)]
    else:
        x=lista[i][1]

        if mayor[1]<x:
            mayor= lista[i]
        if menor[1]>x:
            menor= lista[i]
        suma+=x
        if 100<=X:
            puntuacionmayor+=1
        else:
            puntuacionmenor+=1
    return derbyaux(lista,mayor,menor,puntuacionmayor,puntuacionmenor,suma,i+1)

#Problema 3
#E:numero
#S:numero entero partido en sublistas de lista como punto de corte el cero
#R:numero entero

def split(num):
    if isinstance(num,int):
        return splitaux(num,0,[],0)
    else:
        return 'error'
def splitaux(num,exp,newlist,sublist):      #":" añadido
    if num==0:
        return [sublist]+newlist
    if sublist==0:
        return splitaux(num//10,0,newlist+[],0)
    elif num%10==0:
        return splitaux(num//10,0,[sublist]+newlist,0)
    else:
        return splitaux(num//10,exp+1,newlist,sublist + num%10*10**exp)   #en el pdf, el [] en num%10 esta tachado, no se toma en cuenta. No pude poner corrector

#Problema 4
#E:matriz
#S:booleano si diagonales iguales y los demas son cero
#R:matriz nxn

def matriz_escalar(mat):
    if len(mat)==len(mat[0]):       #":" añadido
        return escalaraux(mat,0,0,1,1)   #":" removido
    else:
        return 'error'

def escalaraux(mat,i,j,x,y):    #":" añadido
    if i==len(mat): #fue por el tiempo pero era len(mat). Solo es eso ahi, lo demas esta bien
        return True
    if i==j:        #":" añadido
        if mat[i][j]==mat[x][y]:   #":" añadido
            return escalaraux(mat,i,j,x+1,y+1)
        else:
            return False
    elif j==len(mat):   #":" añadido
        return escalaraux(mat,i+1,j,x,y)
    elif mt[i][j]==0:       #":" añadido
        return escalaraux(mat,i,j+1,x,y)
    else:
        return False

    
