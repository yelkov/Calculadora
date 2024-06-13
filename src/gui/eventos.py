

def pulsarBoton(tecla, numeroPantalla):
    if numeroPantalla.get() == "0":
        numeroPantalla.set(tecla)
    else:
        numeroPantalla.set(numeroPantalla.get() + tecla)