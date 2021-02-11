from tkinter import*
from tkinter import messagebox
from PIL import*


def pantalla_registro():
    contenedor = Frame(raiz, bg = "white", bd = 10, width = 300, height = 300)
    contenedor.place(x = 50, y= 200)

    lbl_titulo = Label(contenedor, text = "REGISTRO", font = ('Arial',20))
    lbl_titulo.place(relwidth = 1, relheight=0.1)

    lbl_login = Label(contenedor, text="Usuario")
    lbl_login.place(rely = 0.2, relwidth = 0.35, relheight = 0.1)
    txt_usuario = Entry(contenedor)
    txt_usuario.place(relx = 0.4, rely = 0.2, relwidth = 0.55, relheight = 0.1)

    lbl_clave = Label(contenedor, text="Clave")
    lbl_clave.place(rely = 0.4, relwidth = 0.35, relheight = 0.1)
    txt_clave = Entry(contenedor, show = '*')
    txt_clave.place(relx = 0.4, rely = 0.4, relwidth = 0.55, relheight = 0.1)

    btn_registrar = Button(contenedor, text = "Registar", bg = "green", fg = "white", command = lambda: registrar())
    btn_registrar.place(relx = 0.1, rely = 0.6, relwidth = 0.8, relheight = 0.1)

    def registrar():
        usuario = txt_usuario.get()
        clave = txt_clave.get()

        txt_usuario.delete(0,END)
        txt_clave.delete(0,END)

        base = open('baseDatos.txt',"r+")
        #Convertimos los usuarios en una lista
        listaRegistros = base.readlines()
        # Imprimimos los registros
        print(listaRegistros)

        # Creamos una bandera para que nos indique si existe el usuario
        existeUsuario = False

        # vamos a revisar uno a uno los registros
        for registro in listaRegistros:
            # Separamos el registro  actual en usuario registrado y clave registada
            [usuario_registrado,clave_registrado] = registro.split(",")
            print(clave_registrado)

            # Revisamos si el usuario existe
            if usuario == usuario_registrado:
                # Si existe cambiamos el valor de la bandera
                existeUsuario = True
                # Detenemos la revision (Ya encontramos uno que es igual)
                break
      
        # Verificamos si la bandera es True o False
        if existeUsuario == True:
            # Si la bandera es True, queire decir que si hay un registro que ya existe
            messagebox.showinfo("Alerta", "Este usuario ya existe!!")
        else:
            # Si es false registramos el usuario en nuestro archivo
            base.write("%s,%s\n" %(usuario,clave))
            messagebox.showinfo("Mensaje", "El usuario se ha registrado con exito :)")           
        
    
def pantalla_login():

    contenedor = Frame(raiz, bg = "white", bd = 10, width = 300, height = 300)
    contenedor.place(x = 50, y= 200)

    lbl_titulo = Label(contenedor, text = "LOGIN", font = ('Arial',20))
    lbl_titulo.place(relwidth = 1, relheight=0.1)

    lbl_login = Label(contenedor, text="Usuario")
    lbl_login.place(rely = 0.2, relwidth = 0.35, relheight = 0.1)
    txt_login = Entry(contenedor)
    txt_login.place(relx = 0.4, rely = 0.2, relwidth = 0.55, relheight = 0.1)

    lbl_clave = Label(contenedor, text="Clave")
    lbl_clave.place(rely = 0.4, relwidth = 0.35, relheight = 0.1)
    txt_clave = Entry(contenedor, show = '*')
    txt_clave.place(relx = 0.4, rely = 0.4, relwidth = 0.55, relheight = 0.1)

    btn_registrar = Button(contenedor, text = "Login", bg = "blue", fg = "white", command = lambda:Entrar())
    btn_registrar.place(relx = 0.1, rely = 0.6, relwidth = 0.8, relheight = 0.1)

    def Entrar():
        # Obtenemos los datos de las cajas de texto
        usuario = txt_login.get()
        clave = txt_clave.get()

        base = open("baseDatos.txt", "r+")
        listaRegistros = base.readlines()
        
        usuarioCorrecto = False
        for registro in listaRegistros:
            [usuario_registrado, clave_registrado] = registro.split(",")
            clave_registrado = clave_registrado.strip("\n")
            print(clave_registrado)

            if usuario == usuario_registrado and clave == clave_registrado:
                print("Metodo revision")
                usuarioCorrecto = True
                break

        if usuarioCorrecto == True:
            messagebox.showinfo("Mensaje","Bienvenido al sistema")
            Aplicacion()
        else:
            messagebox.showinfo("Alerta","Usuario o clave incorrectos")


def Aplicacion():
    contenedor = Frame(raiz, bg = "white", bd = 10, width = 300, height = 300)
    contenedor.place(x = 50, y= 200)

    lbl_titulo = Label(contenedor, text = "Bienvenidos", font = ('Arial',20))
    lbl_titulo.place(relwidth = 1, relheight=0.1)

#Creamos nuestra pantalla principal
raiz = Tk()
raiz.title("Login")
raiz.geometry("400x600")

# Creamos la base de datos
try:
    baseDatos = open('baseDatos.txt',"r")
    baseDatos.close()
except:
    baseDatos = open('baseDatos.txt',"a")
    print("--- Se ha creado un nuevo archivo ---")
    baseDatos.write("00000,00000\n")
    baseDatos.close()

# Insertar una imagen
#imagen = PhotoImage(file = 'fotos/back.gif')
#imagen_fondo = Label(raiz, image = imagen)
#imagen_fondo.place(relwidth = 1, relheight = 1)


btn_registro = Button(raiz, text = "Registrar", bg = 'gold', width = 15, height = 2,command = pantalla_registro)
btn_registro.place(x=50, y=100)

btn_login = Button(raiz, text = "Login", bg = "gold",width = 15, height = 2,command = pantalla_login)
btn_login.place(x=220, y=100)

raiz.mainloop()
