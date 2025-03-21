import random
from data import constants


def get_random_palindrome_list(size):
    palindromes = [
        "radar", "level", "madam", "racecar", "refer", "civic", "deified", "redivider", "rotor", "kayak"
    ]
    non_palindromes = [
        "hello", "python", "world", "computer", "science", "random", "example", "algorithm", "test", "data"
    ]

    words = palindromes + non_palindromes

    if size > len(words):
        words *= (size // len(words)) + 1

    return random.sample(words, size)


def get_random_palindrome():
    palindromes = [
        "radar", "level", "madam", "racecar", "refer", "civic", "deified", "redivider", "rotor", "kayak"
    ]
    return random.choice(palindromes)


