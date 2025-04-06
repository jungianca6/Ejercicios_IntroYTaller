#1
"""
Objeto Rectangulo
atributos: base (int)
           altura (int)
metodos:
calculeArea(): calcula area rectangulo
E: lado
S: calcular area rectangulo
R: -
calculePerimetro(): calcula perimetro
E: lado
S: calcular perimetro rectangulo
R: -
"""
class Rectangulo:
    def __init__(self,base,altura):
        self.base=base
        self.altura=altura
    def get_base(self):
        return self.base 
    def set_base(self,base,altura):
        return self.base == base
    def get_altura(self):
        return self.altura
    def set_altura(self,base,altura):
        return self.altura == altura
    def calculeArea(self):
        return (self.base)*(self.altura)
    def calculePerimetro(self):
        return (2*self.base)+(2*self.altura)

listafig=[Rectangulo(10,5),Rectangulo(50,25),Rectangulo(8,12),Rectangulo(2,4),Rectangulo(12,6)]

def calculos(listafig):
    return calculos_aux(listafig)

def calculos_aux(listafig):
    if listafig == []:
        return []
    else:
        return [[listafig[0].calculeArea(),listafig[0].calculePerimetro()]] + calculos_aux(listafig[1:])
print(calculos(listafig))


#2

class Empleado:
    def __init__(self,numero,nombre,salario):
        self.numero=numero
        self.nombre=nombre
        self.salariohora=salario
    #get y set
    def get_numero(self):
        return self.numero 
    def set_numero(self,numero):
        return self.numero==numero
    def get_nombre(self):
        return self.nombre
    def set_nombre(self,nombre):
        return self.nombre == nombre
    def get_salario(self):
        return self.salariohora
    def set_salario(selfsalario):
        return self.salariohora == salario
    #mostrar
    def mostrar(self):
        print("Numero: ", self.numero)
        print("Nombre: ", self.nombre)
        print("Salario: ", self.salariohora)
        print("------------------------------")
    def CalcularSalario(self,horas):
        return self.salariohora * horas

listaemp=[Empleado(25,'Alberto',45),Empleado(40,'Juan',4500)]

def datosempleado(listaemp):
    return datosempleadoaux(listaemp)

def datosempleadoaux(listaemp):
    if listaemp==[]:
        return []
    else:
        return [listaemp[0].mostrar()]+datosempleadoaux(listaemp[1:])

print (datosempleado(listaemp))
#3
class Cuenta:
    def __init__(self,Cedula,Nombre,saldoinicial,debitos,creditos,saldoactual):
        self.Cedula = Cedula
        self.Nombre = Nombre
        self.saldoI = saldoinicial
        self.debitos = debitos
        self.creditos = creditos
        self.saldoF = saldoinicial

    def get_saldoinicial(self):
        return self.saldoI

    def get_saldoactual(self):
        return self.saldoF

    def get_creditos(self):
        return self.creditos
    
    def get_debitos(self):
        return self.debitos

    def mostrar(self):
        print("Cedula: ", self.Cedula)
        print("Nombre: ", self.Nombre)
        print("Saldo inicial: ", self.saldoI)
        print("Debitos: ", self.debitos)
        print("Creditos: ", self.creditos)
        print("Saldo final: ", self.saldoF)
        print("------------------------------")

    def haceDeposito(self,monto):
        self.creditos+=monto
        self.saldoF+=monto

    def haceRetiro(self,monto):
        if self.saldoF!=0:
            self.debitos+=monto
            self.saldoF-=monto
        else:
            return 'sin fondos'

    def estadoCuenta(self):
        print("Saldo inicial: ", self.saldoI)
        print("Debitos: ", self.debitos)
        print("Creditos: ", self.creditos)
        print("Saldo final: ", self.saldoF)
            

    
  




