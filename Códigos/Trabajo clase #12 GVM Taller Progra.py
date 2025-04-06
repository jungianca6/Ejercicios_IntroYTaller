"""Conceptos:

1. Iteración: La iteración es la forma más natural y común de ejecutar
repeticiones de acciones, es alternativa al uso de recursividad

Condición para continuar el ciclo: La funcion "while" define la condicion que continúa el ciclo 

2.
En ocasiones es necesario terminar la ejecución del while de una maera
directa. En Python se puede utilizar break. 

"""






#Ejercicios

#1
#E:numero
#S:booleano que verifica si la suma de sus digitos es mayor o igual a 10
#R:numero entero
def suma10(num):
    if isinstance(num,int):
        num=abs(num)
        suma = 0
        while num!=0:
            suma += num%10
            num//= 10
        return suma>=10
    else:
        return 'error'

#2
#E:numero
#S:tupla con la cantidad de digitos mayores a 5, y los digitos menores o iguales a 5
#R:numero entero
def digitos(num):
    if isinstance(num,int):
        num=abs(num)
        mayores=0
        menores=0
        while num!=0:
            if num%10>5:
                mayores+=1
                num//=10
            else:
                menores+=1
                num//=10

        return (mayores,menores)
    else:
        return 'error'

#3
#E:numero
#S:numero formado por los digitos pares del numero de entrada
#R:numero entero
def forma_par(num):
    if isinstance(num,int):
        num=abs(num)
        pares=0
        exp=0
        while num!=0:
            if (num%10)%2==0:
                pares+=num%10*10**exp
                exp+=1
                num//=10
            else:
                num//=10
                exp+=0
        return pares
    else:
        return 'error'
            
#4
#E:numero
#S:booleano que verifica si el primer y ultimo digito del numero son iguales
#R:numero entero
def iguales(num):
    if isinstance(num,int):
        num=abs(num)
        dig1=num%10
        dig2=None
        while num!=0:
            dig2=num%10
            num//=10
        return dig1==dig2
    else:
        return 'error'
#5
#E:numero
#S:lista en orden ascendente de numeros naturales menores al numero dado
#R:numero natural 
def iota(num):
    if isinstance(num,int):
        num=abs(num)
        result=[]
        x=0
        while x<num:
            result.append(x)
            x+=1
        return result
    else:
        return 'error'
#6
#E:lista 
#S:lista que tenga los numeros mayores que 5, y los numeros menores o iguales a 5
#R:lista de digitos
def digitos(lista):
    if isinstance(lista,list):
        mayores=0
        menores=0
        i = 0
        while i<len(lista):
            if lista[i]>5:
                mayores+=1
            else:
                menores+=1
            i+=1
        return [mayores,menores]
#7
#E:lista de numeros
#S: Cuántos estudiantes aprobaron el curso, cuantos estudiantes reprobaron y el promedio de notas 
#R: lista de digitos no nula
def notas(lista):
    if isinstance(lista,list):
        aprobados = 0
        reprobados = 0
        suma = 0
        for nota in lista:
            if nota>= 70:
                aprobados +=1
            else:
                reprobados +=1
            suma +=nota
        promedio = suma/len(lista)
        print (f"a)Estudiantes aprobados:{aprobados} \nb)Estudiantes reprobados: {reprobados} \nc)Promedio de notas:{promedio}")
#8
#E:lista 
#S:booleano que verifica si todos los numeros de la lista son pares
#R:lista no nula
def todos_pares(lista):
    result = True
    for num in lista:
        if (num%2)!=0:
            result = False
            break
    return result
