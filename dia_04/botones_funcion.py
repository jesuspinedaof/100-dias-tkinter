''' Dia 04 | Botones - Funciones '''
# Importación de la libreria Tk
from tkinter import *
from tkinter import ttk
from tkinter import messagebox

'Configuracion de la ventana'
window = Tk() # Ventana principal
window.title("Dia 04 de 100")
window.iconbitmap('./tk.ico') # OPCIONAL
window.geometry("400x300")

'Funciones de los botones'
def mensajeError():
    messagebox.showerror('Error', 'Haz hecho click de error')

def mensajeInfo():
    messagebox.showinfo('Informacion', '¿Que quieres realizar?')

def mensajePrecaucion():
    messagebox.showwarning('Precaucion', '¿Estas seguro de abandonar?')

'Interfaz'
# Texto
titulo = Label(window, text="Botones con funciones", 
               font="Times, 19",bg="#ffffff",fg="#333333")

titulo.pack()

subtitulo = Label(window, text="¡Haz click para ver mensajes de alerta!",
                  font="Times, 15", bg="#ffffff",fg="blue")
subtitulo.pack()

# Botones
btnText1 = Button(window, text="Mensaje 1",
                  bg="red",fg="#ffffff",padx="10",pady="10", 
                  font="Arial, 15", command=mensajeError,
                  cursor="hand2")
btnText1.pack()

btnText2 = Button(window, text="Mensaje 2",
                  bg="blue",fg="#ffffff",padx="10",pady="10", 
                  font="Arial, 15", command=mensajeInfo
                  ,cursor="hand2")
btnText2.pack()

btnText3 = Button(window, text="Mensaje 3",
                  bg="orange",fg="#ffffff",padx="10",pady="10", 
                  font="Arial, 15", command=mensajePrecaucion,
                  cursor="hand2")
btnText3.pack()
window.mainloop()