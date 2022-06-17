
Numbers = [10,9,8,7,6,5,4,3,2,1]



def callBack ():

	print "called"

	for x in Numbers:

		num = 1

		if x == 1:

			num = x 

			print num

			callBack()

		if num < 2:

			print 





callBack()