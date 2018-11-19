""" dict of brands with keys[size,sheen, color, salses no.]
s
"""

size = ['1qt','1gal','5gal']


#sheen needs to be segmented to diffrent brand types

sheen= ['flat','matte','satin','semi_gloss','low_luster','pearl_finnish','medium_luster','eg_shell']
color= ['Extra White', 'Deep', 'Ultra_Deep']
typepaint = ['Emerald','Duration','Cashmere','Superpaint','Harmony','Proclassico','Proclassicw']

import sherwin_salesnum as ss 

Emerald =     [typepaint[0],size[1:3],sheen[0:4],color,'salesNum']
Duration =    [typepaint[1],size[1:3],sheen[0:4],color,'salesNum']
Cashmere =    [typepaint[2],size[1:3],sheen[0:9][4:7],color,'salesNum']
Superpaint =  [typepaint[3],size[1:3],sheen[0:4],color,'salesNum']
Harmony =     [typepaint[4],size[1:3],sheen[0:4],color,'salesNum']
Proclassicw = [typepaint[5],size[1:3],sheen[0:4],color,'salesNum']
Proclassico = [typepaint[6],size[1:3],sheen[0:4],color,'salesNum']


print("What product would you like?\n")
user1 =  input("type here: ")

#need to eual the  input to all lowercase 
def userinputcheck(x):
	if user1 == typepaint[0]:
		return Emerald
	




def brandgen(x):
	if x == Emerald:
		print("   ",typepaint[0])
		print(f"{size[1]},{sheen[0]},{ss.sherwin(salesNumefl[0])}")
		print("   ",typepaint[0])
		print(f"{size[2]},{sheen[0]},{salesNumefl[1]}")
		print("   ",typepaint[0])
		print(f"{size[1]},{sheen[1]},{salesNumemat[0]}")
		print("   ",typepaint[0])
		print(f"{size[2]},{sheen[1]},{salesNumemat[1]}")
	else:
		print("not done")




brandgen(userinputcheck(user1))





