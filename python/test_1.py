def double_char(s):
	result = ""
	for i in s:
		result += i+i
	return result
s = "hello"
print double_char(s)