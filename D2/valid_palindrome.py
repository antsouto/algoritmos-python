"""
125. Valid Palindrome
https://leetcode.com/problems/valid-palindrome/

Uma string é palíndromo quando, ignorando não-alfanuméricos e case,
ela lê igual de frente para trás.

Exemplo: "A man, a plan, a canal: Panama" → True
         "race a car"                     → False

--- v1 ---
Time:  O(n)
Space: O(n)  — aloca string `cleaned` de até n caracteres

--- v2 (two pointers) ---
Time:  O(n)
Space: O(1)  — sem alocação extra, compara in-place
"""


def isPalindrome(s: str) -> bool:
    cleaned = "".join(c.lower() for c in s if c.isascii() and c.isalnum())
    return cleaned == cleaned[::-1]


def isPalindrome_v2(s: str) -> bool:
    l, r = 0, len(s) - 1
    while l < r:
        while l < r and not (s[l].isascii() and s[l].isalnum()):
            l += 1
        while l < r and not (s[r].isascii() and s[r].isalnum()):
            r -= 1
        if s[l].lower() != s[r].lower():
            return False
        l += 1
        r -= 1
    return True

if __name__ == "__main__":
    cases: list[tuple[str, bool]] = [
        ("abacaxi",                          False),
        ("racecar",                          True),
        ("aba",                              True),
        ("a",                                True),
        ("",                                 True),
        ("ab",                               False),
        ("aabbaa",                           True),
        ("A man, a plan, a canal: Panama",   True),
        ("race a car",                       False),
        ("Was it a car or a cat I saw?",     True),
        ("12321",                            True),
        ("12345",                            False),
        ("A1 1a",                            True),
    ]
    for s, expected in cases:
        for fn in (isPalindrome, isPalindrome_v2):
            result = fn(s)
            status = "PASS" if result == expected else "FAIL"
            print(f"[{status}] {fn.__name__}({s!r:42}) = {result} (expected {expected})")
    print("ok")