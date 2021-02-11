# Importando las librerias
from tkinter import*
#Declaracion de variables (operadores de asignacion)
a = 10

#funciones
def ejecutar():
    texto = txt_entrada.get()
    #print("El texto de la caja de texto es: ",texto)
    texto2 = txt_entrada2.get()
    #print("En texto de la caja 2 es", texto2)
    #Convertir el texto de las cajas de texto a numero
    numero1 = float(texto)
    numero2 = float(texto2)

    suma = numero1 + numero2
    suma = round(suma,2)
    sub["text"] =  ("Resultado = " + str(suma))

    print("La suma de los numeros es = ", numero1 + numero2)

    # lIMPIAR LASA CAJITAS DE TEXTO
    txt_entrada.delete(0,END)
    txt_entrada2.delete(0,END)
    # Colocar un cero automaticamente
    txt_entrada.insert(0,"0")
    txt_entrada2.insert(0,"0")

    txt_entrada.focus()





# crear un espacio donde vivira mi aplicacion (Contenedor[screen 1])
screen = Tk() # Crear una screen
screen.geometry("700x500") # Definir el tamaño de la pantalla
screen.resizable(False, False) # Cogelamos la dimension del screen
screen.title("Mi Super App") # Ponemos el titulo
screen.config(bg = "#00A5F7") # Color de fondo de la screen

titulo = Label(screen, text = "Bienvenido a mi App") # crear un Label
titulo.pack(side = TOP) #Ubicamos nuestro texto Arriba, abajo, izquierda y derecha
titulo.config(bg = "#00A5F7", fg = "white", font = ("Corbel",20))

sub = Label(screen, text = "Texto prueba")
sub.place(x = 290, y = 50)
sub.config (bg = "#00A5F7", fg = "white", font = ("Consolas",16), justify = CENTER)

# Crear caja de Texto
txt_entrada = Entry(screen, width = 20, font = ("Consolas",15), fg = "blue")
txt_entrada.place(x=270, y=80)
txt_entrada.config(justify = CENTER) # justify = [CENTER,RIGHT]
txt_entrada.config(state = NORMAL) # state = [NORMAL,  DISABLED]
#txt_entrada.config(show = "*") # Para ocultar las letras cuando escribimos

txt_entrada2 = Entry(screen, width = 20, font = ("Consolas",15), fg = "blue")
txt_entrada2.place(x=270, y=110)
txt_entrada2.config(justify = CENTER) # justify = [CENTER,RIGHT]
txt_entrada2.config(state = NORMAL) # state = [NORMAL,  DISABLED]


# Crear un boton
btn_click = Button(screen, text = "Presioname", width = 15, height = 1)
btn_click.place(x = 280, y = 150)
btn_click.config(bg = "green", fg = "white",font = ("consolas",15), command = ejecutar)

screen.mainloop() #Se mantiene abierta la screen
