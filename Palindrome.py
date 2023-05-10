import string

def is_palindrome(s):
    s = ''.join(c for c in s if c not in string.punctuation)
    s = s.lower()
    return s == s[::-1]
s = "A man, a plan, a canal, Panama"
print("Is the string '{}' a palindrome? {}".format(s, is_palindrome(s)))