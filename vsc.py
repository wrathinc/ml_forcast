

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
listnum = [1, 2, 3, 4, 5, 6, 7, 8]
nestlist = [7,8,9,10,11,12]


testf = [''.join(map(str, i)) for i in zip(listnum, nestlist)]

print(testf)



def findSmallestNum(num):
    num.sort() 
    print(num[0],num[-1])

findSmallestNum(listnum)


def calculate_exponet(num, exp):
    print(num**exp)


calculate_exponet(3,5)



def isEvenOrOdd(num):
	if num % 2==0:
		print("{} is Even".format(num))
		
	else:
		print("{} is odd".format(num))
		pass


isEvenOrOdd(7)


def minMax(nums):
	small = min(nums)
	large = max(nums)
	print("this is the smallest: {}".format(small))
	print("this is the largest: {}".format(large))

minMax(listnum)

def char_count(txt1, txt2):
	x = txt1
	y = txt2.count(x)
	print(y)
	return y 


char_count("a", "edaaaaabit")

testlist = "hi edabit fghh abc"

def find_index(lst, txt):
	fi_ind = lst.index(txt)
	print(fi_ind)

find_index(testlist, "fgh")


def my_pi(n):
	import math
	x = round(math.pi,n)
	
	print(x)
	
my_pi(17)  

def mean(lst):
	import math
	nsum = math.fsum(lst)
	nlen = len(lst)
	sdnum = nsum/nlen
	te = round(sdnum,2)
	print(te)


mean(listnum)

def find_digit_amount(num):
	find_amount = len(num)
	print(f"amount in list {find_amount}")


find_digit_amount(listnum)

def count_words(txt):
	find_amount = txt.split(" ")
	c_words = len(find_amount)
	
	print(f"We have {c_words} words in this string!")

count_words(testlist)



def repeat(item, times):
	return([item] * times)

print(repeat(10,5))


def month_name(num):
	months = [
		"easteregg",
		"january",
		"febuary",
		"march",
		"apri",
		"june",
		"may",
		"june",
		"july",
		"august",
		"semptember",
		"october",
		"november",
		"december"
	]

	print(months[num])


	

month_name(1)


def sortNumAsceding(lst):
	lst.sort() 
	print(lst)



sortNumAsceding(listnum)


lstss = ["Ryan", "Kieran", "Jason", "Matt"]

def isFourLetters(lst):
	newlist = []
	for item in reversed(lst):
		if len(item) == 4:
			newlist.append(item)
			newlist.reverse()
		else:
			lst.remove(item)	

	print(newlist)


isFourLetters(lstss)






def isFourLetters(lst):
	ls = []
	for w in lst:
		if len(w) == 4:
			ls.append(w)
	return ls
