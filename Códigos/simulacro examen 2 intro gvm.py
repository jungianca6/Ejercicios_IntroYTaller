"""Simulacro de Examen Parcial #2
Giancarlo Vega Marín
2020195338"""

#Problema 1
#E:lista
#S:cantidad de digitos de cada número
#R:lista de numeros enteros
def cuente_c(lista):
    if isinstance(lista,list):
        return cuenteC_aux(lista,0,[])
    else:
        return 'error'

def cuenteC_aux(lista,i,digitos):
    if i==len(lista):
        return digitos
    elif lista[i]==0:
        return cuenteC_aux(lista,i+1,digitos+[1])
    else:
        return cuenteC_aux(lista,i+1,digitos+[largo(lista[i],0)])

def largo(num,largonum):
    if num==0:
        return largonum
    else:
        return largo(num//10,largonum+1)

#Iterativo
def cuente_i(lista):
    if isinstance(lista,list):
        return cuenteI_aux(lista,[])
    else:
        return 'error'

def cuenteI_aux(lista,digitos):
    largodigitos=0
    for ele in lista:
        if ele==0:
            digitos +=[1]
        else:
            largodigitos=0
            while ele!=0:
                largodigitos+=1
                ele//=10
            digitos += [largodigitos]
    return digitos



#Problema 2
#E:lista
#S:lista de listas, divididas por la aparicion de un cero
#R:lista no nula
def partir_c(lista):
    if isinstance(lista,list):
        return partirCaux(lista,0,[],[])
    else:
        return 'error'

def partirCaux(lista,i,newlist,sublist):
    if i==len(lista):
        return newlist + [sublist]
    elif lista[i]!=0:
        return partirCaux(lista,i+1,newlist,sublist+[lista[i]])
    else:
        return partirCaux(lista,i+1,newlist+[sublist],[])

#Iterativo
def partir_i(lista):
    if isinstance(lista,list):
        return partirIaux(lista,[],[])
    else:
        return 'error'

def partirIaux(lista,newlist,sublist):
    for ele in lista:
        if ele!=0:
            sublist+=[ele]
        else:
            if sublist!=[]:
                newlist+=[sublist]
                sublist=[]
    return newlist+[sublist]

#Problema 3
#E:digito, numero y otro numero
#S:eliminacion del digito por n veces del #2 numero, formando nuevo numero
#R:digitos y numeros enteros
def elimine_n(dig,num,veces):
    if isinstance(dig,int) and isinstance(num,int) and dig>=0 and dig<=9:
        return eliminenaux(dig,abs(num),veces,0,0)
    else:
        return 'error'

def eliminenaux(dig,num,veces,exp,nuevonum):
    while num!=0:
        if (num%10)==dig:
            if veces<=0:
                nuevonum+=(num%10*10**exp)
                num//=10
                exp+=1
            else:
                num//=10
                veces-=1
        else:
            nuevonum+=(num%10*10**exp)
            num//=10
            exp+=1
    return nuevonum



#Versión correcta

            
