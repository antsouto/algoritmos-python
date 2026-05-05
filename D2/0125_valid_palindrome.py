"""
125. Valid Palindrome
https://leetcode.com/problems/valid-palindrome/

A phrase is a palindrome if, after converting all uppercase letters into
lowercase letters and removing all non-alphanumeric characters, it reads
the same forward and backward.

Time:  O(?)
Space: O(?)
"""


def is_palindrome(s: str) -> bool:
    l = 0
    r = len(s)-1
    while l < r:
        while l < r and not s[l].isalnum() :
            l += 1
        while l < r and not s[r].isalnum() :
            r -= 1
        if s[l].lower() != s[r].lower():
            return False
        l += 1
        r -= 1
    return True


def test_is_palindrome() -> None:
    assert is_palindrome("A man, a plan, a canal: Panama") == True
    assert is_palindrome("race a car") == False
    assert is_palindrome(" ") == True
