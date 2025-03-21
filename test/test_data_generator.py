import unittest
from data import data_generator
from data import constants


class TestPalindromeGenerator(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(data_generator.get_random_palindrome_list(0), [])

    def test_small_list(self):
        result = data_generator.get_random_palindrome_list(5)
        self.assertEqual(len(result), 5)

    def test_large_list(self):
        result = data_generator.get_random_palindrome_list(100)
        self.assertEqual(len(result), 100)

    def test_random_palindrome(self):
        self.assertIn(data_generator.get_random_palindrome(), [
            "radar", "level", "madam", "racecar", "refer", "civic", "deified", "redivider", "rotor", "kayak"
        ])


if __name__ == "__main__":
    unittest.main()