def palindrome(text):
    return text == text[::-1]
def palindrome_pointers(text):
    left, right = 0, len(text)-1
    while left < right:
        if text[left] != text[right]:
            return False
        left += 1
        right-=1
    return True
def palindrome_recursive(text):
    if len(text) <= 1:
        return True
    if text[0] != text[-1]:
        return False
    return palindrome_recursive(text[1:-1])
