
'''

mypython script 

'''
class Name (object): 

    def __init__(self,personsName):
        
        self.personsName = personsName


        #self.number = 17 overridding vars 


        #print self.number
         

        print ("My first name is  "+personsName)

        print ("\n")

        pass 

    def Name01 (self,last):
 
        print ("My last name is " + last )

        print ("\n")


    def Age (self, age): 

        print ("My age is " + str(age) + " years old")

        print ("\n")

    def School (self,school):
         
        print ("I go to school at " + school )
        
        print ("\n")

    def  Grade (self, grade):
           
         
         print ("My grade is " +str(grade)+"th")

         print ("\n")




x = Name ("Sean")

x.Name01("Peart")

x.Age (18)

x.School ("Bard High School Early College")

x.Grade(12)


#-------------------------------------------------------
y = Name ("David")

y.Name01("Peart")

y.Age (11)

y.School ("LAS")

y.Grade(6)


class InheritClass (Name):

    def __init__ (self):

        pass



grab = InheritClass ()

grab.Age(40)






class Newname(InheritClass):

    def __init__(self):

        pass 

        #super(Newname,self).__init__()  overridding vars 


        #self.number = 18



z = Newname ()

z.Name01("Samuel")


#print z.number

#----------------------------------Overridding varbales and funcions------------------------------------------------------------



class Override (object): 

    def __init__(self):
        
        yes =   "Yes I have the class all for my self with out not other trying to override me "

        #print  yes 

        print ("\n")


    def friend (self):

        print ("I No evil in sight")

        print ("\n")






#i = Override ()

#i.friend ()



class EvilOverride (Override): 

    def  __init__ (self):
        

        super (EvilOverride,self).__init__()

        self.yes = "oh oh oh I take over your class"


        print (self.yes)

        print ("\n")



    def friend (self):
        
        print ("I am here to take over oh oh oh !!!")

        print ("\n")





g = EvilOverride ()

g.friend ()








