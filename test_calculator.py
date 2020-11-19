"""
Unit tests for the calculator library
"""

import calculator


class TestCalculator:

    def test_multiply(self):
        assert 4 == calculator.multiply(2, 2)

