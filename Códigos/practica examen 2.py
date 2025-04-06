def convertirbinario(num):
    if isinstance(num,int)and esbinario(num):
        return convertirbinarioaux(abs(num),0,0)
    else:
        return 'error'

def convertirbinarioaux(num,decimal,exp):
    if num==0:
        return decimal
    else:
        return convertirbinarioaux(num//10,decimal+(num%10*(2**exp)),exp+1)

def esbinario(num):
    if num==0:
        return True
    elif num%10>1:
        return False
    else:
        return esbinario(num//10)

#-------------------------------------------------
def concatenar(lista):
    if isinstance(lista,list):
        return concatenaraux(lista,[])
    else:
        return 'error'

def concatenaraux(lista,newlista):
    if lista==[]:
        return newlista
    elif isinstance(lista[0],list):
        return concatenaraux(lista[1:],newlista+concatenaraux(lista[0],[]))
    else:
        return concatenaraux(lista[1:],newlista+[lista[0]])
#-----------------------------------
def menor_mayor(lista):
    if isinstance(lista,list):
        return menormayoraux(lista)

def menormayoraux(lista):
    return [menorlista(lista[1:],lista[0]),mayorlista(lista[1:],lista[0])]

def mayorlista(lista,mayor):
    if lista==[]:
        return mayor
    elif lista[0]>mayor:
        return mayorlista(lista[1:],lista[0])
    else:
        return mayorlista(lista[1:],mayor)

def menorlista(lista,menor):
    if lista==[]:
        return menor
    elif lista[0]<menor:
        return menorlista(lista[1:],lista[0])
    else:
        return menorlista(lista[1:],menor)


#-----------------------------
def divide(num1,num2):
    if isinstance(num1,int) and isinstance(num2,int):
        return divideaux(num1,num2,0,0)

def divideaux(num1,num2,coc,res):
    if num1-num2<0:
        return (coc,res+(num1))
    else:
        return divideaux((num1-num2),num2,coc+1,res)

#-----------------------------------------------
def movies(lista):
    if isinstance(lista,list) and maxlista(lista):
        return moviesaux(lista,0,0,0)
    else:
        return 'error'

def moviesaux(lista,jueces,promedio,cine):
    if lista==[]:
        return(jueces,promedio/jueces,cine)
    elif lista[0]>3.5:
        return moviesaux(lista[1:],jueces+1,promedio+lista[0],cine+1)
    else:
        return moviesaux(lista[1:],jueces+1,promedio+lista[0],cine)

def maxlista(lista):
    if lista==[]:
        return True
    if lista[0]>5:
        return False
    else:
        return maxlista(lista[1:])

#-----------------------------------------------------
def partir(num):
    if isinstance(num,int):
        return partiraux(num,0,[],0)
    else:
        return 'error'

def partiraux(num,exp,result,sumanum):
    if num==0:
        return [sumanum]+result
    elif num%10!=0:
        return partiraux(num//10,exp+1,result,sumanum+num%10*10**exp)
    elif sumanum==0:
        return partiraux(num//10,0,[]+result,0)
    else:
        return partiraux(num//10,0,[sumanum]+result,0)

#---------------------------------------------------------------------------
def notas(lista):
    if isinstance(lista,list):
        return notasaux(lista,0,0,mayorlista(lista[1:],lista[0]),menorlista(lista[1:],lista[0]),len(lista))
    else:
        return 'error'
    
def notasaux(lista,notas,promedio,mayorlista,menorlista,largo):
    if lista==[]:
        return [mayorlista,menorlista,notas,promedio/largo]
    elif lista[0]>67.5:
        return notasaux(lista[1:],notas+1,promedio+lista[0],mayorlista,menorlista,largo)
    else:
        return notasaux(lista[1:],notas,promedio+lista[0],mayorlista,menorlista,largo)


def mayorlista(lista,mayor):
    if lista==[]:
        return mayor
    elif lista[0]>mayor:
        return mayorlista(lista[1:],lista[0])
    else:
        return mayorlista(lista[1:],mayor)

def menorlista(lista,menor):
    if lista==[]:
        return menor
    elif lista[0]<menor:
        return menorlista(lista[1:],lista[0])
    else:
        return menorlista(lista[1:],menor) 
#---------------------------------------------------------
def prodescalar(e,v):
    if isinstance(e,int) and isinstance(v,list):
        return escalaraux(e,v,[])
    else:
        return 'error'
def escalaraux(e,v,producto):
    if v==[]:
        return producto
    else:
        return escalaraux(e,v[1:],producto+[e*v[0]])

#--------------------------------------------------
def reemplazo(num):
    if isinstance(num,int):
        return reemplazoaux(num,0,0)
    else:
        return 'error'

def reemplazoaux(num,exp,nuevonum):
    while num!=0:
        if (num%10)%3==0:
            exp+=1
            num//=10
        else:
            nuevonum+=num%10*10**exp
            exp+=1
            num//=10
    return nuevonum
            
#---------------------------------------------
def divisores(num):
    if isinstance(num,int):
        return divisoresaux(num,1,[])
    else:
        return 'error'

def divisoresaux(num,i,div):
    if i==num:
        return div
    elif num%i==0:
        if i==1:
            return divisoresaux(num,i+1,div)
        else:
            return divisoresaux(num,i+1,div+[i])
    elif num==1 or div==[]:
        return 'Es primo'
    else:
        return divisoresaux(num,i+1,div)

def divisoresI(num):
    if isinstance(num,int):
        return divisoresIaux(num,1,[])
    else:
        return 'error'
    
def divisoresIaux(num,i,div):
    while i!=num:
        if num%i==0:
            if i==1:
                return divisoresIaux(num,i+1,div)
            else:
                return divisoresIaux(num,i+1,div+[i])
        else:
            return divisoresIaux(num,i+1,div)
    return div
            
#--------------------------------------------------------
def sololista(lista):
    if isinstance(lista,list):
        return sololista_aux(lista,[])
    else:
        return 'error'
    
def sololista_aux(lista,sololist):
    for ele in lista:
        if isinstance(ele,list):
            sololist+=sololista_aux(ele,[])
        else:
            sololist+=[ele]
    return sololist
            
