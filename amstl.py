sum=input("������һ��������?)
count=0
while True:
	if not sum.isdigit():
		print("������һ�����`)
		sum=input("������һ��������?)
	else:
		lens=len(sum)
		sums=list(sum)
		for i in range(len(sums)):
			count+=int(sum[i])**lens
		if int(sum)==count:
			print("������� %d �ǰ�ķ˹��������"%int(sum))
			
		else:
			print("������� %d ���ǰ�ķ˹������?%int(sum))
		break	 