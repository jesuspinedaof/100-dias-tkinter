''' Dia 03 | Etiquetas - Texto
    Para seguir un tutorial en video aquí el link
    del canal de youtube...
    "https://www.youtube.com/playlist?list=PLaZLND08hkc_m9VjyImLZOMIo67SnXNOV"
    
    Clase completa implementando lo aprendido
    Jesús Pineda - Tu amigo programador
'''

# Importación de la libreria Tk
from tkinter import *
from tkinter import font # Este lo usaremos para definir algunas fuentes

# Vamos a crear una ventana y sus características
window = Tk()
window.title("Día 03 de 100 Tkinter")
window.iconbitmap('tk.ico')
window.geometry('500x300')

# Crear un título y subtitulo
titulo = Label(window, 
               text="Día 3 de 100 Tkinter",
               font="Times, 20",
               fg="#333333")
titulo.pack()

subtitulo = Label(window, text=f"Comandos de texto",bg='red', fg="black", font="Arial, 15")
subtitulo.pack()

# Texto con los parametros - comandos de [Label]
comand = Label(window, font="Courier, 13", bg="black", fg="#2BFF00",pady="10",padx="10", text=
               f"root: Es donde se mostrará el texto\n"
               f"text: Texto al mostrar\n"
               f"fg: Color del texto\n"               
               f"bg: Color del fondo\n"
               f"font: Fuente del texto\n"
               f"padx, pady: Espacio interno\n"

)
comand.pack()

# Ejecutamos el bucle principal
window.mainloop()

''' Esto ha sido todo por el día 03. Se sabe que esto es básico pero los primeros
    10 días vamos a ver lo mas básico de tkinter. Ya sabes que puedes ver lo que es los conceptos y guías en video en la lista
    "https://www.youtube.com/playlist?list=PLaZLND08hkc_m9VjyImLZOMIo67SnXNOV"

    Cualquier duda, pregunta, contribución, colaboración o reporte:
    tornioficial@gmail.com
    https://wa.me/584160601607

'''