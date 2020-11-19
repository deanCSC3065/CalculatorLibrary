"""
Unit tests for the calculator library
"""

import calculator


class TestCalculator:

    def test_multiply(self):
        assert 4 == calculator.multiply(2, 2)


    def test_multiply_2(self):
        assert 50 == calculator.add(5, 10)

