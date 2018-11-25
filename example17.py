import string
str=input("请输入一个字符串：\n")
l=0
s=0
d=0
o=0
for c in str:
	if c.isalpha():
		l+=1
	elif c.isspace():
		s+=1
	elif c.isdigit():
		d+=1
	else:
		o+=1
print("char=%d,space=%d,digit=%d,other=%d"%(l,s,d,o))