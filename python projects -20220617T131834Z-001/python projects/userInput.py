
print "<Hellow their welcome to the name recoriding list>"

# convert the user name  to a string so we can store in a varable 
nameArray = []


userInput = str(raw_input("Please enter your name here:"))
raw_input();

def  reset ():
    
	userInput01 = str(raw_input("Please enter your name here:"))
	print userInput01
	print userInput
	raw_input();
	
	if  userInput01.isdigit(): 

		reset();

	elif userInput01.isalpha():
		#userInput = userInput01
		
		nameArray.append(userInput01)

		print nameArray



def  AddaUser():

	if (userInput not in nameArray): 

					nameArray.append(userInput)

					print nameArray


def  checker ():
				
	if (userInput.isalpha()): 
    				
				
    				AddaUser();

	elif(userInput.isdigit()):
					print"Please enter a name"
					reset();
				#raw_input()




checker ();



raw_input();
