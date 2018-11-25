n=input("Please input a number:")
count=0
l=len(n)
for i in range(l):
	count=int(n[i])*(8**(l-i-1))+count
print(count)