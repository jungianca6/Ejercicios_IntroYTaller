def suma_cocientes(num):
    if isinstance(num,int):
        return cocientesaux(abs(num),1,0)
    else:
        return 'error'

def cocientesaux(num,i,suma):
    if i>num:
        return suma
    else:
        return cocientesaux(num,i+1,suma+(1/(i+1)))
#-----------------------------------------------------

def factorial(num):
    if isinstance(num,int):
        return factorialaux(num,1,1)
    else:
        return 'error'

def factorialaux(num,i,fact):
    if i>num:
        return fact
    else:
        return factorialaux(num,i+1,fact*i)
#-------------------------------------------------------
#Raiz cuadrada
def square_root(num,iteracion):
    if isinstance(num,int)and isinstance(iteracion,int):
        return squarerootaux(abs(num),abs(iteracion),0,1)
    else:
        return 'error'

def squarerootaux(num,iteracion,i,result):
    if i==iteracion:
        return result
    else:
        return squarerootaux(num,iteracion,i+1,1/2*((num/result)+result))
#Euler
def euler(num):
    if isinstance(num,int):
        return euleraux(abs(num),1)
    else:
        return 'error'
def euleraux(num,n,euler):
    if :
        return euler
    else:
        return euleraux(num,n+1,1/1*n
