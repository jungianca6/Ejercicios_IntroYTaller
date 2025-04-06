class Camion:
    def __init__(self,placa,estado,viajes):
        self.placa = placa
        self.estado = estado
        self.viajes = viajes
    def get_estado(self):
        return self.estado
    def get_viajes(self):
        return self.viajes
    def hacer_viaje(self):
        self.viajes+=1
        print ("Camión hizo viaje")
    def enviar_reparacion(self):
        self.estado='libre'
        
        
#-------------------------------------------------
class Vuelo:
    def __init__(self,aerolinea,numero,fecha,hora,capacidad,cantidad,estado):
        self.aerolinea=aerolinea
        self.numero=numero
        self.fecha=fecha
        self.hora=hora
        self.capacidad=capacidad 
        self.cantidad=cantidad
        self.estado=estado

    def get_fecha(self):
        return self.fecha

    def get_hora(self):
        return self.hora
    
    def get_capacidad(self):
        return self.capacidad
    
    def get_cantidad(self):
        return self.cantidad

    def set_capacidad(self,capacidad):
        self.capacidad=capacidad
    
    def set_cantidad(self,cantidad):
        self.cantidad=cantidad
    
    def get_estado(self):
        return self.estado

    def actualizar_hora(self,hora):
        self.hora=hora

    
    def mostrar(self):
        print("Aerolinea: ", self.aerolinea)
        print("Numero: ", self.numero)
        print("Fecha: ", self.fecha)
        print("Hora: ", self.hora)
        print("Capacidad: ", self.capacidad)
        print("Cantidad: ", self.cantidad)
        print("Estado: ", self.estado)
        print("------------------------------")

    def actualizar_fecha(self,fecha):
        self.fecha=fecha

    def reserva(self,cantidad):
        if self.capacidad!=0:
            self.cantidad+=cantidad
            self.capacidad-=cantidad
        else:
            return 'no hay espacio'

listavuelos=[Vuelo('NY',5,'23/10/2023','14:00',250,0,'O'),Vuelo('NY',5,'23/11/2023','15:00',250,0,'O'),Vuelo('NY',5,'23/12/2023','17:00',250,0,'O'),
             Vuelo('NY',5,'23/10/2023','7:00',250,0,'O'),Vuelo('NY',5,'23/06/2023','22:00',250,0,'O')]

def busque(lista,fecha):
    for vue in lista:
        if vue.get_fecha()==fecha and vue.get_capacidad()!=0:
            vue.mostrar()
            

"""e=Profesor("1","Jeff","01/02/1990","CE")
e.get_ingreso()[6:]
'1990'
e.get_ingreso()[3:5]
'02'
e.get_ingreso()[0:2]
'01'
"""

#---------------------------------------------------------------------------------------------

class Nodo:
    def __init__(self, valor):
        self.next = None
        self.valor = valor
    def get_value(self):
        return self.valor
        
class Lista:
    def __init__(self):
        self.head = None
        self.tail = None
        self.largo = 0

    def __len__(self):
        return self.largo
        
    def appe(self, valor):
        if isinstance(valor, int):
            self.largo += 1
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

    def dele(self, value):
        if self.head == None:
            return "Lista vacía"
        elif self.head.get_value() == value: # primer nodo
            self.head = self.head.next
            self.largo -= 1
        else:
            exito = False
            tmp = self.head
            while tmp.next != None:
                if tmp.next.get_value() == value:
                    exito = True
                    tmp.next = tmp.next.next
                    self.largo -= 1
                    break
                else:
                    tmp = tmp.next
            if not exito:
                return "Elemento no existe"
    def borrarI(self):
        if self.head==None:
            return 'vacia'
        else:
            self.head = self.head.next
            self.largo-=1
            


    def borrarU(self):
        if self.head==None:
            return 'Vacía'
        elif self.head.next==None:
            self.head = self.head.next
            self.largo-=1
        else:
            tmp=self.head
            while tmp.next!=None:
                if tmp.next.next==None:
                    self.largo-=1
                    tmp.next=tmp.next.next
                else:
                    tmp=tmp.next

    def multi(self):
        node= self.head
        multinum=1
        while node!=None:
            multinum*=node.get_value()
            node=node.next
        return multinum

    def prom(self):
        node=self.head
        promnum=0
        while node!=None:
            promnum+=node.get_value()
            node=node.next
        return promnum/self.largo
    
    def deleall(self, value):
        if self.head == None:   #vacio
            return "Lista vacía"
        elif self.head.get_value() == value: #primer nodo
            self.head = self.head.next
            self.largo -= 1
            tmp = self.head
            while tmp.next != None:
                if tmp.next.get_value() == value:
                    tmp.next = tmp.next.next
                    self.largo -= 1
                else:
                    tmp = tmp.next
        else: #no es primer nodo
            tmp = self.head
            while tmp.next != None:
                if tmp.next.get_value() == value:
                    tmp.next = tmp.next.next
                    self.largo -= 1
                else:
                    tmp = tmp.next
                 
  
