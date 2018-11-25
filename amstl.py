sum=input("请输入一个正整数?)
count=0
while True:
	if not sum.isdigit():
		print("请输入一个整擿)
		sum=input("请输入一个正整数?)
	else:
		lens=len(sum)
		sums=list(sum)
		for i in range(len(sums)):
			count+=int(sum[i])**lens
		if int(sum)==count:
			print("您输入的 %d 是阿姆斯特朗数！"%int(sum))
			
		else:
			print("您输入的 %d 不是阿姆斯特朗数?%int(sum))
		break	 