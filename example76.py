def peven(n):
	count=0
	for i in range(2,n+1,2):
		count+=1/i
	return count
def podd(n):
	count=0
	for i in range(1,n+1,2):
		count+=1/i
	return count
def dcall(sf,n):
	s= sf(n)
	return s
n=int(input("Please input a number:"))
if n%2==0:
	print(dcall(peven,n))
else:
	print(dcall(podd,n))