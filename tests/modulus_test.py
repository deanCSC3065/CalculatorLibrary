"""
Unit tests for the calculator library
"""

import modulus


class TestCalculator:

    def test_modulus_correct(self):
        assert 1 == modulus.modulus(10, 3)

        


