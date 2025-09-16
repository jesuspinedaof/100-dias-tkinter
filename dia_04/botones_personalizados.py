''' Dia 04 | Botones - Personalización '''
# Importación de la libreria Tk
from tkinter import *
from tkinter import ttk

'Configuracion de la ventana'
window = Tk() # Ventana principal
window.title("Dia 04 de 100")
window.iconbitmap('./tk.ico') # OPCIONAL
window.geometry("400x300")

'Interfaz'
# Texto
titulo = Label(window, text="Botones personalizados", 
               font="Times, 19",bg="#cfcfcf",fg="#333333")

titulo.pack()

subtitulo = Label(window, text="Haz click en los botones para ver su efecto",
                  font="Times, 15", bg="#cfcfcf",fg="#AF50EA")
subtitulo.pack()

# Botones
'''
Button(
    master=None,             # Widget padre (ventana o frame)
    text="",                 # Texto que aparece en el botón
    command=None,            # Función que se ejecuta al hacer clic
    width=None,              # Ancho del botón (en caracteres)
    height=None,             # Alto del botón (en líneas de texto)
    padx=0,                  # Espacio horizontal interno
    pady=0,                  # Espacio vertical interno
    font=None,               # Fuente del texto (ej. ("Arial", 12, "bold"))
    bg=None,                 # Color de fondo
    fg=None,                 # Color del texto (foreground)
    activebackground=None,   # Color de fondo cuando el botón está activo
    activeforeground=None,   # Color del texto cuando está activo
    relief="raised",         # Estilo del borde: flat, raised, sunken, groove, ridge
    bd=2,                    # Grosor del borde
    state="normal",          # Estado: normal, disabled, active
    image=None,              # Imagen en lugar de texto
    compound="center",       # Combina texto e imagen: top, bottom, left, right, center
    cursor="arrow",          # Tipo de cursor al pasar por encima
    anchor="center",         # Alineación del contenido: n, ne, e, se, s, sw, w, nw, center
    justify="center",        # Justificación del texto: left, center, right
    takefocus=False,         # Si el botón puede recibir foco con Tab
    highlightbackground=None,# Color del borde cuando no tiene foco
    highlightcolor=None,     # Color del borde cuando tiene foco
    highlightthickness=0     # Grosor del borde de foco
'''
btn1 = Button(window, text="Ejemplo 1", font="Times, 15",
              bg="black",fg="red", padx="5", pady="10")
btn1.pack()

btn2 = Button(window, text="Ejemplo 2", font="Times, 15",
              bg="orange",fg="black", bd="2", activebackground="black",activeforeground="orange",
              padx="5", pady="5", cursor="hand2", justify="left")
btn2.pack()

btn3 = Button(window, text="Ejemplo 3", font="Times, 15",
              bg="green",fg="white", bd="5", activebackground="black",activeforeground="green",
              padx="5", pady="5", cursor="crosshair", justify="left")
btn3.pack()

# Bucle principal
window.mainloop()