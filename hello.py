def hello():
	print("hello world")

hello()

def jia():
	a=input("a:")
	b=input("b:")
	count=int(a)+int(b)
	print("%s"%a, "+ %s"%b," = %d"%count)

jia()

def kebianvar(a,*b):
	print(a)
	for var in b:
		print("kebian:",var)
	return
kebianvar('sfff',2,34,'dsff',44)