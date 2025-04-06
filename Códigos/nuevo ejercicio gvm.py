#Trabajo 7
#giancarlo vega marin
#20201958338

#1
#E:dos listas de numeros
#S:lista donde cada elemento es una lista de dos elementos:
#multiplicacion y division de los digitos de la misma posicion de ambas listas
#R:listas del mismo tamaño
def producto_div(lista1,lista2):
    if isinstance(lista1,list) and isinstance(lista2,list)and lista1!=[] and lista2!=[] and len(lista1)==len(lista2):
      return prodiv_aux(lista1,lista2)
    else:
      return 'error'

def prodiv_aux(lista1,lista2):
    if lista1==[] and lista2==[]:
      return []
    else:
      return [[lista1[0]*lista2[0]],[lista1[0]/lista2[0]]] + prodiv_aux(lista1[1:],lista2[1:])

#2
#E:lista y elemento
#S:elimine de la lista la primera aparicion del elemento
#R:que sea lista, y elemento un numero natural
def eliminarele(lista,ele):
    if isinstance(lista,list) and isinstance(ele,int):
      return eliminareleaux(lista,ele)
    else:
      return 'error'

def eliminareleaux(lista,ele):
    if lista==[]:
      return []
    elif lista [0]==ele:
      return lista[1:]
    else:
      return [lista[0]]+ eliminareleaux(lista[1:],ele)

#3
#E:lista
#S:el promedio de las calificaciones 
#R:lista con 10 elementos
def calificacion(lista):
    if isinstance(lista,list) and len(lista)==10:
        return calificacion_aux(lista)
        if cien==True:
            return calificacion_aux(lista,0)
        else:
            return 'error'  
    else:
        return 'error'

def cien(lista):
    if lista==[]:
        return True
    elif lista[0]>=0 and lista[0]<=100:
        return cien(lista[1:])
    else:
        return False

def calificacion_aux(lista):
    if lista==[]:
        return []
    else:
        return eliminar2(lista,dig2)
    
def PromedioDeJueces(lista):
    if lista!=[]:
        return lista[0]+PromedioDeJueces(lista[1:])
    else:
        return 0

def eliminar(lista,dig1):
    dig1==Menor(lista)
    if lista==[]:
        return []
    if lista[0]==Menor(lista):
        return lista[1:]
    else:
        return [lista[0]]+ eliminar(lista[1:],dig1)

   
def eliminar2(lista,dig2):
    dig2==Mayor(lista)
    if lista[0]==[]:
        return []
    if lista[0]==Mayor(lista):
        return lista[1:]
    else:
        return [lista[0]]+ eliminar(lista[1:],dig2)


def Menor(lista):
    if len(lista)==1:
        return lista[0]
    elif lista[1]>=lista[0]:
        return  Menor([lista[0]]+lista[2:])
    elif lista[0]>=lista[1]:
        return Menor(lista[1:])

def Mayor(lista):
    if len(lista)==1:
        return lista[0]
    elif lista[1]<=lista[0]:
        return  Mayor([lista[0]]+lista[2:])
    elif lista[0]<=lista[1]:
        return Mayor(lista[1:])

#4
#E:lista
#S:booleano que verifique si todos los elementos de la lista fueron pares
#R:que sea una lista
def todos_pares(lista):
    if isinstance (lista,list):
        return todospares_aux(lista)
    else:
        return 'error'

def todospares_aux(lista):
    if lista==[]:
        return True
    elif lista[0]%2!=0:
        return False
    else:
        return todospares_aux(lista[1:])
    

#5
#E:lista
#S:booleano que verifica si al menos un número de la lista es par
#R:que sea una lista
def hay_par(lista):
    if isinstance(lista,list):
        return haypar_aux(lista)
    else:
        return 'error'

def haypar_aux(lista):
    if lista==[]:
        return False
    elif lista[0]%2==0:
        return True
    else:
        return haypar_aux(lista[1:])

#6
#E:numero natural
#S:lista en orden ascendente de numeros naturales menores al dado
#R:numero natural
def iota(num):
    if isinstance(num,int):
        return iota_aux(abs(num))
    else:
        return 'error'

def iota_aux(num):
    if num==0:
        return []
    else:
        return iota_aux(num-1)+[(num-1)%10]
    
#7
#E:lista
#S:dos sublistas que contenga los elementos pares y los impares
#R:lista no nula
def separa(lista):
    if isinstance(lista,list) and lista!=[]:
        return separa_aux(lista)

def separa_aux(lista):
    pares=pares_aux(lista)
    impares=impares_aux(lista)
    if lista==[]:
        return []
    else:
        return (pares,impares)

def pares_aux(lista):
    if lista == []:
        return []
    elif lista[0] %2 == 0:
        return [lista[0]]+ pares_aux(lista[1:])
    else:
        return pares_aux(lista[1:])

def impares_aux(lista):
    if lista == []:
        return []
    elif lista[0] %2 != 0:
        return [lista[0]]+ impares_aux(lista[1:])
    else:
        return impares_aux(lista[1:])

    



