import tkinter as tk
from threading import Thread
import random
import time

#Colores
iridium = "#3D3C3A"
azureBlue = "#4863A0"
newMidnightBlue = "#0000A0"
oakBrown = "#806517"
paleta = [iridium, azureBlue, newMidnightBlue, oakBrown]

#Ventana
def ventana():
    ventanaPrincipal = tk.Tk()
    ventanaPrincipal.title("Ventana HD")
    ventanaPrincipal.minsize(900, 500)
    ventanaPrincipal.maxsize(1080, 1920)

    ventanaPrincipal.configure(background="pink")
    ancho = 600
    largo = 400

    # Canvas Ventana03
    canvasC1 = tk.Canvas(ventanaPrincipal, width=800, height=600, borderwidth=0, highlightthickness=0, bg="black")
    canvasC1.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
    canvasC2 = tk.Canvas(ventanaPrincipal, width=ancho, height=largo, borderwidth=0, highlightthickness=0, bg="#48FF33")
    canvasC2.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

    # Titulos
    tituloAnim = tk.Label(canvasC1, text="Animación", font=("Papyrus", 15),
                          bg="black", fg="white")
    tituloAnim.place(x=500, y=70)

    tituloTaller = tk.Label(canvasC1, text="Taller Interfaz Gráfica", font=("Arial", 15),
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
        bola = Esfera(canvasC2, random.randint(0, 400), random.randint(0, 200), random.randint(25, 225),
                      random.randint(1, 6), random.randint(1, 6), random.choice(paleta))
        bola_thread = Thread(target=bola.mover)
        bola_thread.daemon = True
        bola_thread.start()

    # Botones

    botonAnimPolig = tk.Button(canvasC1, text="Empezar", command=empezar)
    botonAnimPolig.place(x=600, y=537, anchor=tk.S)

    ventanaPrincipal.mainloop() # para que siga viva la ventana
ventana() #super importante
