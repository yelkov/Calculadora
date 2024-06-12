import pytest
from src.operaciones.operaciones import *

def test_suma():
    assert sumar(1,2) == 3
    assert sumar(-1,1) == 0
    assert sumar(-1,-1) == -2
    assert sumar(5,0) == 5

def test_resta():
    assert restar(8,5) == 3
    assert restar(3,3) == 0
    assert restar(-2,2) == -4
    assert restar(5,0) == 5

def test_multiplicar():
    assert multiplicar(2,2) == 4
    assert multiplicar(7,1) == 7
    assert multiplicar(5,-3) == -15
    assert multiplicar(5,0) == 0

def test_dividir():
    assert dividir(10,2) == 5
    assert dividir(0,5) == 0
    assert dividir(100,-10) == -10