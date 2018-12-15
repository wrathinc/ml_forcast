def unique_words(page):
  ''' Returns set of the unique words in list of lines of text

    Example:

    >>> from StringIO import StringIO
    >>> fileText = """the cat sat on the mat
    ... the mat was ondur the cat
    ... one fish two fish red fish
    ... blue fish
    ... This fish has a yellow car
    ... This fish has a yellow star"""
    >>> file = StringIO(fileText)
    >>> page = file.readlines()
    >>> words = unique_words(page)
    >>> print sorted(list(words))
    ["This", "a", "blue", "car", "cat", "fish", "has", "mat", 
     "on", "ondur", "one", "red", "sat", "star", "the", "two", 
     "was", "yellow"]
    >>>
  '''

  return set(word  for line in page  for word in line.split())

def _test():
    import doctest
    doctest.testmod()

if __name__ == "__main__":
    _test()