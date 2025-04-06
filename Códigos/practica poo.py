class Nodo:
    def __init__(self, nombre, nota):
        self.next = None
        self.nombre = nombre
        self.nota = nota
    def get_nota(self):
        return self.nota
    def get_nombre(self):
        return self.nombre

class Lista:
    def __init__(self):
        self.head = None
        self.largo = 0
        
    def __len__(self):
        return self.largo
    
    def appe(self, nombre,nota):
        if isinstance(nota, int):
            self.largo += 1
            if self.head == None : # caso 1
                self.head = Nodo(nombre,nota)
            else:  # caso 2: lista con elementos
                tmp = self.head
                while tmp.next != None :
                    tmp = tmp.next
                tmp.next = Nodo(nombre,nota)
        else:
            print("Error")
             
    def printL(self): 
        node = self.head
        print("[", end = "")
        while node != None:
            if node.next==None:
                print("[", end = "")
                print(node.get_nombre(),",",node.get_nota(),end = "")
                node = node.next
            else:
                print("[", end = "")
                print(node.get_nombre(),",",node.get_nota(),end = "], ")
                node = node.next
        return print("]]", end="")

    def borrar(self,valor):
        if self.head==None:
            return 'Vacía'
        elif self.head.get_nombre() == valor: # primer nodo
            self.head = self.head.next
            self.largo -= 1
        else:
            exito = False
            tmp = self.head
            while tmp.next != None:
                if tmp.next.get_nota() == valor:
                    exito = True
                    tmp.next = tmp.next.next
                    self.largo -= 1
                    break
                else:
                    tmp = tmp.next
            if not exito:
                return "Elemento no existe"
        
        
    
li = Lista()
li.appe('Andres',6)
li.appe('Esteban',9)
li.appe('Jose',60)


#-----------------------------------------------------------------
  
