# Este es un comentario

#Importar las librerias necesarias
from tkinter import*

raiz = Tk()                 # Creamos el screen1
raiz.title("Mi primer app") # Poner titulo a screen1

# Elemntos (widgets)
mensaje = Label(raiz, text = "Hola mundo")
mensaje.pack()

raiz.mainloop() # Para que se muestre la ventana
