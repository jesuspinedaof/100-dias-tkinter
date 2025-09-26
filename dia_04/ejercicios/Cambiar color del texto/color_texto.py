''' Cambiar color del texto '''

# Librerías principales
from tkinter import *
from tkinter import ttk
from tkinter import font
# Librería utilizada para crear selecciones al aleatorias
import random

'Configuración inicial'
window = Tk()
window.title("Cambiar el color de texto")
window.iconbitmap("./tk.ico")
window.geometry("500x300")

'Utilidades'
lista_colores = [
    "blue",
    "red",
    "green",
    "yellow",
    "orange",
    "pink",
    "purple",
    "lime",
    "violet",
    "beige",
    "tan",
    "maroon",
    "gold"
]

color_inicial = "white" # Color por defecto para los texto

'Funciones'
# Esta funcion recibe los colores de la lista, y los muestra de forma aleatoria con random
def cambiarColor(texto):
    cambio_color = random.choice(lista_colores)
    texto.config(fg=cambio_color)
    return

def cambiarTexto1():
    cambiarColor(texto1)

def cambiarTexto2():
    cambiarColor(texto2)
    
def cambiarTexto3():
    cambiarColor(texto3)  
    
'Interfaz'
# Texto
texto1 = Label(window, text="Texto 1", font=("Courier", 17), fg=color_inicial, bg="black", padx="5", pady="5")
texto1.pack()

texto2 = Label(window, text="Texto 2", font=("Courier", 17), fg=color_inicial, bg="black", padx="5", pady="5")
texto2.pack()

texto3 = Label(window, text="Texto 3", font=("Courier", 17), fg=color_inicial, bg="black", padx="5", pady="5")
texto3.pack()

# Botones
boton1 = Button(window, text="Cambiar color Texto 1", command=cambiarTexto1, font="Helvetita, 14")
boton1.pack()

boton2 = Button(window, text="Cambiar color Texto 2", command=cambiarTexto2, font="Helvetita, 14")
boton2.pack()

boton3 = Button(window, text="Cambiar color Texto 3", command=cambiarTexto3, font="Helvetita, 14")
boton3.pack()

# Bucle principal
window.mainloop()