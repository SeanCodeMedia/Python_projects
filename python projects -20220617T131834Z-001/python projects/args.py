
# passing unlimited arguments 
# also a list of ags 
def pass_in(*agrs):

	for agrs in agrs:

		print agrs 



ten = [1,2,3,4,5,6,7,8,9,10]

#pass_in(*ten)


# overriding arguments 
# over ride stop from crashing 

def  Argu ( x = 11 , y = 12):

	print x
	print y  




#Argu()

# nesting functions in python 


def outSide_Fun (x = 1):

    x = 1
 #print "out side function"

    def inside_fun():

        print x

    return inside_fun
	 
	 

fun = outSide_Fun ()

fun ()

################class
class sean (object): 


    def __init__ (self):


        pass 
    
    def info (self):

        print "sean"





#x = sean ()

#x.info()


#///////////declration///////////////////////


def Add_a_one (func):

    def nesting ():

        return func ()+1

return nesting 

########################



