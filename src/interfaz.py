import tkinter as tk
from .eventos import * 
from .operaciones import *

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
    numero_pantalla = tk.StringVar()

    pantalla = tk.Entry(frame,textvariable=numero_pantalla, font=32)
    pantalla.grid(row=1,column=0,pady=20,columnspan=5)
    pantalla.config(bg="black",fg="#03f943",justify="right")
    pantalla.insert(0,"0")

    #=========== FILA 1 ===============
    botonVacio1 = tk.Frame(frame,width=47,height=40,padx=10,bd=1,relief="groove")
    botonVacio1.grid(row=2,column=1)

    botonAtras = tk.Button(frame,text="←",width=3,padx=10,pady=10,background="lightgrey")
    botonAtras.grid(row=2,column=2)

    botonC = tk.Button(frame,text="C",width=3,padx=7,pady=7,background="#fc7",font="bold")
    botonC.grid(row=2,column=3)

    botonMultiplicar = tk.Button(frame,text="×",width=3,padx=10,pady=10,bg="lightgrey")
    botonMultiplicar.grid(row=2,column=4)

    #=========== FILA 2 ===============
    boton7 = tk.Button(frame,text="7",width=3,padx=10,pady=10,command=lambda:pulsarNumero("7",numero_pantalla))
    boton7.grid(row=3,column=1)

    boton8 = tk.Button(frame,text="8",width=3,padx=10,pady=10,command=lambda:pulsarNumero("8",numero_pantalla))
    boton8.grid(row=3,column=2)

    boton9 = tk.Button(frame,text="9",width=3,padx=10,pady=10)
    boton9.grid(row=3,column=3)

    botonDividir = tk.Button(frame,text="÷",width=3,padx=10,pady=10,bg="lightgrey")
    botonDividir.grid(row=3,column=4)

    #=========== FILA 3 ===============
    boton4 = tk.Button(frame,text="4",width=3,padx=10,pady=10)
    boton4.grid(row=4,column=1)

    boton5 = tk.Button(frame,text="5",width=3,padx=10,pady=10)
    boton5.grid(row=4,column=2)

    boton6 = tk.Button(frame,text="6",width=3,padx=10,pady=10)
    boton6.grid(row=4,column=3)

    botonRestar = tk.Button(frame,text="-",width=3,padx=10,pady=10,bg="lightgrey",command=lambda:pulsarResta(numero_pantalla))
    botonRestar.grid(row=4,column=4)

    #=========== FILA 4 ===============
    boton1 = tk.Button(frame,text="1",width=3,padx=10,pady=10)
    boton1.grid(row=5,column=1)

    boton2 = tk.Button(frame,text="2",width=3,padx=10,pady=10)
    boton2.grid(row=5,column=2)

    boton3 = tk.Button(frame,text="3",width=3,padx=10,pady=10)
    boton3.grid(row=5,column=3)

    botonSumar = tk.Button(frame,text="+",width=3,padx=10,pady=10,bg="lightgrey",command=lambda:pulsarSuma(numero_pantalla))
    botonSumar.grid(row=5,column=4)

    #=========== FILA 5 ===============
    botonMasMenos = tk.Button(frame,text="+/-",width=3,padx=10,pady=10,bg="lightgrey")
    botonMasMenos.grid(row=6,column=1)

    boton0 = tk.Button(frame,text="0",width=3,padx=10,pady=10)
    boton0.grid(row=6,column=2)

    botonComa = tk.Button(frame,text=",",width=3,padx=10,pady=10,bg="lightgrey")
    botonComa.grid(row=6,column=3)

    botonResultado = tk.Button(frame,text="=",width=3,padx=10,pady=10,bg="grey",command=lambda:pulsarResultado(numero_pantalla))
    botonResultado.grid(row=6,column=4)

    #=========== EJECUTAR ===============

    raiz.mainloop()



