''' Dia 05 | Entradas '''
# Importación de la libreria Tk
from tkinter import * 
from tkinter import ttk
from tkinter import font

'Configuracion de la ventana'
window = Tk() # Ventana principal
window.title("Dia 05 en TKinter")
window.iconbitmap("./tk.ico") # OPCIONAL
window.geometry("400x300")

'Interfaz'

# Botones
'''Entry(
    master=None,               # 📦 Contenedor padre (window, frame, etc.)

    # 🎨 Personalización visual
    background=None,           # Color de fondo (alias: bg)
    foreground=None,           # Color del texto (alias: fg)
    font=None,                 # Fuente del texto (ej. ('Arial', 12))
    width=None,                # Ancho del campo en caracteres
    borderwidth=None,          # Grosor del borde (alias: bd)
    relief=None,               # Estilo del borde: flat, sunken, raised, groove, ridge
    highlightcolor=None,       # Color del borde cuando el widget tiene el foco
    highlightbackground=None,  # Color del borde cuando el widget NO tiene el foco
    highlightthickness=None,   # Grosor del borde de enfoque
    insertbackground=None,     # Color del cursor de inserción
    insertborderwidth=None,    # Grosor del borde del cursor de inserción
    insertwidth=None,          # Grosor del cursor de inserción
    selectbackground=None,     # Color de fondo de la selección
    selectforeground=None,     # Color del texto seleccionado
    cursor=None,               # Tipo de cursor al pasar sobre el campo

    # ⚙️ Comportamiento
    show=None,                 # Caracter para ocultar el texto (ej. '*')
    state=None,                # Estado del widget: normal, disabled, readonly
    justify=None,              # Alineación del texto: left, center, right
    takefocus=None,            # Si puede recibir foco con Tab (True/False)
    exportselection=True,      # Si exporta la selección al portapapeles

    # 🔗 Asociación con variables
    textvariable=None,         # Variable StringVar vinculada al contenido

    # 🔍 Validación
    validate=None,             # Tipo de validación: focus, focusin, focusout, key, all, none
    validatecommand=None,      # Función que se llama para validar la entrada
    invalidcommand=None,       # Función que se llama si la validación falla

    # 📜 Desplazamiento
    xscrollcommand=None,       # Comando para vincular con scrollbar horizontal

    # 🏷️ Identificación
    name=None,                 # Nombre interno del widget
    class_=None                # Clase del widget (para temas y estilos)
)'''

titulo = Label(window, text="Iniciar sesion", font="Helvetita, 17")
titulo.pack()

subtitulo = Label(window, text="Usuario", font="Helvetita, 14")
subtitulo.pack()

inputUsuario = Entry(window, state="normal", width="30")
inputUsuario.pack()


subtitulo2 = Label(window, text="Contraseña", font="Helvetita, 14")
subtitulo2.pack()

inputUsuario2 = Entry(window, show="*", font="Courier, 12", 
                      width="25", justify="center", takefocus=True)
inputUsuario2.pack()

# Bucle principal
window.mainloop()
