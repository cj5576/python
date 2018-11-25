t1=1
t2=1
for i in range(1,22):
	print('%12ld %12ld'%(t1,t2)),
	if i%3==0:
		print()
	t1=t1+t2
	t2=t1+t2
		