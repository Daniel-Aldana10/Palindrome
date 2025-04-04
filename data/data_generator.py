import random
import string
def get_random_palindrome_string(size):
    if size == 0:
        return ""
    half = ''.join(random.choices(string.ascii_lowercase, k=size//2))
    if size % 2 == 0:
        return half + half[::-1]
    else:
        return half + random.choice(string.ascii_lowercase) + half[::-1]



