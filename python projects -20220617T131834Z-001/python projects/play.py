# this a python function and checking data types 
#!/usr/bin/env 
import random;
sean01 = 10;  
import time;
import calendar;
ballColors  = ["yellow","bule","red"]

HowLong = len(ballColors)

def  printOut ():

	list (ballColors)
	print ballColors
	print "hellow progammer"
    
	return  

def  Add ():

		ballColors.append("orenage")
		printOut()
		return  

def sean(): 
 
	if (sean01 != 10 ): 

	      print "hellow world new progammer is in town and i am a going to add some stuff to may list"

# calls the add function to append to the gruop 
       	Add()


	if (sean01 == 11):

	  	 	 print "hellow  not progammer"

	  	 	 ballColors.remove("red")

	  		 printOut( )
	  		 return
#	else: 

#		print "can't add any thing to the list"

			

#print("<pressEnter>")


def  Check ():
	
	if ("bule" or "yellow" or "green" in ballColors): 
  
		print "diiferent color_Balls" 

		print HowLong

    	elif ("pink" in ballColors): 
 
    		print "pink_ball"

    	elif ("gray" in ballColors): 

    		print "gray_ball"


	return 

##################################################################################################################

# dictionary 
cumputer = {}

cumputer["brand"] = "hp"
cumputer["color"] = "black"
cumputer["os"] = "windows 7"
cumputer["modle"] = 2012
cumputer["internet_provider"] = "optimum"
cumputer["workig_state"] = True 

def computerData (): 
	if (cumputer["modle"] == 2012): 
		
		print "my computer is a"+ cumputer["os"]+ " modle"

		return        
#################################################################################################################3
"""
UserInput = str(raw_input ("put your name here:"))
print UserInput

def  checker ():

	if (UserInput == "Bean"):


		print "Hellow ".lower()+" Bean".upper()

		return 


print ("<press enter>")
"""
###################################################################################################################

print ballColors[1]

Table_of_Names = ["Dick", "Jhon", "Mark", "Sean"]

print "Sean" in Table_of_Names

sean()
Check()
computerData ()
#checker ()

#raw_input()
####################################################################################################################

pickANumer = random.randint(0, 5)
print pickANumer



DifferentPhones = ["Fire Fox", "Android", "Apple","windows", "Facebook ", "black berry"]


print "my phone is a "+ random.choice (DifferentPhones) +" phone"

####################################################################################################################

for counter in DifferentPhones:

	print counter
#####################################################################################################################


def passingvalues (prams): 

	if (prams):

		print "dog names"

	if (prams == "Jhon") :

		 print "hellow jhon"

	elif (prams == "mike"): 

			print "mike"

			return   


passingvalues("mike")


dayTime = time.time()

print "today time is ",dayTime

localtime = time.localtime(time.time())
print "Local current time :", localtime

'''
def  multiply (number):
	print "4"
	return number*2 
	
multiply(4)

''' 
cal = calendar.month(2014, 7)
print "Here is the calendar:"
print cal;
 
#############################################################################################
Var = "david"
print len(Var)