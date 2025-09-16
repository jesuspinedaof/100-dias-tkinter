''' Dia 04 | Botones - Texto, personalización, comandos
    Para seguir un tutorial en video aquí el link
    del canal de youtube...
    "https://www.youtube.com/playlist?list=PLaZLND08hkc_m9VjyImLZOMIo67SnXNOV"
    
    Clase completa implementando lo aprendido
    Jesús Pineda - Tu amigo programador
'''

# Importación de las librearias utilizadas
from tkinter import *
from tkinter import font # Este lo usaremos para definir algunas fuentes
from tkinter import messagebox

import os
import webbrowser # Utilizada para abrir enlances webs

'Vamos a crear una ventana y sus características'
window = Tk()
window.title("Día 04 de 100 Tkinter")
window.iconbitmap('tk.ico')
window.geometry('500x300')

'Funciones para Redirigir'
def redirigirYoutube():
    webbrowser.open_new("https://www.youtube.com/@tuamigoprogramador_oficial")

def redirigirGithub():
    webbrowser.open_new("https://github.com/jesuspinedaof")

def redirigirFacebook():
    webbrowser.open_new("https://www.facebook.com/Tuamigoprogramador")
    
def redirigirLinktree():
    webbrowser.open_new("https://linktr.ee/jesuspinedaof")


'Interfaz'
# Texto
titulo = Label(window, text="Dia 04 de 100 Tkinter", font="Helvetita, 20",padx="50",pady="20")
titulo.pack()

subtitulo = Label(window, text="Links Sociales", font="helvetita, 17", fg="#007DFB")
subtitulo.pack()

# Botones
btnGithub = Button(window, 
                   text="Github", 
                   font="Helvetita, 12", 
                   bg="#333333",
                   fg="#a9a9a9",
                   padx="20",
                   pady="2",
                   activebackground="#00FBE2",
                   activeforeground="#333333",
                   cursor="hand2",
                   bd="2",
                   command=redirigirGithub)
                    # Llamar a la funcion de redirigirGithub()
btnGithub.pack()

btnFacebook = Button(window, 
                   text="Facebook", 
                   font="Helvetita, 12", 
                   bg="#0080FF",
                   fg="#ffffff",
                   padx="20",
                   pady="2",
                   activebackground="#00FBE2",
                   activeforeground="#333333",
                   cursor="hand2",
                   bd="2",
                   command=redirigirFacebook)
                    # Llamar a la funcion de redirigirFacebook()
btnFacebook.pack()

btnYoutube = Button(window, 
                   text="YouTube", 
                   font="Helvetita, 12", 
                   bg="#FF0000",
                   fg="#ffffff",
                   padx="20",
                   pady="2",
                   activebackground="#00FBE2",
                   activeforeground="#333333",
                   cursor="hand2",
                   bd="2",
                   command=redirigirYoutube)
                    # Llamar a la funcion de redirigirYoutube()
btnYoutube.pack()

btnLinktree = Button(window, 
                   text="Linktree", 
                   font="Helvetita, 12", 
                   bg="#3CFF00",
                   fg="#101010",
                   padx="20",
                   pady="2",
                   activebackground="#00FBE2",
                   activeforeground="#333333",
                   cursor="hand2",
                   bd="2",
                   command=redirigirLinktree)
                    # Llamar a la funcion de redirigirLinktree()
btnLinktree.pack()

# Llamar el bucle principal
window.mainloop()

''' Esto ha sido todo por el día 04. Se sabe que esto es básico pero los primeros
    10 días vamos a ver lo mas básico de tkinter. Ya sabes que puedes ver 
    lo que es los conceptos y guías en video en la lista
    "https://www.youtube.com/playlist?list=PLaZLND08hkc_m9VjyImLZOMIo67SnXNOV"

    Cualquier duda, pregunta, contribución, colaboración o reporte:
    tornioficial@gmail.com
    https://wa.me/584160601607

'''