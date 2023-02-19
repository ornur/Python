def IsPalindrome(K):
    digits = []
    while K > 0:
        digits.append(K % 10)
        K = K // 10
    for i in range(len(digits) // 2):
        if digits[i] != digits[-i-1]:
            return False
    return True


'''
count = 0
for K in [12321, 45654, 78987, 24642, 13531, 2468642, 1357531, 9876789, 123454321, 987654321]:
    if IsPalindrome(K):
        count += 1
print(count)
'''