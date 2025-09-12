''' Dia 03 | Etiquetas - Personalización '''
# Importación de la libreria Tk
from tkinter import *

# Vamos a crear una ventana
window = Tk()

''' Para personaliza etíquetas utilizaremos los metodos de parametros
    que [Label], contiene'''
# Parametros de Label
#[root]: Este sería la ventana donde se va a mostrar
#[text]: Asignar el texto que va a mostrar la etíqueta
#[fg]: Color de texto
#[bg]: Color de fondo
#[font]: Fuente y tamaño
#[padx, pady]: Espaciado interno

titulo = Label(window, 
               text="Etíquetas personalizadas en Tk", 
               fg='#9a9a9a', 
               bg="#333333",
               font="Arial, 16",
               padx=10, pady=10
)
titulo.pack()

# Llamamos al bucle principal para mantener la ventana abierta
window.mainloop()

'Deberiamos ver algo así:'