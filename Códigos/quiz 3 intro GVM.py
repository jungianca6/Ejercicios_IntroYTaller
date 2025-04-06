#Quiz 3 de Intro
#Giancarlo Vega Marín
#E:numero
#S:lista de numeros donde cada numero se forma con los digitos hasta encontrar un 0. (0 es el punto de corte)
#R:numero entero
"""no puse E,S,y R en el pdf"""

def partir(num):
    if isinstance(num,int):
        return partir_aux(abs(num),[],0,0)
    else:
        return 'error'              #me falto el else: 'error'

def partir_aux(num,result,temporal,exp):
    if num==0:
        if temporal!=0:
            return [temporal]+result
        else:
            return result
    elif num%10!=0:
        return partir_aux(num//10,result,num%10*10**exp+temp,exp+1)
    elif num%10==0:
        if temp==0:
            return partir_aux(num//10,result,0,0)
        else:
            return partir_aux(num//10,[temp]+result,0,0)

        
