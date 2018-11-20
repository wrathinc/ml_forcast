
ten_things = "youtube.com google.com pythonprogramming.net onemoreurl.com"

stuff = ten_things.split(' ')

more_stuff = ['youtube.com',' google.com']




if len(more_stuff)!=10:
    print("Add another url please!")
    while more_stuff ==False:
         more_stuff.append('new_url.com') 
        


    while len(stuff) != 10:
        next_one = more_stuff.pop()
        print("Adding: ",next_one)
        
        stuff.append(next_one)
        print(f"There are {len(stuff)} items now.") 

print(stuff)

