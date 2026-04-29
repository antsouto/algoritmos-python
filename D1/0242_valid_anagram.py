"""
242. Valid Anagram
https://leetcode.com/problems/valid-anagram/

Given two strings s and t, return True if t is an anagram of s.

Time:  O(n)
Space: O(k) — tamanho do alfabeto
"""

from collections import Counter


def is_anagram(s: str, t: str) -> bool:
    return Counter(s) == Counter(t)


if __name__ == "__main__":
    assert is_anagram("anagram", "nagaram") is True
    assert is_anagram("rat", "car") is False
    assert is_anagram("", "") is True
    assert is_anagram("a", "ab") is False
    print("ok")
