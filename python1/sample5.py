a = 8201
b = 3127
c = -1

while c != 0
	c= a % b
	a = b
	b = c
else:
	print(a)
	 