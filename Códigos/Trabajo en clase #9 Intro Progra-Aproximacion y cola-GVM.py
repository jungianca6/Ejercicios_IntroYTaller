"""
Trabajo en clase #9 Intro Progra- Recursividad cola y aproximación
Giancarlo Vega Marín"""

#1
#E:numero
#S:serie numérica establecida a partir de 2
#R:numero entero, numero mayor o igual a 2
#Serie:2,5,7,10,12,15,17,20...
def serie(num):
    if isinstance(num,int) and num>=2:
        return serieaux(abs(num),1,0,[2])
    else:
        return 'error'

def serieaux(num,i,n,result):
    if (2*i)+n>=num:  # caso base
        return result
    elif i==1:
        return serieaux(num,i+1,n+1,result)
    elif i%2==0:
        return serieaux(num,i+1,n,result+[((2*i)+n)])
    else:
        return serieaux(num,i+1,n+1,result+[((2*i)+n)])

#2
#E:numero
#S:cuantas veces aparecen digitos en parejas
#R:numero entero
def parejas(num):
    if isinstance(num,int):
        return parejasaux(abs(num),0)
    else:
        return 'error'

def parejasaux(num,result):
    if num==0:   # caso base
        return result 
    elif num%10==(num//10)%10:
        return parejasaux(num//100,result+1)
    else:
        return parejasaux(num//100,result)

#3
#E:lista de 10 elementos
#S:promedio de las calificaciones, excluyendo el mayor y menor
#R:que tenga 10 numeros la lista, y que el numero sea del 1 al 10
def calificacion(lista):
    if isinstance(lista,list)and lista!=[] and len(lista)==10: 
        return promedio(lista)
        if diez(lista)==True:
            return promedio(lista)
        else:
            return 'error'
    else:
        return 'error'

def promedio(lista):
    return (sumacalificaciones(eliminarmayor(eliminarmenor(lista,menor(lista),[],0),mayor(lista),[],0),0))//len(eliminarmayor(eliminarmenor(lista,menor(lista),[],0),mayor(lista),[],0))

def sumacalificaciones(lista,suma):
    if lista==[]: # caso base
        return suma
    else:
        return sumacalificaciones(lista[1:],suma+lista[0])

def eliminarmenor(lista,menor,lista1,ele):
    if lista==[]: # caso base
        return lista1
    elif lista[0]==menor and ele==0:
        return eliminarmenor(lista[1:],menor,lista1,ele+1)
    elif ele>=1:
        return eliminarmenor(lista[1:],menor,lista1+[lista[0]],ele)
    else:
        return eliminarmenor(lista[1:],menor,lista1+[lista[0]],ele)
                           
def eliminarmayor(lista,mayor,lista2,ele):
    if lista==[]: # caso base
        return lista2
    elif lista[0]==mayor and ele==0:
        return eliminarmenor(lista[1:],mayor,lista2,ele+1)
    elif ele>=1:
        return eliminarmayor(lista[1:],mayor,lista2+[lista[0]],ele)
    else:
        return eliminarmayor(lista[1:],mayor,lista2+[lista[0]],ele)

def mayor(lista):
    if isinstance(lista,list) and lista!=[]:
        return mayor_aux(lista[1:], lista[0])
    else:
        return 'error'

def mayor_aux(lista, result):
    if lista == []: # caso base
        return result
    elif lista[0] > result:
        return mayor_aux(lista[1:], lista[0])
    else:
        return mayor_aux(lista[1:], result)

def menor(lista):
    if isinstance(lista,list) and lista!=[]:
        return menor_aux(lista[1:], lista[0])
    else:
        return 'error'
  
def menor_aux(lista, result):
    if lista == []: # caso base
        return result
    elif lista[0] < result:
        return menor_aux(lista[1:], lista[0])
    else:
        return menor_aux(lista[1:], result)

def diez(lista):
    if lista==[]:
        return True
    elif lista[0]>=0 and lista[0]<=10:
        return diez(lista[1:])
    else:
        return False

#4
#E:lista
#S:nueva lista con sus elementos invertidos
#R:que sea lista no nula
def invertir(lista):
    if isinstance(lista,list) and lista!=[]:
        return invertiraux(lista,[])
    else:
        return 'error'

def invertiraux(lista,inverso):
    if lista==[]:   # caso base
        return inverso
    else:
        return invertiraux(lista[1:],[lista[0]]+inverso)

#5
#E:lista y un numero
#S:eliminacion de elementos que coincidan con el numero dado, excepto su ultima aparicion
#R:lista no nula y numero entero
def elimine(lista,num):
    if isinstance(lista,list) and isinstance(num,int):
        return elimineaux(lista,num,0,contadornum(lista,num,0),[])
    else:
        return 'error'

def elimineaux(lista,num,elim,cont,nuevalist):
    if lista==[]:   # caso base
        return nuevalist
    if elim==(cont-1):
        return elimineaux(lista[1:],num,elim,cont,nuevalist+[lista[0]])
    elif lista[0]==num:
        return elimineaux(lista[1:],num,elim+1,cont,nuevalist)
    else:
        return elimineaux(lista[1:],num,elim,cont,nuevalist+[lista[0]])

def contadornum(lista,num,apariciones):
    if lista==[]:   # caso base
        return apariciones
    elif lista[0]==num:
        return contadornum(lista[1:],num,apariciones+1)
    else:
        return contadornum(lista[1:],num,apariciones)

#6
#E:lista y elemento
#S:eliminacion de todas las apariciones de ese elemento en la lista
#R:lista no nula y elemento entero
def eliminar_todos(lista,ele):
    if isinstance(lista,list) and isinstance(ele,int):
        return eliminartodosaux(lista,ele,[])
    else:
        return 'error'

def eliminartodosaux(lista,ele,newlist):
    if lista==[]:   # caso base
        return newlist
    elif lista[0]==ele:
        return eliminartodosaux(lista[1:],ele,newlist)
    else:
        return eliminartodosaux(lista[1:],ele,newlist+[lista[0]])

#7
#E:y (numero al que se va a calcular raíz)
#S:aproximacion de raiz quinta
#R:y>0
def raiz5(y, err):
    if isinstance(y, int) and y > 0 and isinstance(err, float) and err > 0 and err < 1:
        return raiz5_aux(y, err)
    else:
        return 'Error'

def raiz5_aux(Y, err):
    def XN(Xn):
        return (1/4) * (3 * Xn + (Y / Xn ** 4))

    def aux5(Xn, err):
        Xn1 = XN(Xn)
        error = abs(Xn1 - Xn)
        if error < err:
            return Xn1
        else:
            return aux5(Xn1, err)
    return aux5(1, err)

#8
#E:y (numero al que se va a calcular raíz)
#S:aproximacion raiz cúbica
#R:y>0
def raiz3(y):
    if isinstance(y, int) and y > 0:
        return raiz3_aux(y, 0.000001)
    else:
        return 'Error'
def raiz3_aux(Y, err):
    def XN(Xn):
        return (1/3) * (2 * Xn + Y / Xn**2)

    def aux3(Xn, err):
        Xn1 = XN(Xn)
        error = abs(Xn1 - Xn)
        if error < err:
            return Xn1
        else:
            return aux3(Xn1, err)
    return aux3(1, err)
