''' Dia 04 | Botones - texto '''
# Importación de la libreria Tk
from tkinter import *
from tkinter import ttk

'Configuracion de la ventana'
window = Tk() # Ventana principal
window.title("Dia 04 de 100")
window.iconbitmap('./tk.ico') # OPCIONAL
window.geometry("400x300")

'Crear boton'
botonClick = Button(window, text="¡Click aquí!")
botonClick.pack() # No olvidar de mostrarlo

# Bucle principal
window.mainloop()
