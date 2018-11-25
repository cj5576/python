def isPrime(n):
	if n==2:
		return 1
	if n in[1]:
		return 0
	for i in range(2,n):
		if n%i==0:
			return 0
	return 1

def getPrimeList(n):
	l=[]
	if n==1:
		return l
	if n==2:
		l.append(n)
		return l
	for i in range(2,n+1):
		if isPrime(i)==1:
			l.append(i)
	return l

n=int(input("请输入一个正整数："))
print('{}='.format(n),end='')
if n in [1]:
	print('{}='.format(n))
while n not in [1]:
	for i in getPrimeList(n):
		if n%i==0:
			n=int(n/i)
			if n==1:
				print(i)
			else:
				print('{}*'.format(i),end='')
			break
	