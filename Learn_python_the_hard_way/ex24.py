'''
print("Let's practice everything.")
print('You\'d need to know \'bout escapes with \\ that do:')
print('\n newlines and \t tabs.')

poem = """
\tThe lovely planted 
cannot discern \n the needs of love 
nor comprehend passion form intuition 
and requires an explanation 
\n\twhhere there is none.
"""


print("-------------------")
print(poem)
print("-------------------")

five = 10 - 2 + 3 - 6
print(f"This should be five: {five}")

def secret_formula(started):
	jelly_beans = started * 500
	jars = jelly_beans / 1000
	crates = jars / 100 
	return jelly_beans, jars, crates 


start_point = 1000
beans, jars, crates = secret_formula(start_point)


# remember that this is another way to format a string.
print("with a starting point of: {}".format(start_point))

#it's just like with a f"" string
print(f"we'd have {beans} beans, {jars} jars, and {crates} crates.")

start_point = start_point / 10

print("We can also do that way:")
formula = secret_formula(start_point)
# this is an easy way to apply a list to a format string
print("We'd have {} beans {} jars, {} creates.".format(*formula))

'''
def break_words(stuff):
	"""This function will break up words for us."""
	words = stuff.split(' ')
	return words 

def sort_words(words):
	"""Sort the words."""
	return sorted(words)

def print_first_word(words):
	"""Prints the first word after popping it off."""
	word = words.pop(0)
	print(word)

def print_last_word(words):
	"""Prints the last word after poppig if off."""
	word = words.pop(-1)
	print(word)

def print_sort_sentence(sentence):
	"""Takes in a full sentence and returns the sorted words."""
	words = break_words(sentence)
	return sort_words(words)

def print_first_and_last(sentence):
	"""Prints the first and last words of the sentence."""
	words = break_words(sentence)
	print_first_words(words)
	print_last_words(words)

def print_first_and_last_sorted(sentence):
	"""Sorts the words then prints the first and last one."""
	words = sort_sentence(sentence)
	print_first_word(words)
	print_last_word(words)