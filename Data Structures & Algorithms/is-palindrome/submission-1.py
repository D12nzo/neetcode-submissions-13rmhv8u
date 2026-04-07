class Solution:
    def isPalindrome(self, s: str) -> bool:
        a = ''.join(re.split(r'[^a-zA-Z0-9]', s)).lower()
        l = 0
        r = len(a) - 1

        while l < r:
            if a[l] != a[r]:
                return False
            l += 1
            r -= 1

        return True