
def sumar(primer_operador, segundo_operador):
    return primer_operador + segundo_operador

def restar(primer_operador, segundo_operador):
    return primer_operador - segundo_operador

def multiplicar(primer_operador,segundo_operador):
    return primer_operador * segundo_operador

def dividir(primer_operador, segundo_operador):
    if segundo_operador == 0:
        raise ValueError("No es posible división por 0.")
    return primer_operador / segundo_operador