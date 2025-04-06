#Examen corregido
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


#Original
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
        return splitaux(num//10,exp+1,newlist,sublist + num%10*10**exp)

# Pregunta 3
print("Pregunta 3:")
print("partir(123029201034)  Correcto: [123,292,1,34] Retorna: ",partir(123029201034))
print("partir(89762931)      Correcto: [89762931]     Retorna: ",partir(89762931))
print("partir(12000000)      Correcto: [12]           Retorna: ",partir(12000000))
print("partir(1200045)       Correcto: [12, 45]       Retorna: ",partir(1200045))
print("------------------------------------------------------------")

print("Pregunta 3:")
print("split(123029201034)  Correcto: [123,292,1,34] Retorna: ",split(123029201034))
print("split(89762931)      Correcto: [89762931]     Retorna: ",split(89762931))
print("split(12000000)      Correcto: [12]           Retorna: ",split(12000000))
print("split(1200045)       Correcto: [12, 45]       Retorna: ",split(1200045))
print("------------------------------------------------------------")
