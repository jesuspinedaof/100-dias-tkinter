''' Instalacion de Tkinter '''
#importar la libreria de Tk
import tkinter
from tkinter import *
import tkinter as ttk

# Crear la ventana principal
window = Tk()

# Crear un boton con el texto "Hola mundo"
ttk.Button(window, text="Hola mundo").grid() # .grid() es el metodo para mostrar y organizar widgets

# Ejecutar el bucle principal para mantener la ventana activa
window.mainloop()
