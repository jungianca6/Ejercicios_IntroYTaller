import tkinter as tk
from time import*
from tkinter import messagebox
import random
import time
from threading import Thread
import pygame
from PIL import ImageTk,Image
#start_time=time.time()

#endtime=time.time()
#totaltime= start-end
#Thread(funcion)
#daemon
#@classmethod
#tk.PhotoImage and .pack()

#globaltotal en cada uno, un globalaux para cada funcion

#Colores
Violeta = "#9400D3"
Indigo = "#4B0082"
Azul = "#0000FF"
Verde = "#00FF00"
Amarillo = "#FFFF00"
Naranja = "#FF7F00"
Rojo = "#FF0000"

paleta = [Violeta,Indigo,Azul,Verde,Amarillo,Naranja,Rojo]

def destruye_ventana(vD,vG):     #entrar y salir               
        """  
        Funcionalidad: Destruye la ventana actual
        Entradas:N/A
        Salidas:N/A
        """
        vG.deiconify()
        vD.destroy()


start_time=time.time() #time
endtime=time.time()
totaltime= start_time-endtime

#Funciones 

def suma(numero):
    global cont1   
    if not isinstance(numero, int):
        return messagebox.showerror(title="error",message="Lo sentimos no es un numero entero")
    else:
        cont1=0
        return suma_aux(numero)

