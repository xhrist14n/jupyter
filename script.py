import doctest
import unittest

def suma(a,b):
    """
    Funcion de suma de dos numeros
    >>> suma(5,10)
    15
    >>> suma(8,9)
    17
    """
    return a+b

def resta(a,b):
    """
    Funcion de resta de dos numeros
    >>> resta(5,10)
    -5
    """
    return a-b


if __name__ == '__main__':
	doctest.testmod()


class Pruebas(unittest.TestCase):
	def test(self):
		1/0


if __name__ == '__main__':
	unittest.main()
