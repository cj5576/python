class Hello(object):
	i='caojian'
	
	def __init__(self,name):
		print('init(self,name)')
	def __init__(self):
		print('init(self)')
	
	
myClass=Hello()
print(myClass.i)
