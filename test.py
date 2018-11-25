def isSuShu(m):
	for i in range(2,m):
		if m%i==0:
			return 0
	return 1

n=int(input("Please input int:"))

lists=[]
for i in range(2,n+1):
	if isSuShu(i)==1:
		lists.append(i)
print(lists)

