''' Dia 05 | Entradas '''
# Importación de la libreria Tk
from tkinter import * 
from tkinter import ttk

'Configuracion de la ventana'
window = Tk() # Ventana principal
window.title("Dia 05 en TKinter")
window.iconbitmap("./tk.ico") # OPCIONAL
window.geometry("400x300")

# Entrada - Input
dato = Entry(window)
dato.pack()

# Bucle principal
window.mainloop()