def suma_aux(numero):            
    global cont1
    if numero == 0:
        return 0
    else:
        cont1 = cont1+1
        return numero%10 + suma_aux(numero//10)
        


def multiplicacion(numero):
    global cont2
    if not isinstance(numero, int):   
        return messagebox.showerror(title="error",message="Lo sentimos no es un numero entero")
    else:
        cont2 = 0
        return multiplicacion_aux(numero)

def multiplicacion_aux(numero):
    global cont2     
    if numero == 0:
        return 1
    else:
        cont2=cont2+1   
        return numero%10 * multiplicacion(numero//10)

 

def par(numero):
    global cont3
    if not isinstance(numero, int):
        return messagebox.showerror(title="error",message="Lo sentimos no es un numero entero")
    else:
        cont3 = 0    
        return par_aux(numero)

def par_aux(numero):
    global cont3 
    if numero  == 0:
        return 0
    elif numero%2==0:
        cont3=cont3+1
        return 1 + par(numero//10)
    else:
        cont3=cont3+1
        return par(numero//10)

 
     
def impar(numero):
    global cont4
    if not isinstance(numero, int):
        return messagebox.showerror(title="error",message="Lo sentimos no es un numero entero")
    else:
        cont4 = 0    
        return impar_aux(numero)

def impar_aux(numero):
    global cont4 
    if numero  == 0:
        return 0
    elif numero%2==0:
        cont4=cont4+1
        return 1 + par(numero//10)
    else:
        cont4+1
        return par(numero//10)

#Ventana Principal

def window():
    ventana = tk.Tk()
    ventana.title("menu")
    ventana.minsize(600, 220)
    ventana.maxsize(600, 220)

    ventana.configure(background="light blue")
    ancho = 600
    largo = 400
    
    def analisis_numerico():

 
        analisisNumerico= tk.Toplevel() #se genera la pantalla que se muestra para el about
        analisisNumerico.title("Insertar numero con n valores")
        analisisNumerico.minsize(600, 150)
        analisisNumerico.maxsize(600,150)
        analisisNumerico.configure(background="light blue")
    # etiquetas
        numerante=tk.Label(analisisNumerico,text="Inserte el numero a evaluar:")
        numerante.place(x=150,y=20)
    # entradas de texto
        entradaN=tk.Entry(analisisNumerico,width=10)
        entradaN.place(x=350,y=20)
    #--------------------------------------------------
        def analisis_Aux(numero):
            analisisNumeric = tk.Toplevel() #se genera la pantalla que se muestra para el about
            analisisNumeric.title("Insertar numero con n valores")
            analisisNumeric.minsize(600, 250)
            analisisNumeric.maxsize(600,250)
            analisisNumeric.configure(background="light blue")
            #Definiciones de funciones
            sumado=suma(numero)
            producto=multiplicacion(numero)
            pares=par(numero)
            impares=impar(numero)
            contador=cont1+cont2+cont3+cont4
        # etiquetas
            numerante=tk.Label(analisisNumeric,text="La suma es: " + str(sumado))
            numerante.place(x=150,y=20)

            numerante=tk.Label(analisisNumeric,text="El producto es: " + str(producto))
            numerante.place(x=150,y=50)

            numerante=tk.Label(analisisNumeric,text="Cantidad de digitos pares: " + str(pares))
            numerante.place(x=150,y=80)

            numerante=tk.Label(analisisNumeric,text="Cantidad de digitos impares: " + str(impares))
            numerante.place(x=150,y=110)

            numerante=tk.Label(analisisNumeric,text="Cantidad de recursiones: " + str(contador))
            numerante.place(x=150,y=140)

            numerante=tk.Label(analisisNumeric,text="Tiempo de operación: " + str(totaltime))
            numerante.place(x=150,y=170)

        
            
                
            def destruye_ventanal(DE,Di):
                """
                Funcionalidad: Destruye la ventana actual
                Entradas:N/A
                Salidas:N/A
                """
                Di.deiconify()
                DE.destroy()
            ventana.withdraw()
            
            analisisNumeric.protocol('WM_DELETE_WINDOW', lambda:destruye_ventanal(analisisNumeric,analisisNumerico))
            
            volver = tk.Button(analisisNumeric, text="Volver", width=10, command=lambda:destruye_ventanal(analisisNumeric,analisisNumerico))
            volver.place(x=350, y=70)
            
        
        def borrado():
       
            entradaN.delete(0,"end")
        
        def insertar(numero):

            if numero!="" :
                if numero!="":
                    return analisis_Aux(int(numero))
                else:
                    return messagebox.showinfo("Error","no es un numero entero o el numero entero ingresado es menor a 10")
            else:
                return messagebox.showinfo("Error","Debe de rellenar todos los espacios")
                
            
    
        ventana.withdraw()
        
        analisisNumerico.protocol('WM_DELETE_WINDOW', lambda:destruye_ventana(analisisNumerico,ventana))
        
        volver = tk.Button(analisisNumerico, text="Volver", width=10, command=lambda:destruye_ventana(analisisNumerico,ventana))
        volver.place(x=350, y=70)
        borrar=tk.Button(analisisNumerico,text="limpiar", width=10,command=borrado)
        borrar.place(x=250,y=70)
        insertado=tk.Button(analisisNumerico,text="Insertar",width=10,command= lambda:insertar(entradaN.get()))
        insertado.place(x=150,y=70) 


    def Fichapersonal():
        fichapers= tk.Toplevel() #se genera la pantalla que se muestra para el about
        fichapers.title("Ficha personal")
        fichapers.minsize(1000, 700)
        fichapers.maxsize(1000,700)
        fichapers.configure(background="light blue")

        img=ImageTk.PhotoImage(file='giancarlo(1).jpg')
        img1=ImageTk.PhotoImage(file='giancarlo(1).jpg')
        img2=ImageTk.PhotoImage(file='giancarlo(1).jpg')
        
          #-------------------------------------------------------------------
        nombre=tk.Label(fichapers,text="Giancarlo Vega Marin")
        nombre.place(x=30,y=30)
        #-------------------------------------------------------------------
        carnet=tk.Label(fichapers,text="Inserte su carnet")
        carnet.place(x=30,y=80)
        #-------------------------------------------------------------------
        receta=tk.Label(fichapers,text="Receta del pinto:1 Calienta el aceite en una sartén grande y fríe la cebolla y \n el pimiento hasta que estén suaves.\n Agrega los frijoles, bien escurridos,\n y fríe de tres a cinco minutos. Agrega un poco del caldo de cocción, \n si ves que están quedando muy secos. \n Incorpora el arroz y sigue friendo unos tres minutos más agregando un poco más de caldo de frijoles \npara que el gallo pinto no quede muy seco \n y finalmente adorna con culantro picado.")

    
        receta.place(x=10,y=130)  
        #-------------------------------------------------------------------
        imagenI=tk.Label(fichapers,text= "esta esmi foto",image = img)
        imagenI.place(x=30,y=30)
        #-------------------------------------------------------------------
        imagenL=tk.Label(fichapers,text="Hobbies")
        imagenL.place(x=30,y=330)
        #-------------------------------------------------------------------
        grupoM=tk.Label(fichapers,text="METALLICA Y SU GENERO ES ROCK")
        grupoM.place(x=30,y=380)
        #-------------------------------------------------------------------
        imagenG=tk.Label(fichapers,text="correo electronico")
        imagenG.place(x=30,y=430)
        #-------------------------------------------------------------------
        PAparticipante=tk.Label(fichapers,text="pais de origen")
        PAparticipante.place(x=30,y=480)
        #-------------------------------------------------------------------
        Esparticipante=tk.Label(fichapers,text="Estado")
        Esparticipante.place(x=30,y=530)
        #-------------------------------------------------------------------
        Dparticipante=tk.Label(fichapers,text="descripción")
        Dparticipante.place(x=30,y=580)
                    
        ventana.withdraw()
        
        fichapers.protocol('WM_DELETE_WINDOW', lambda:destruye_ventana(fichapers,ventana))

        volver = tk.Button(fichapers, text="Volver", width=10, command=lambda:destruye_ventana(fichapers,ventana))
        volver.place(x=450, y=360)

        

        

        
        ventana.withdraw()
        
        fichapers.protocol('WM_DELETE_WINDOW', lambda:destruye_ventana(fichapers,ventana))

   
        volver = tk.Button(fichapers, text="Volver", width=10, command=lambda:destruye_ventana(fichapers,ventana))
        volver.place(x=900, y=650)


    def Animacion():
        animation= tk.Toplevel() #se genera la pantalla que se muestra para el about
        animation.title("Animacion")
        animation.minsize(900, 500)
        animation.maxsize(1080, 1920)

        animation.configure(background="#00ffc8")

        canvasC1 = tk.Canvas(animation, width=800, height=600, borderwidth=0, highlightthickness=0, bg="black")
        canvasC1.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
        canvasC2 = tk.Canvas(animation, width=ancho, height=largo, borderwidth=0, highlightthickness=0, bg="#87CEEB")
        canvasC2.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

        tituloAnim = tk.Label(canvasC1, text="Colores del Arcoíris", font=("Papyrus", 15),
                              bg="black", fg="#FF7F00")
        tituloAnim.place(x=500, y=70)

        tituloTaller = tk.Label(canvasC1, text="Animación", font=("Arial", 15),
                              bg="black", fg="white")
        tituloTaller.place(x=100, y=80)
        
        class Esfera:

            def __init__(self, canvas, x, y, diam, xVelocidad, yVelocidad, color): # constructor
                self.canvas = canvas # atributo
                self.color = color # atributo
                self.esfera = canvas.create_oval(x, y, diam, diam, fill=color) # atributo
                self.xVelocidad = xVelocidad # atributo
                self.yVelocidad = yVelocidad # atributo

            def mover(self): # metodo
                while True:
                    coordinates = self.canvas.coords(self.esfera)

                    if (coordinates[2] >= (self.canvas.winfo_width()) or coordinates[0] < 0):
                        self.xVelocidad = -self.xVelocidad

                    if (coordinates[3] >= (self.canvas.winfo_height()) or coordinates[1] < 0):
                        self.yVelocidad = -self.yVelocidad

                    self.canvas.move(self.esfera, self.xVelocidad, self.yVelocidad, )

                    time.sleep(0.01)

            def empezar():
                bola = Esfera(canvasC2, 200, 200, 250, random.randint(1, 6), random.randint(1, 6), random.choice(paleta))
                bola_thread = Thread(target=bola.mover)
                bola_thread.daemon = True
                bola_thread.start()

            # Botones

            botonAnimPolig = tk.Button(canvasC1, text="Empezar", command=empezar)
            botonAnimPolig.place(x=300, y=537, anchor=tk.S)

            
       
        ventana.withdraw()
        animation.protocol('WM_DELETE_WINDOW', lambda:destruye_ventana(animation,ventana))

        volver = tk.Button(canvasC1, text="Volver", width=10, command=lambda:destruye_ventana(animation,ventana))
        volver.place(x=600, y=517)

        

        
    analisis=tk.Button(ventana,text="   Analisis de numeros   ",padx=10,pady=10,command=analisis_numerico)
    analisis.place(x=210,y=20)
#---------------------------------------------------------------------------------------------------------------------
    fichaPersonal=tk.Button(ventana,text="        Ficha personal       ",padx=10,pady=10,command=Fichapersonal)
    fichaPersonal.place(x=210,y=80)
#---------------------------------------------------------------------------------------------------------------------
    animacion=tk.Button(ventana,text="            Animacion          ",padx=10,pady=10,command=Animacion)
    animacion.place(x=210,y=140)
    ventana.mainloop()
window()
