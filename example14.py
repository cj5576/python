#判断输入参数是否为素数
def isSuShu(m):
	for i in range(2,m):
		if m%i==0:
			return 0
	return 1
#返回小于参数的所有素数列表
def getSuShuList(x):
	lists=[]
	for i in range(2,x+1):
		if isSuShu(i)==1:
			lists.append(i)
	return lists

n=int(input("请输入一个正整数："))
print('{}='.format(n),end=''),
if not isinstance(n,int) or n<=0:
	print("请输入一个正整数！")
elif n in [1]:
	print('{}'.format(n))
while n not in [1]:
	for i in getSuShuList(n):
		if n%i==0:
			n=int(n/i)
			if n==1:
				print(i)
			else:
				print('{}*'.format(i),end=''),
			break