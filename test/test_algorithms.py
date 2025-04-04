import unittest
import re
from palindrome_algorithms import algorithms


def normalize(s):
    return re.sub(r'[^a-zA-Z0-9]', '', s).lower()


palindromes = [
    "radar",
    "level",
    "A man a plan a canal Panama",
    "Was it a car or a cat I saw",
    "No 'x' in Nixon",
    "hello",
    "Python",
    "racecar",
    "12321",
    "not a palindrome"
    ""
]

expected_results = [
    True,
    True,
    True,
    True,
    True,
    False,
    False,
    True,
    True,
    False,
    True
]


class PalindromeTests(unittest.TestCase):
    def test_palindromeg(self):
        for i in range(len(palindromes)):
            result = algorithms.palindrome(normalize(palindromes[i]))
            self.assertEqual(result, expected_results[i])

    def test_palindrome_pointers(self):
        for i in range(len(palindromes)):
            result = algorithms.palindrome_pointers(normalize(palindromes[i]))
            self.assertEqual(result, expected_results[i])

    def test_palindrome_recursive(self):
        for i in range(len(palindromes)):
            result = algorithms.palindrome_recursive(normalize(palindromes[i]))
            self.assertEqual(result, expected_results[i])


if __name__ == "__main__":
    unittest.main(verbosity=2)
