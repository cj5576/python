#[1,2,3,4,5,6,7,8]
#[1,2,4,5,7,8]
#[2,4,7,8]
#[4,7]
#[7]
#a=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34]
num=int(input("Please input a number:"))
a=[]
for i in range(num):
	a.append(i+1)
n=0
m=0
print(a)
while True:
	l=len(a)
	b=[]
	j=0
	n=m
	if l==2:
		if n==0:
			n=2
	for i in range(1,l+1):		
		if (i+n)%3==0:
			b.append(i-j-1)
			j+=1
			if l-i<3 and l-i>0 and l>3:
				m=l-i
			if i==l and l>3:
				m=0
			if l<3:
				m=i
	if l<3:
		m=0
	print('N=',n)
	for i in range(0,len(b)):
		print(a.pop(b[i]))
	print(a)
	if l==1:
		break
print(a)
		