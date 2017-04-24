class Stack :

	def __init(self):
		
		self.list = []

	def push(self, input):
		# save last element at last
		self.list.append(input)
		print(self.list)

	def pop(self):
		# return last element and remove
		print(self.list.pop())

	def clear(self):
		# remove all element

