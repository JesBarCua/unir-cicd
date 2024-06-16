import unittest
from unittest.mock import patch
import pytest

from app.calc import Calculator


def mocked_validation(*args, **kwargs):
    return True


@pytest.mark.unit
class TestCalculate(unittest.TestCase):
    def setUp(self):
        self.calc = Calculator()

    # Suma
    def test_add_method_returns_correct_result(self):
        self.assertEqual(4, self.calc.add(2, 2))
        self.assertEqual(0, self.calc.add(2, -2))
        self.assertEqual(0, self.calc.add(-2, 2))
        self.assertEqual(1, self.calc.add(1, 0))

    def test_add_method_fails_with_nan_parameter(self):
        self.assertRaises(TypeError, self.calc.add, "2", 2)
        self.assertRaises(TypeError, self.calc.add, 2, "2")
        self.assertRaises(TypeError, self.calc.add, "2", "2")
        self.assertRaises(TypeError, self.calc.add, None, 2)
        self.assertRaises(TypeError, self.calc.add, 2, None)
        self.assertRaises(TypeError, self.calc.add, object(), 2)
        self.assertRaises(TypeError, self.calc.add, 2, object())

    # Restar
    def test_restar_method_returns_correct_result(self):
        self.assertEqual(0, self.calc.substract(2, 2))
        self.assertEqual(8, self.calc.substract(8, 0))
        self.assertEqual(4, self.calc.substract(2, -2))
        self.assertEqual(-4, self.calc.substract(-5, -1))

    def test_restar_method_fails_with_nan_parameter(self):
        self.assertRaises(TypeError, self.calc.substract, "2", 2)
        self.assertRaises(TypeError, self.calc.substract, 2, "2")
        self.assertRaises(TypeError, self.calc.substract, "2", "2")
        self.assertRaises(TypeError, self.calc.substract, None, 2)
        self.assertRaises(TypeError, self.calc.substract, 2, None)
        self.assertRaises(TypeError, self.calc.substract, object(), 2)
        self.assertRaises(TypeError, self.calc.substract, 2, object())

    # Multiplicar
    def test_multiplicar_method_returns_correct_result(self):
        self.assertEqual(4, self.calc.multiply(2, 2))
        self.assertEqual(0, self.calc.multiply(0, 0))
        self.assertAlmostEqual (7.5, self.calc.multiply(3, 2.5))
        self.assertEqual(-6, self.calc.multiply(3, -2))
        self.assertEqual(-8, self.calc.multiply(-4, 2))

    def test_multiplicar_method_fails_with_nan_parameter(self):
        self.assertRaises(TypeError, self.calc.multiply, "2", 2)
        self.assertRaises(TypeError, self.calc.multiply, 2, "2")
        self.assertRaises(TypeError, self.calc.multiply, "2", "2")
        self.assertRaises(TypeError, self.calc.multiply, None, 2)
        self.assertRaises(TypeError, self.calc.multiply, 2, None)
        self.assertRaises(TypeError, self.calc.multiply, object(), 2)
        self.assertRaises(TypeError, self.calc.multiply, 2, object())

    # Division
    def test_divide_method_returns_correct_result(self):
        self.assertEqual(1, self.calc.divide(2, 2))
        self.assertEqual(0, self.calc.divide(0, 2))
        self.assertAlmostEqual (1.5, self.calc.divide(3, 2))
        self.assertAlmostEqual (5.25, self.calc.divide(10.5, 2))
        self.assertEqual(-5, self.calc.divide(10, -2))
        self.assertEqual(-4, self.calc.divide(-20, 5))
        self.assertEqual(3, self.calc.divide(-6, -2))

    def test_divide_method_fails_with_nan_parameter(self):
        self.assertRaises(TypeError, self.calc.divide, "2", 2)
        self.assertRaises(TypeError, self.calc.divide, 2, "2")
        self.assertRaises(TypeError, self.calc.divide, "2", "2")
        self.assertRaises(TypeError, self.calc.divide, None, 2)
        self.assertRaises(TypeError, self.calc.divide, 2, None)
        self.assertRaises(TypeError, self.calc.divide, object(), 2)
        self.assertRaises(TypeError, self.calc.divide, 2, object())

    def test_divide_method_fails_with_division_by_zero(self):
        self.assertRaises(TypeError, self.calc.divide, 2, 0)
        self.assertRaises(TypeError, self.calc.divide, 2, -0)
        self.assertRaises(TypeError, self.calc.divide, 0, 0)
        self.assertRaises(TypeError, self.calc.divide, "0", 0)

    # Potencia
    def test_potencia_method_returns_correct_result(self):
        self.assertEqual(4, self.calc.power(2, 2))
        self.assertEqual(0, self.calc.power(0, 2))
        self.assertEqual(1, self.calc.power(2, 0))
        self.assertAlmostEqual(0.25, self.calc.power(2, -2))
        self.assertAlmostEqual(0.25, self.calc.power(-2, -2))
        self.assertAlmostEqual(2.15, self.calc.power(10, 1/3), places=2)
        self.assertEqual(-8, self.calc.power(-2, 3))

    def test_potencia_method_fails_with_nan_parameter(self):
        self.assertRaises(TypeError, self.calc.power, "2", 2)
        self.assertRaises(TypeError, self.calc.power, 2, "2")
        self.assertRaises(TypeError, self.calc.power, "2", "2")
        self.assertRaises(TypeError, self.calc.power, None, 2)
        self.assertRaises(TypeError, self.calc.power, 2, None)
        self.assertRaises(TypeError, self.calc.power, object(), 2)
        self.assertRaises(TypeError, self.calc.power, 2, object())

    # Raiz cuadrada
    def test_raiz_cuadrada_method_returns_correct_result(self):
        self.assertEqual(2, self.calc.raiz_cuadrada(4))
        self.assertAlmostEqual(2.24, self.calc.raiz_cuadrada(5), places=2)
        self.assertEqual(0, self.calc.raiz_cuadrada(0))

    def test_raiz_cuadrada_method_fails_with_nan_parameter(self):
        self.assertRaises(TypeError, self.calc.raiz_cuadrada, "2")
        self.assertRaises(TypeError, self.calc.raiz_cuadrada, None)
        self.assertRaises(TypeError, self.calc.raiz_cuadrada, object())

    def test_raiz_cuadrada_numero_negativo(self):
        self.assertRaises(TypeError, self.calc.raiz_cuadrada, -2)
        self.assertRaises(TypeError, self.calc.raiz_cuadrada, -10)

    # Logaritmo base 10
    def test_logaritmo_base10_method_returns_correct_result(self):
        self.assertEqual(1, self.calc.logaritmo_base10(10))
        self.assertEqual(2, self.calc.logaritmo_base10(100))
        self.assertAlmostEqual(1.30, self.calc.logaritmo_base10(20), places=2)
        self.assertAlmostEqual(-1, self.calc.logaritmo_base10(0.1))

    def test_logaritmo_base10_method_fails_with_nan_parameter(self):
        self.assertRaises(TypeError, self.calc.logaritmo_base10, "2")
        self.assertRaises(TypeError, self.calc.logaritmo_base10, None)
        self.assertRaises(TypeError, self.calc.logaritmo_base10, object())

    def test_logaritmo_base10_numero_menor_cero_o_negativo(self):
        self.assertRaises(TypeError, self.calc.logaritmo_base10, 0)
        self.assertRaises(TypeError, self.calc.logaritmo_base10, -2)

if __name__ == "__main__":  # pragma: no cover
    unittest.main()
