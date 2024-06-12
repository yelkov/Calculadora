import tkinter as tk

def iniciar_interfaz():

#Configuramos la raíz de la interfaz
    raiz = tk.Tk()
    raiz.title("Calculadora de Yelko")
    raiz.iconbitmap(r"imagenes\\logo.ico")
    raiz.config(bg="lightgrey") #fondo gris claro

#configuramos el frame principal
    frame = tk.Frame(raiz)
    frame.pack()

#=========== PANTALLA ===============
    numeroPantalla = tk.StringVar()

    pantalla = tk.Entry(frame,width=60,textvariable=numeroPantalla, font=32)
    pantalla.grid(row=1,column=0,pady=20,columnspan=4)
    pantalla.config(bg="black",fg="#03f943",justify="right")
    pantalla.insert(0,"0")

    raiz.mainloop()


iniciar_interfaz()