''' Dia 05 | Entradas - Texto, personalización, metodos, funciones
    Para seguir un tutorial en video aquí el link
    del canal de youtube...
    "https://www.youtube.com/playlist?list=PLaZLND08hkc_m9VjyImLZOMIo67SnXNOV"
    
    Clase completa implementando lo aprendido
    Jesús Pineda - Tu amigo programador
'''

# Importación de las librearias utilizadas
from tkinter import * 
from tkinter import ttk
from tkinter import font
from tkinter import messagebox

'Configuracion de la ventana'
window = Tk() # Ventana principal
window.title("Dia 05 en TKinter")
window.iconbitmap("./tk.ico") # OPCIONAL
window.geometry("400x300")

'Utilidades'
lista_palabras_clave = []

'Funciones'
def almacenar_palabras_clave():
    palabras = inputTexto.selection_get()
    lista_palabras_clave.insert(0, palabras)
    return

def mostrar_palabras_clave():
    messagebox.showinfo("Palabras claves guardadas", f"Palabras almacenadas: {lista_palabras_clave}")
    
'Interfaz'
# Titulos
titulo = Label(window, text="Dia 05 de 100 en Tkinter", 
               font="Helvetita, 15", padx="5", pady="5")
titulo.pack()

subtitulo = Label(window, text="Guardar palabras claves", font="Helvetita, 14")
subtitulo.pack()

textoInput = Label(window, text="Selecciona palabras claves para guardarlas", font="Times, 12",
                   bg="white", fg="#7703ff", padx="3", pady="3")
textoInput.pack()

inputTexto = Entry(window, font="Courier, 14", width="30", background="black", foreground="#37ff00",
                   insertbackground="#37ff00",insertwidth="3",cursor="hand2", relief="flat", border="10",
                   selectbackground="#37ff00", selectforeground="black")
inputTexto.pack()

btnGuardar = Button(window, text="Guardar palabras clave", font="Courier, 14", command=almacenar_palabras_clave,
                    bg="#7703ff", fg="white", padx="5", pady="5")
btnGuardar.pack()

btnMostrar = Button(window, text="Mostrar palabras clave", font="Courier, 14", command=mostrar_palabras_clave,
                    bg="#7703ff", fg="white", padx="5", pady="5")
btnMostrar.pack()

# Bucle principal
window.mainloop()