#Giancarlo Vega Marín
#Carne: 2020195338
#Tercer Parcial

#Primer problema
"""
Clase Nodo:
Atributos:
+placa
+marca
+modelo
+anio
+next:referencia 
Métodos:
- get_placa()
- get_marca()
- get_modelo()
- get_anio()
"""

class Nodo:
    def __init__(self,placa,marca,modelo,anio):
        self.next = None
        self.placa = placa
        self.marca = marca
        self.modelo = modelo
        self.anio = anio

    def get_placa(self):
        return self.placa
    
    def get_marca(self):
        return self.marca
    
    def get_modelo(self):
        return self.modelo
    
    def get_anio(self):
        return self.anio
"""
Clase Lista:
Atributos:
+ largo: int
+ head: referencia
+ tail

Métodos:
- __len__(): retorna el largo de la lista

- appe(placa,marca,modelo,anio): inserta un nodo al final de la lista
E: valor a insertar
S: lista actualizada con nodo al final
R: -

- printL(): muestra el contenido de la lista

- borrar(placa): elimina el nodo/carro con la misma placa
E: placa a borrar
S: lista actualizada con el nodo borrado
R: -

- indice(i): retorna el valor en la posicion "i"
E: indice
S: valor en el indice dado
R: - 
"""
class Lista:
    def __init__(self):
        self.head = None
        self.tail = None
        self.largo = 0
        
    def __len__(self):
        return self.largo
    
    def appe(self,placa,marca,modelo,anio):
        if isinstance(anio, int):
            self.largo += 1
            if self.head == None : # caso 1
                self.head = Nodo(placa,marca,modelo,anio)
            else:  # caso 2: lista con elementos
                tmp = self.head
                while tmp.next != None :
                    tmp = tmp.next
                tmp.next = Nodo(placa,marca,modelo,anio)
        else:
            print("Error")
             
    def printL(self): 
        node = self.head
        print("[", end = "")
        while node != None:
            if node.next==None:
                print("[", end = "")
                print(node.get_placa(),",",node.get_marca(),",",node.get_modelo(),",",node.get_anio(),end = "")
                node = node.next
            else:
                print("[", end = "")
                print(node.get_placa(),",",node.get_marca(),",",node.get_modelo(),",",node.get_anio(),end = "], ")
                node = node.next
        return print("]]", end="")

    def borrar(self,placa):
        if self.head==None:
            return 'Vacía'
        elif self.head.get_placa() == placa: # primer nodo
            self.head = self.head.next
            self.largo -= 1
        else:
            exito = False
            tmp = self.head
            while tmp.next != None:
                if tmp.next.get_placa() == placa:
                    exito = True
                    tmp.next = tmp.next.next
                    self.largo -= 1
                    break       #break
                else:
                    tmp = tmp.next
            if not exito:
                return "Elemento no existe"
    def indice(self,i):
        node = self.head
        j=0
        result='no hay'
        while node!=None:
            if i==j:
                result = node
                break
            else:
                node=node.next
                j+=1
        return result
    
#Problema 2   
"""
Clase Lista - List:
Atributos:
+ marca
+ ano
+ modelo
+ precio
+ tipo
Métodos:
- get_precio()
- mostrar(): obtiene los valores de la lista de clase

- calculaImpuesto(porcentaje): retorna el impuesto a
pagar segun porcentaje ingresado
E: porcentaje
S: impuesto a pagar segun porcentaje ingresado
R: -

- ActualizaPrecio(nuevoPrecio): actualiza el precio
E: nuevo precio
S: precio actualizado
R: precio actual mayor o igual a 8 digitos

"""
class Carro:
    def __init__(self,marca,ano,modelo,precio,tipo):
        self.marca = marca
        self.ano= ano
        self.modelo = modelo
        self.precio = precio
        self.tipo = tipo

    def get_precio(self):
        return self.precio
    
    def mostrar(self):
        print("------------------------------")
        print("Marca: ", self.marca)
        print("Año: ", self.ano)
        print("Modelo: ", self.modelo)
        print("Precio: ", self.precio)
        print("Tipo: ", self.tipo)
        print("------------------------------")

    def CalculaImpuesto(self,porcentaje):
        self.precio=self.precio*(porcentaje/100)

    def ActualizaPrecio(self,nuevoPrecio):
        if (self.precio-10000000)>=0:
            self.precio=nuevoPrecio
        else:
            return 'no tiene 8 digitos'

listacarros=[Carro('Bugatti',2000,'Chiron',8000000,'Sedán'),
             Carro('BMW',2009,'i3',12000000,'Sedán'),
             Carro('Ferrari',2008,'296',15000000,'Hatchbook'),
             Carro('Ford',2010,'Fiesta',9000000,'Microbus'),
             Carro('Honda',2015,'Civic',22000000,'4x4')]

def MasCaros(lista):
    for car in lista:
        if car.get_precio()>=10000000: #: añadido
            car.mostrar()
            car.CalculaImpuesto(5)

print(MasCaros(listacarros))
             


    

