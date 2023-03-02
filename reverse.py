def reverse(s):
	str1 = ""
	for i in s:
		str1 = i + str1
	return str1

s = "KeralaBlastersFC"

print("The original string is : ", end="")
print(s)

print("The reversed string is : ", end="")
print(reverse(s))
