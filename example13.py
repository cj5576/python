for i in range(100,1000):
	l=list(str(i))
	x=int(l[0])
	y=int(l[1])
	z=int(l[2])
	if x*x*x+y*y*y+z*z*z==i:
		print(i)
