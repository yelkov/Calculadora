import pytest
from src.operaciones import *

def test_suma():
    assert sumar(1,2) == 3
    assert sumar(-1,1) == 0
    assert sumar(-1,-1) == -2