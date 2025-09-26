''' Contador de clicks '''

# Librearías principales
from tkinter import *
from tkinter import ttk
from tkinter import font

'Configuración de la ventana'
window = Tk()
window.title("Contador de Clicks")
window.iconbitmap("./tk.ico")
window.geometry("300x200")

'Utilizables'
contador = 0

'Funciones'
def contadorClicks():
    global contador
    contador += 1
    clicks.config(text=f"{contador}")

'Inferfaz'
titulo = Label(window, text="Contador de clicks", font="Times, 19")
titulo.pack()

subtitulo = Label(window, text="Haga pulse el boton para contar los clicks")
subtitulo.pack()

clicks = Label(window, text="0", font="Helvetita, 18")
clicks.pack()

boton = Button(window, text="Click", command=contadorClicks, font="Helvetita, 16",
               fg="white", bg="purple", padx="20")
boton.pack()

# Bucle principal
window.mainloop()