def comp(txt1, txt2):
	
	if len(txt1) == len(txt2):
		print("same amount of charchters")
		return True
	else: 
		print("not the same amount of charcters")
		return False
		
comp("AB", "CD")


def lessThanOrEqualToZero(num):
	if num > 0:
		print("passed")
		return False
	else:
		print("failed")
		return True 
		
lessThanOrEqualToZero(5)







lists = [1,2,3,4,5,6]
nestlist = [7,8,9,10,11,12]


testf = [''.join(map(str, i)) for i in zip(lists, nestlist)]

print(testf)


def num_to_dashes(num):
	
	for x in num:
		num * 2
	return x



print(num_to_dashes(lists[3]))