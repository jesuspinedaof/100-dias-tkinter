''' Dia 03 | Etiquetas - Textos '''
# Importación de la libreria Tk
from tkinter import *

# Vamos a crear una ventana
window = Tk()

'''Para Crear un texto en TK pordemos usar (Label)
Cabe resaltar que label hay que pasarle minímo 2 parametros
Sería donde se va a mostrar [window], y el texto [text=""]. Por último [.pack] visto en el día 02 '''

Label(window, text="Hola mundo").pack()
# Otro metodo asignando el texto a una variable
titulo = Label(window, text="Día 03 de 100 días Tkinter")
titulo.pack()

# Llamamos al bucle principal para mantener la ventana abierta
window.mainloop()

'Deberiamos ver algo así:'