
s = "Was it a car or a cat I saw?"
s1 = "tab a cat"
import re
def isPalindrome(s):
    s = s.replace(" ", "")
    s = re.sub(r'[^a-zA-Z0-9]', '', s)
    s = s.lower()

    left_pointer = 0
    right_pointer = len(s) - 1
    while left_pointer < right_pointer:
        if s[left_pointer] != s[right_pointer]:
            return False
        left_pointer+=1
        right_pointer-=1
    return True
print(isPalindrome(s1))