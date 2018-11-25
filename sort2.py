def quicksort(nums):
	if len(nums)<=1:
		return nums
	less=[]
	greater=[]
	base=nums.pop()
	
	for x in nums:
		if x<base:
			less.append(x)
		else:
			greater.append(x)
	return quicksort(less)+[base]+quicksort(greater)
	
def main():
	num_list=[5,76,3,-3,-6,88,9,7,-11,-95,6,4,3,-6]
	print(str(num_list))
	print(str(quicksort(num_list)))

main()
	
	
	