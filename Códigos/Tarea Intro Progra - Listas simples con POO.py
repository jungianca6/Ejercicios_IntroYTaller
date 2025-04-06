#Giancarlo Vega Marín
#Carne: 2020195338
"""
Clase Nodo - Node:
Atributos:
+ value: int
+ next: referencia
Métodos:
- get_value()
"""
class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.next = None    # referencia al nodo siguiente
    def get_value(self):
        return self.valor

"""
Clase Lista - List:
Atributos:
+ size: int
+ head: referencia
Métodos:
- __len__(): retorna el largo de la lista
- appe(valor): inserta un nodo al final de la lista
E: valor a insertar
S: lista actualizada con nodo al final
R: -
- printL(): muestra el contenido de la lista
- suma(): obtiene la suma de los elementos de la lista en forma iterativa
- suma_r():obtiene la suma de los elementos de la lista en forma recursiva
- cuente_i(valor): cantidad de elementos en la lista iguales al 
valor dado iterativamente
E: valor a insertar
S: cantidad de elementos en la lista iguales al valor dado
R: -
- cuente_r(valor): cantidad de elementos en la lista iguales al 
valor dado recursivamente
E: valor a insertar
S: cantidad de elementos en la lista iguales al valor dado
R: -
- inn(ele): indica si el elemento existe en la lista
E: elemento
S: booleano que indicia si el elemento existe en la lista
R: - 
"""

class Lista:
    def __init__(self):
        self.size = 0    # largo de la lista   
        self.head = None
    def __len__(self):
        return self.size
    def appe(self, valor):
        if isinstance(valor, int):
            self.size += 1
            if self.head == None : # caso 1
                self.head = Nodo(valor)
            else:  # caso 2: lista con elementos
                tmp = self.head
                while tmp.next != None :
                    tmp = tmp.next
                tmp.next = Nodo(valor)
        else:
            print("Error")
    def printL(self): 
        node = self.head
        print("[", end = "")
        while node != None:
            if node.next==None:
                print(node.get_value(),end = "")
                node = node.next
            else:
                print(node.get_value(),end = ", ")
                node = node.next
        return print("]", end="")
    
    def suma(self):
        sumaI=0
        node = self.head
        while node!=None:
            sumaI+=node.get_value()
            node=node.next
        return sumaI
    
    def suma_r(self):
        node= self.head
        return self.sumar_aux(node,0)

    def sumar_aux(self,node,sumaR):
        if node==None:
            return sumaR
        else:
            return self.sumar_aux(node.next,sumaR+node.get_value())

    def cuente_i(self,valor):
        if isinstance(valor,int):
            cuentenum=0
            node = self.head
            while node!=None:
                if node.get_value()==valor:
                    cuentenum+=1
                    node=node.next
                else:
                    node=node.next
            return cuentenum
        else:
            print("Error")
            
    def cuente_r(self,valor):
        node= self.head
        if isinstance(valor,int):
            return self.cuenter_aux(valor,node,0)
        else:
            return 'error'
    def cuenter_aux(self,valor,node,cuentenumR):
        if node==None:
            return cuentenumR
        elif node.get_value()==valor:
            return self.cuenter_aux(valor,node.next,cuentenumR+1)
        else:
            return self.cuenter_aux(valor,node.next,cuentenumR)

    def inn(self,ele):
        node= self.head
        result=False
        while node!=None:
            if ele==node.get_value():
                result=True
                break
            else:
                node= node.next
        return result
    
li = Lista()
li.appe(4)
li.appe(3)
li.appe(2)
li.appe(10)
li.appe(25)
li.appe(8)
li.printL()



