
import colors 
'''
# function for that prints counts of cheese count and boxes of crakers
def cheese_and_crackers(cheese_count, boxes_of_crackers):
	with colors.pretty_output(colors.FG_CYAN) as out:
		out.write(f"\nYou have {cheese_count} cheeses!!")
		out.write(f"you have {boxes_of_crackers} boxes of crackes!!")
		out.write("Man that's enough for a party!")
		out.write("get a blanket. \n")

print("################################################\n")
with colors.pretty_output(colors.BOLD, colors.UNDERSCORE, colors.FG_RED) as out:
	out.write("We can just give the function numbers directly:")
cheese_and_crackers(20, 30)


with colors.pretty_output(colors.BOLD, colors.UNDERSCORE, colors.FG_RED) as out:
	out.write("OR, we can use variables from our script:")

amount_of_cheese = 10
amount_of_crackers = 50

cheese_and_crackers(amount_of_cheese, amount_of_crackers)

with colors.pretty_output(colors.BOLD, colors.UNDERSCORE, colors.FG_RED) as out:
	out.write("We can even do math inside too:")
cheese_and_crackers(10 + 20, 5 + 6)

with colors.pretty_output(colors.BOLD, colors.UNDERSCORE, colors.FG_RED) as out:
	out.write("And we can combine the tow, variables and math:")
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)


'''


def add(a, b):
	print(f"ADDING {a} + {b}")
	return a + b 

def sub(a, b): 
	print(f"SUBTRACTING {a} + {b}")
	return a - b 

def muiltply(a, b):
	print(f"MUILTPLY {a} * {b}")
	return a * b 

def divied(a, b):
	print(f"DIVED {a} / {b}")
	return a / b 

print("Let's do some math with just functions!")

age = add(30,5)
height =sub(78, 4)
weight = muiltply(40,5)
iq = divied(100, 2)

print(f"Age: {age}, Height: {height}, Weight: {weight}, IQ: {iq}")

# A puzzle for the extra credit, type it in anyway. 
print("Here is a puzzle.")

what = add(age, sub(height, muiltply(weight, divied(iq, 2))))

print("That becomes: ", what, "Can you do in by hand?")
