# python -m pytest test_myClass.py

from myClass import MyClass 

def test_fatorial0():
    assert MyClass.fatorial(0) == 1

def test_fatorial1():
    assert MyClass.fatorial(1) == 1

def test_fatorial_negativo():
    assert MyClass.fatorial(-10) == 0

def test_fatorial4():
    assert MyClass.fatorial(4) == 24

def test_fatorial5():
    assert MyClass.fatorial(5) == 120