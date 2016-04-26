def xo(s):
	"""
	better way:
	s = s.lower()
	return s.count("x") == s.count("o")
	"""
	s = s.lower()
	count_x = 0
	count_o = 0
	for ch in s:
		if ch == 'x':
			count_x += 1
		if ch == 'o':
			count_o += 1
	return count_x == count_o
print xo("xxxoo")