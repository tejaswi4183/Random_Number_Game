import pyfiglet
import random
z=1
while(z):
	name=input("Enter Your Name : ")
	pyfiglet.print_figlet("WELCOME TO THE GAME")
	pyfiglet.print_figlet(name)
	print("\n*******************RULES*********************\n\n --> U HAVE 3 CHOICES \n --> WITHIN THREE CHOICES YOU GUESS THE CORRECT ONE THAN YOU WON THE GAME \n 3.IF YOU DID'T GUESS THE NUMBER YOU LOSE THE GAME\n\n******ALL THE BEST",end=" ")
	print(name,"*********\n")
	flag=0
	i=1
	

	print("\t SELECT LEVEL \n\n 1.LOW --> Range 1-10 \n 2.MEDIUM --> Range 1-25 \n 3.HIGH --> Range 1-50\n")
	choice=int(input("Enter Your Choice :"))
	if(choice==1):
		while i<=3:
			a=random.randint(1,10)
			b=int(input("Enter Number : "))
			print("Random Number is : ", a,"\n")
			if(a==b):
				pyfiglet.print_figlet("YOU WIN")
				pyfiglet.print_figlet(name)
				flag=10
				break
			else:
				i=i+1
		if(flag==0):
			pyfiglet.print_figlet("YOU LOSE")
			pyfiglet.print_figlet(name)
	elif(choice==2):
		while i<=3:
			a=random.randint(1,25)
			b=int(input("Enter Number : "))
			print("Random Number is : ", a,"\n")
			if(a==b):
				pyfiglet.print_figlet("YOU WIN")
				pyfiglet.print_figlet(name)
				flag=10
				break
			else:
				i=i+1
		if(flag==0):
			pyfiglet.print_figlet("YOU LOSE")
			pyfiglet.print_figlet(name)
	elif(choice==3):
		while i<=3:
			a=random.randint(1,25)
			b=int(input("Enter Number : "))
			print("Random Number is : ", a,"\n")
			if(a==b):
				pyfiglet.print_figlet("YOU WIN")
				pyfiglet.print_figlet(name)
				flag=10
				break
			else:
				i=i+1
		if(flag==0):
			pyfiglet.print_figlet("YOU LOSE")
			pyfiglet.print_figlet(name)
	else:
		print("Enter Correct Choice")
	z=int(input("Do You Want To Play Again Enter Any Key Otherwise Enter 0"))
