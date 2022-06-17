x = ["sean","david","peart"]

#names=list (x)

#print (names)

#print ( "mike" in x )

#Entername =  raw_input ("enter your name here") 

def  names ():
	if ("mike" in x ):
	    print ("yes mike is in my array but on your request i have removed it")
        
            x.remove("mike")
            
            names=list (x)
            print (names)

        elif("sean" in x ):

             print ("mike is not in my array but on your request i have added it ") 

             x.append ("mike")
             names=list (x)
             print (names)
names();

