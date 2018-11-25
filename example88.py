i=0
while(True):
	n=int(input("Please input a number,between 1 to 50:"))
	if n>=1 and n<=50:
		i+=1
		print("*"*n)
	if i==7:
		break
