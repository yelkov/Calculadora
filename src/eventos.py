from .operaciones import *

añadir_numero = True
operacion_sumar = False
operacion_restar = False
operacion_dividir = False
operacion_multiplicar = False
primer_operador = ""
segundo_operador = ""
resultado = 0

def pulsarNumero(tecla_numero, numero_pantalla):
    global añadir_numero
    global primer_operador

    if añadir_numero:
        if numero_pantalla.get() == "0":
            numero_pantalla.set(tecla_numero)
        else:
            numero_pantalla.set(numero_pantalla.get() + tecla_numero)

    elif not añadir_numero:
        if primer_operador == "":
            primer_operador = numero_pantalla.get()
        
        numero_pantalla.set(tecla_numero)
        
        añadir_numero = True

def pulsarSuma(numero_pantalla):
    global añadir_numero
    global operacion_sumar
    global primer_operador
    global segundo_operador
    global resultado

    añadir_numero = False
    operacion_sumar = True

    if primer_operador != "":
        segundo_operador = numero_pantalla.get()
        resultado = sumar(int(primer_operador),int(segundo_operador))
        numero_pantalla.set(resultado)

        primer_operador = ""

def pulsarResta(numero_pantalla):
    global añadir_numero
    global operacion_restar
    global primer_operador
    global segundo_operador
    global resultado

    añadir_numero = False
    operacion_restar = True

    if primer_operador != "":
        segundo_operador = numero_pantalla.get()
        resultado = restar(int(primer_operador),int(segundo_operador))
        numero_pantalla.set(resultado)

        primer_operador = ""

def pulsarDivision(numero_pantalla):
    global añadir_numero
    global operacion_dividir
    global primer_operador
    global segundo_operador
    global resultado

    añadir_numero = False
    operacion_dividir = True

    if primer_operador != "":
        segundo_operador = numero_pantalla.get()
        resultado = dividir(int(primer_operador),int(segundo_operador))
        numero_pantalla.set(resultado)

        primer_operador = ""

def pulsarMultiplica(numero_pantalla):
    global añadir_numero
    global operacion_multiplicar
    global primer_operador
    global segundo_operador
    global resultado

    añadir_numero = False
    operacion_multiplicar = True

    if primer_operador != "":
        segundo_operador = numero_pantalla.get()
        resultado = multiplicar(int(primer_operador),int(segundo_operador))
        numero_pantalla.set(resultado)

        primer_operador = ""


def pulsarResultado(numero_pantalla):
    global operacion_sumar
    global operacion_restar
    global operacion_dividir
    global operacion_multiplicar
    global primer_operador 
    global segundo_operador
    global resultado

    if primer_operador == "":
        resultado = numero_pantalla.get()
        numero_pantalla.set(resultado)

        resultado = 0

    else:
        if operacion_sumar:
            segundo_operador = numero_pantalla.get()
            resultado = sumar(int(primer_operador),int(segundo_operador))
            numero_pantalla.set(resultado)

            resultado = 0
            primer_operador = ""
            operacion_sumar = False

        elif operacion_restar:
            segundo_operador = numero_pantalla.get()
            resultado = restar(int(primer_operador),int(segundo_operador)) 
            numero_pantalla.set(resultado)

            resultado = 0
            primer_operador = ""
            operacion_restar = False

        elif operacion_dividir:
            segundo_operador = numero_pantalla.get()
            resultado = dividir(int(primer_operador),int(segundo_operador)) 
            numero_pantalla.set(resultado)

            resultado = 0
            primer_operador = ""
            operacion_dividir = False

        elif operacion_multiplicar:
            segundo_operador = numero_pantalla.get()
            resultado = multiplicar(int(primer_operador),int(segundo_operador)) 
            numero_pantalla.set(resultado)

            resultado = 0
            primer_operador = ""
            operacion_multiplicar = False

        


