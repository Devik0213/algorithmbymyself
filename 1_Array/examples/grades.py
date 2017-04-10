# http://interactivepython.org/runestone/static/pythonds/Introduction/GettingStartedwithData.html#built-in-collection-data-types

class Grades :
	
	def __init__(self):

		self.list = []

	def append(self, input) :
		
		self.list.append(input)

	def show(self) :

		for x in self.list :
			print(x)

	def average(self):

		sum = 0

		for x in self.list :
			sum += x

		print(sum/len(self.list))




grades = Grades()
grades.append(83)
grades.append(95)
grades.append(56)
grades.append(59)
grades.append(83)
# grades.show()
print("Average")
grades.average()
