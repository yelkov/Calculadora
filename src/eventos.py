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

def pulsarComa(numero_pantalla):
    global añadir_numero

    if añadir_numero and "." not in numero_pantalla.get():
        numero_pantalla.set(numero_pantalla.get()+".")

def pulsarMasMenos(numero_pantalla):
    global añadir_numero

    if añadir_numero:
        if numero_pantalla.get()[0] != "-":
            numero_pantalla.set("-" + numero_pantalla.get())
        else:
            numero_pantalla.set(numero_pantalla.get()[1:])
    else:
        numero_pantalla.set("-")
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
        resultado = sumar(float(primer_operador),float(segundo_operador))
        if resultado.is_integer():
            resultado = int(resultado)
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
        resultado = restar(float(primer_operador),float(segundo_operador))
        if resultado.is_integer():
            resultado = int(resultado)
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
        resultado = dividir(float(primer_operador),float(segundo_operador))
        if resultado.is_integer():
            resultado = int(resultado)
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
        resultado = multiplicar(float(primer_operador),float(segundo_operador))
        if resultado.is_integer():
            resultado = int(resultado)
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

    def realizar_operacion(operacion):
        global primer_operador
        segundo_operador = numero_pantalla.get()
        resultado = operacion(float(primer_operador), float(segundo_operador))
        if resultado.is_integer():
            resultado = int(resultado)
        numero_pantalla.set(resultado)

        resultado = 0
        primer_operador = ""
        return False  

    if primer_operador == "":
        resultado = numero_pantalla.get()
        numero_pantalla.set(resultado)
        resultado = 0
    else:
        if operacion_sumar:
            operacion_sumar = realizar_operacion(sumar)
        elif operacion_restar:
            operacion_restar = realizar_operacion(restar)
        elif operacion_dividir:
            operacion_dividir = realizar_operacion(dividir)
        elif operacion_multiplicar:
            operacion_multiplicar = realizar_operacion(multiplicar)
        


