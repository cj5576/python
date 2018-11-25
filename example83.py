n=input("Please input a number:")
s=4
sum=4
for i in range(2,int(n)+1):
	print(sum)
	if i<=2:
		s*=7
	else:
		s*=8
	sum+=s
print("sum=",sum)