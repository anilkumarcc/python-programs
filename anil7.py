import random
l=["r","p","s"]
d={"r":"rock","s":"scissors","p":"paper"}
us=0
cs=0

while True:
	#take input from user

	u=input("enter your choice, press n to discontinue")
	#to exit
	if u=='n':
		print("Game over")
		print("user score",us)
		print("comp score",cs)
		if us==cs:
			print("tie")
		elif us>cs:	
			print("user wins")
		else :
			print("comp wins")	
		exit()
	#input from computer
	c=random.choice(l)
	print("computer chooses",d[c])

	#compare the user and computer choice
	if u == c:
		print("tie")
	elif  u=="r" and c=="p":
		print("comp wins")
		cs=cs+1
	elif u =="r" and c =="s":	
		print("user wins")
		us=us=+1
	elif u=='p' and c=="s":
		print("user wins")
		cs=cs+1
	elif u =='p' and c=="r":
		print("user wins")
		us=us+1
	elif u=='s' and c=='r':
		print("comp wins")
		cs=cs+1
	elif u =='s' and c=="p":
		print("user wins")




