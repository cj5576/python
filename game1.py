import random

num = random.randint(1,100)
guess=0
while True:
	num_input=input("请输入一个1到100的数字：")
	guess+=1
	if not num_input.isdigit():
		print("请输入数字！")
	elif int(num_input)<0 or int(num_input)>=100:
		print("输入的数字必须介于1到100！")
	else:
		if num==int(num_input):
			print("恭喜您猜对了！一共猜了 %d 次"%guess)
			break
		elif num>int(num_input):
			print("您输入的数字小了！")
		elif num<int(num_input):
			print("您输入的数字大了！")
		else:
			print("系统错误，请联系管理员！")
		
		