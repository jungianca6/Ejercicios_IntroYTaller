#Giancarlo Vega Marin
#2020195338
#Trabajo en Clase #8 Intro Progra

#1
#E:numero
#S:digito menor del numero
#R:numero entero
#pila
def menorpila(num):
    if isinstance(num,int):
        return menor_aux(abs(num))
    else:
        return 'error'
    
def menor_aux(num):
    if num//10 == 0: # caso base
         return num%10 # valor de retorno
    else:
        return compara(num%10, menor_aux(num//10))
    
def compara(x, y):
    if x < y:
        return x
    else:
        return y
#Cola
def menor(num):
    if isinstance(num,int):
        return menoraux(abs(num),num%10)
    else:
        return 'error'

def menoraux(num,result):
    if num==0:
        return result
    elif num%10<result:
        return menoraux(num//10,num%10)
    else:
        return menoraux(num//10,result)


#2
#E:numero y digito
#S:digitos del numero restados por el digito
#R:numero y digito entero
def restard(dig,num):
    if isinstance(num,int) and isinstance(dig,int) and dig>=0 and dig<=9:
        return restardaux(dig,abs(num),0,0)
    else:
        return 'error'

def restardaux(dig,num,result,exp):
    if num==0:
        return result
    elif (num%10-dig)<0:
        return restardaux(dig,num//10,result,exp+1)
    else:
        return restardaux(dig,num//10, result+(num%10-dig)*10**exp,exp+1)
        

#3
#E:numero
#S:digitos que sean multiplo de 4, se conviertan en cero
#R:numero entero
def cambia(num):
    if isinstance(num,int):
        return cambia_aux(abs(num),0,0)
    else:
        return 'error'

def cambia_aux(num,result,exp):
    if num==0:
        return result
    elif (num%10)%4==0:
        return cambia_aux(num//10,result,exp+1)
    else:
        return cambia_aux(num//10,result+(num%10)*10**exp,exp+1)

#4
#E:numero y digito
#S:tupla compuesta de los digitos del numero mayores al digito dado, y de los digitos del numero menores al digito dado
#R:numero y digito entero
def divida(dig,num):
    if isinstance(num,int) and isinstance(dig,int) and dig>=0 and dig<=9:
        return divida_aux(dig,abs(num),0,0,0,0)
    else:
        return 'error'

def divida_aux(dig,num,mayores,menores,exp1,exp2):
    if num==0:
        return (mayores,menores)
    elif (num%10-dig)>=0:
        return divida_aux(dig,num//10,mayores+(num%10)*10**exp1,menores,exp1+1,exp2)
    else:
        return divida_aux(dig,num//10,mayores,menores+(num%10)*10**exp2,exp1,exp2+1)

#5
#E:numero y digito
#S:booleano que determine si todos los digitos del numero son divisores exactos del digito 
#R:numero y digito entero
def todos_div(num,dig):
    if isinstance(num,int) and isinstance(dig,int) and dig>=0 and dig<=9:
        return todosdiv_aux(abs(num),dig)
    else:
        return 'error'

def todosdiv_aux(num,dig):
    if num==0:
        return True
    elif (num%10)%dig==0:
        return todosdiv_aux(num//10,dig)
    else:
        return False

    
