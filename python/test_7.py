#from collections import Counter
def char_freq(message):
	#better way : return Counter(message)
	a = sorted(message)
	temp = ""
	count = {}
	for i in a:
		if temp != i:
			temp = i;
			count[temp] = 1
			continue
		count[temp] += 1
	return count

		
    

print char_freq("I like cats")