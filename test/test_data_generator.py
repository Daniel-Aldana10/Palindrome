import unittest
from data import data_generator
from data import constants


class TestPalindromeGenerator(unittest.TestCase):
    def test_empty_string(self):
        self.assertEqual(data_generator.get_random_palindrome_string(0), "")

    def test_small_string(self):
        result = data_generator.get_random_palindrome_string(5)
        self.assertEqual(len(result), 5)
        self.assertEqual(result, result[::-1])

    def test_large_string(self):
        result = data_generator.get_random_palindrome_string(100)
        self.assertEqual(len(result), 100)
        self.assertEqual(result, result[::-1])

    def test_random_palindrome(self):
        result = data_generator.get_random_palindrome_string(7)
        self.assertEqual(result, result[::-1])

if __name__ == "__main__":
    unittest.main()