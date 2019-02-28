 #python program to shuffle a deck of card using the module random and draw 5 cards

 
import itertools, random


deck = list(itertools.product(range(1,14),['spade','heart','diomond','club']))
 

random.shuffle(deck)


print ("you got:")
for i in range (5):
		print(deck[i][0],"of",deck[i][1])