def two_decimal_places(n):
	return round(n+0.00005,2) 
	if n*1000%10 == 5:
		return round(n,2)+0.01
	return round(n,2)

print two_decimal_places(2.67499995)