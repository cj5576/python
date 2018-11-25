def isSuShu(m):
	for i in range(2,m):
		if m%i==0:
			return 0
	return 1
if isSuShu(15)==1:
	print('a')