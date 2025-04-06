#Giancarlo Vega Marín
#Carne: 2020195338
class Vehiculo:
    def __init__(self,placa,marca,ruedas,kilometraje,combustible,consumo):
        self.placa = placa
        self.marca = marca
        self.ruedas= ruedas
        self.kilometraje = kilometraje
        self.combustible = combustible
        self.consumo = consumo

    def mostrar(self):
        print("Placa: ", self.placa)
        print("Marca: ", self.marca)
        print("Ruedas: ", self.ruedas)
        print("Kilometraje: ", self.kilometraje)
        print("Combustible: ", self.combustible)
        print("Consumo: ", self.consumo)


    def get_kilometraje(self):
        return self.kilometraje
    
    def set_kilometraje(self,kilometraje):
        self.kilometraje = kilometraje
        
    def hacerViaje(self,kms):
        kilometraje=self.kilometraje
        self.kilometraje=kilometraje+kms


class Auto:
    def __init__(self,placa,marca,ruedas,kilometraje,combustible,consumo,modelo,ano):
        Vehiculo.__init__(self,placa,marca,ruedas,kilometraje,combustible,consumo)
        self.modelo = modelo
        self.ano = ano

    def get_kilometraje(self):
        return self.kilometraje
    
    def mostrar(self):
        Vehiculo.mostrar(self)
        print("Modelo: ", self.modelo)
        print("Año: ", self.ano)
        print("------------------------------")

class Moto:
    def __init__(self,placa,marca,ruedas,kilometraje,combustible,consumo,estilo,cilindraje):
        Vehiculo.__init__(self,placa,marca,ruedas,kilometraje,combustible,consumo)
        self.estilo = estilo
        self.cilindraje = cilindraje

    def get_kilometraje(self):
        return self.kilometraje
        
    def mostrar(self):
        Vehiculo.mostrar(self)
        print("Estilo: ", self.estilo)
        print("Cilindraje: ", self.cilindraje)
        print("------------------------------")  

listavehiculos = [Auto('BFV-771','Toyota',4,15000,120,0.125,'RAV4',2000),Auto('AKL-793','Nissan',4,7500,120,0.125,'NOTE',2007),Auto('VMG-198','Chevrolet',4,30000,120,0.125,'Camaro',2015),
                  Moto('ZKL-016','BMW',2,16000,12,0.04,'Brat',2),Moto('MKS-210','Honda',2,10500,12,0.04,'Chopper',6),Moto('FKN-015','Yamaha',2,2500,12,0.04,'Bobber',4)]
            
def revise(lista):
    for car in lista:
        if car.get_kilometraje()>=10000:
            car.mostrar()

print(revise(listavehiculos))
