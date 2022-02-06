""" Method Testing """


import unittest
from unittest import TestCase
from palindrome import is_palindrome
from prime_number import is_prime


class TestingFunctions(TestCase):
    """ Methods Tests """

    def test_is_palindrome(self):
        """ Testing is_palindrome method """
        self.assertEqual(is_palindrome('Anita lava la tina'), True)
        self.assertEqual(is_palindrome('Logra Casillas alli sacar gol'), True)
        self.assertEqual(is_palindrome('Claro que no soy palindromo'), False)
        self.assertEqual(is_palindrome('Esto tampoco es un palindromo'), False)
        self.assertEqual(is_palindrome('Ana'), True)

    def test_is_prime(self):
        """ Testing is_prime method """
        self.assertEqual(is_prime(7), True)
        self.assertEqual(is_prime(200), False)
        self.assertEqual(is_prime(53), True)
        self.assertEqual(is_prime(23), True)
        self.assertEqual(is_prime(45), False)
        self.assertEqual(is_prime(32), False)
        self.assertEqual(is_prime(142), False)


if __name__ == '__main__':
    unittest.main()
