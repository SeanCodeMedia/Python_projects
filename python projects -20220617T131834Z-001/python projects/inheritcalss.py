
class Parent (object): 
    def __init__(self):
    	
    	self.y = "sorry mommy"

	def  hellowWorld (self):
 		print "hellow world"



class  child (Parent):
    def __init__(self):
    
	super(child,self).__init__()

	def  goodbye (self):
 	    pass



x = child (); 
print (x.y)
