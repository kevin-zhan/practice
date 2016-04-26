import math
def find_next_square(sq):
    # Return the next square if sq is a square, -1 otherwise
    if float(int(math.sqrt(sq))) == math.sqrt(sq):
    	return math.pow(math.sqrt(sq)+1,2)
    return -1

print find_next_square(121)