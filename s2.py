def is_palindrome(s):
  if len(s) < 2:
    return True
  if s[0]!=s[-1]:
    return False
  else:
    return is_palindrome(s[1:-1])

s = "qakzhkaq"
print(is_palindrome(s))