li = Lista()
li.appe(4)
li.appe(3)
li.appe(2)
li.appe(10)
li.appe(25)
li.appe(8)
li.printL()

#-----------------------------------------------------------
class Empresa:
    def __init__(self,ubicacion,telefono,dueno,servicios,costos,cantidad):
        self.ubicacion=ubicacion
        self.telefono=telefono
        self.dueno=dueno
        self.servicios=servicios 
        self.costos=costos
        self.cantidad=cantidad

    def get_costo(self):
        return self.costos
    def get_servicio(self):
        return self.servicios

    def mostrar(self):
        print("Ubicacion: ", self.ubicacion)
        print("Telefono: ", self.telefono)
        print("Dueño: ", self.dueno)
        print("Servicios: ", self.servicios)
        print("Costos: ", self.costos)
        print("Cantidad: ", self.cantidad)
        print("------------------------------")

    def ActualizarCosto(self,servicio,costo):
        if self.servicios==servicio:
            self.costos=costo   #solo un =
        else:
            'no existe el servicio'

    def costomasalto(self):
        mayor=self.costos[0]
        i=0
        n=len(self.costos)
        j=0
        while i<n:
            if self.costos[i]>=mayor:
                mayor=self.costos[i]
                j=1
                i+=1
            else:
                i+=1
        return [self.servicios[j],mayor]
    
e=Empresa('chepe','8','rosa',['limpieza','cocina'],[25000,40000],100)

def costomas(lista):
    if isinstance(lista,list):
        return costomasaltoxd(lista,lista[0],1,0,len(lista))
    else:
        'error'

       
def costomasaltoxd(lista,mayor,i,j,n):
    while i<n:
        if lista[i]>=mayor:
            mayor=lista[i]
            j=i
            i+=1
        else:
            i+=1
    return [lista[j],mayor]

#---------------------------------------------------------
class Carro:
    def __init__(self,marca,modelo,kilometraje,ano):
        self.marca=marca
        self.modelo=modelo
        self.kilometraje=kilometraje
        self.ano=ano
    def mostrar(self):
        print("Marca: ", self.marca)
        print("Modelo: ", self.modelo)
        print("Kilometraje: ", self.kilometraje)
        print("Año: ", self.ano)
        print("------------------------------")

    def get_kilometraje(self):
        return self.kilometraje
    def get_marca(self):
        return self.marca
    def get_modelo(self):
        return self.modelo
    def get_ano(self):
        return self.ano
    
    def viaje(self,kms):
        self.kilometraje+=kms

    def estado(self):
        if self.kilometraje>=5000 and self.kilometraje%5000==0:
            return 'Revisión' 
        elif self.kilometraje>100000:
            return 'Fuera Garantía'
        else:
            return 'Normal'

class Nodo:
    def __init__(self,marca,modelo,kilometraje,ano):
        self.next = None
        Carro.__init__(self,marca,modelo,kilometraje,ano)
    def get_kilometraje(self):
        return self.kilometraje
    def get_marca(self):
        return self.marca
    def get_modelo(self):
        return self.modelo
    def get_ano(self):
        return self.ano
    
        
class Lista:
    def __init__(self):
        self.head = None
        self.largo = 0

    def __len__(self):
        return self.largo
        
    def appe(self, marca,modelo,kilometraje,ano):
        if isinstance(ano, int):
            self.largo += 1
            if self.head == None : # caso 1
                self.head = Nodo(marca,modelo,kilometraje,ano)
            else:  # caso 2: lista con elementos
                tmp = self.head
                while tmp.next != None :
                    tmp = tmp.next
                tmp.next = Nodo(marca,modelo,kilometraje,ano)
        else:
            print("Error")

    def printL(self): 
        node = self.head
        print("[", end = "")
        while node != None:
            if node.next==None:
                print("[", end = "")
                print(node.get_marca(),",",node.get_modelo(),",",node.get_kilometraje(),",",node.get_ano(),end = "")
                node = node.next
            else:
                print("[", end = "")
                print(node.get_marca(),",",node.get_modelo(),",",node.get_kilometraje(),",",node.get_ano(),end = "], ")
                node = node.next
        return print("]]", end="")

lc = Lista()
lc.appe('Bmv','351i',0,2018)
   
        


        
        


        

        
