''' Ventanas | Crear, icono, título, tamaño '''

# Importación de la librería
from tkinter import *
from tkinter import ttk

# Ventana principal
windows = Tk()

# Asignamos un nombre a la ventana con [.title]
windows.title('Ventanas en Tkinter')

# Agregamos un icono a la ventana con [.iconbitmap]
windows.iconbitmap('dia_02/tk.ico') 
''' Cabe resaltar que el icono tiene que estar en la ruta exacta
    recomendable ponerlo en una carpeta dentro del archivo .py
    Además "iconbitmap" solo acepta archivos .ico '''

# Establecemos un tamaño a la ventana
windows.geometry('500x300')

# Ejecutamos el bucle principal [.mainloop]. Para mantener la ventana activa
windows.mainloop()
