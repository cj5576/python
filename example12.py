from math import sqrt
h=0
leap=1
for i in range(101,200):
	j=int(sqrt(i))
	for k in range(2,j+1):
		if i%k==0:
			leap=0
			break
	if leap==1:
		print(i)
		h+=1
	leap=1
	
print('The Total is ',h)