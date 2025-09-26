''' Dia 05 | Entradas - Funcinales'''
# Importación de la libreria Tk
from tkinter import * 
from tkinter import ttk
from tkinter import font
from tkinter import messagebox

'Configuracion de la ventana'
window = Tk() # Ventana principal
window.title("Dia 05 en TKinter")
window.iconbitmap("./tk.ico") # OPCIONAL
window.geometry("400x300")

'Funciones'
def guardar_usuario():
    global inputUsuario
    nombre = inputUsuario.get()
    messagebox.showinfo("Información", f"Usuario: {nombre}. Guardado con exito")
    
'Interfaz'
# Texto
titulo = Label(window, text="Día 05 de 100 en tkinter", font="Helvetita, 16")
titulo.pack()

subtitulo = Label(window, text="Guardar datos de [Entry]", font="Helvetita, 13")
subtitulo.pack()

# Botones
'''* METODOS DE ENTRY *
entry.get()                  # Obtener el texto actual del campo
entry.insert(index, text)    # Insertar texto en una posición específica (ej. index=0 para el inicio)
entry.delete(start, end=None)# Eliminar texto desde 'start' hasta 'end' (si no se indica 'end', borra un solo carácter)
entry.select_range(start, end)# Seleccionar texto entre dos posiciones
entry.selection_clear()      # Quitar cualquier selección de texto
entry.selection_present()    # Retorna True si hay texto seleccionado
entry.selection_get()        # Devuelve el texto actualmente seleccionado
entry.index(index)           # Devuelve la posición del índice (ej. 'insert', 'end', etc.)
entry.icursor(index)         # Mueve el cursor de inserción a una posición específica
entry.xview()                # Obtiene la posición de desplazamiento horizontal
entry.xview_scroll(number, what)#↔Desplaza el texto horizontalmente ('units' o 'pages')
entry.xview_moveto(fraction) # Mueve la vista horizontal a una fracción (0.0 a 1.0)
entry.configure(**kwargs)   # Modifica parámetros del widget después de crearlo
entry.cget(option)           # Obtiene el valor de un parámetro (ej. entry.cget("bg"))
entry.focus_set()            # Da el foco al widget
entry.focus_get()            # Devuelve el widget que tiene el foco
entry.after(ms, func)        #⏱Ejecuta una función después de cierto tiempo (ms = milisegundos)
entry.bind(event, handler)   # Asocia eventos (teclado, ratón, etc.) con funciones
entry.unbind(event)          # Elimina una asociación de evento
entry.update()               # Fuerza una actualización inmediata del widget
entry.update_idletasks()     # Actualiza tareas pendientes sin bloquear la interfaz
entry.pack(), place(), grid()# Posicionamiento en la ventana (según el gestor de geometría usado)'''

usuarioText = Label(window, text="Introduzca un nombre de usuario", font="Helvetita, 12")
usuarioText.pack()

inputUsuario = Entry(window, width="27", borderwidth="3", font="Courier, 12",
                     relief="groove", insertbackground="#0073ff",insertwidth="4")
inputUsuario.pack()

btnGuardar = Button(window, text="Guardar usuario", command=guardar_usuario, bg="#0073ff", fg="#ffffff")
btnGuardar.pack()

# Bucle principal
window.mainloop()