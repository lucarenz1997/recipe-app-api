"""

"""

from django.test import SimpleTestCase

from app import calc

class CalcTests(SimpleTestCase):
    def test_add_numbers(self):
        # Tests that two numbers are added together
        self.assertEqual(calc.add(3, 5), 8)

    def test_subtract_numbers(self):
        # Tests that values are subtracted and returned
        self.assertEqual(calc.substract(15,10), 5)
