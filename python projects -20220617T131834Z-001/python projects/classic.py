


class Name (object):

	def __init__(self, name, sirname ):

	    self.name = name 

	    self.sirname = sirname

	    print self.name + "\n" + self.sirname


	    print "start of class"

	def NameFun (self): 

		print ("sean")





x = Name ("Sean", "Peart")

x.NameFun()
		
			
class  BasClass  (Name):

	def __init__(self):

		self.z = "testing 123"

		print self.z 
                      
	def NameFun (self):

		print "david"




y = BasClass ()
y.NameFun()	


'''
class dum (BasClass):

	def __init__(self):

		super (BasClass,self).__init__()

		self.z = "check check"

		print self.z





G = dum ()
'''



