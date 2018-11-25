n=int(input("Please input a number:"))
while(True):
	if n%2==0:
		print("please input a add number:")
		n=int(input("Please input a number:"))
	else:
		break
s="9"
while(True):
	if int(s)%n==0:
		break
	s+="9"
m=int(s)
print(m,' / ',n,' = ',m/n)