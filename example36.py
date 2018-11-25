def isPrime(n):
	if n==1:
		return 0
	if n==2:
		return 1
	for i in range(2,n):
		if n%i==0:
			return 0
	return 1
l=[]
n=0
for i in range(1,101):
	if isPrime(i)==1:
		l.append(i)
		n+=1
print(n)
print(l)
