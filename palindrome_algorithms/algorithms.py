def palindrome(text):
    return text == text[::-1]  # O(n)

def palindrome_pointers(text):
    left, right = 0, len(text)-1  # O(1)
    while left < right:  # O(n)
        if text[left] != text[right]:  # O(1)
            return False  # O(1)
        left += 1  # O(1)
        right -= 1  # O(1)
    return True  # O(1)

def palindrome_recursive(text):
    if len(text) <= 1:  # O(1)
        return True
    if text[0] != text[-1]:  # O(1)
        return False
    return palindrome_recursive(text[1:-1])  # O(n)
