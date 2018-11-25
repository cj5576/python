a=[]
while True:
	n=input("Please input a number:")
	if n.isdigit():
		a.append(int(n))
	else:
		break
print(a)
max=a[0]
min=a[0]
l=len(a)
print(l)
for i in range(0,l):
	if max<a[i]:
		max=a[i]
		print('max',max)
	if min>a[i]:
		min=a[i]
		print('min',min)
a[0]=max
a[l-1]=min
print(a)
m=input("please input the move times:")
if m.isdigit():
	for i in range(0,int(m)):
		temp=a[l-1]
		for j in range(l-1,0,-1):
			a[j]=a[j-1]
		a[0]=temp
print(a)