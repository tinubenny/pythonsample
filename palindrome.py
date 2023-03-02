def isPalindrome(s):
	return s == s[::-1]

s = "malayalam"
ans = isPalindrome(s)

if ans:
	print("yes palindrome")
else:
	print("No palindrome")
