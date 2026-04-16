class Solution:
    def isPalindrome(self, s: str) -> bool:
        check = len(s) - 1
        looper = 0
        while looper < check:
            while looper < check and not s[looper].isalnum():
                looper += 1
            while looper < check and not s[check].isalnum():
                check -= 1
            if s[looper].lower() != s[check].lower():
                return False
            check -= 1
            looper += 1
        return True
        