class Queue :

	def __init(self):
		
		self.list = []

	def enqueue(self, input):
		# save last element at last
		self.list.append(input)
		print(self.list)

	def dequeue(self):
		# return first element and remove
		print(self.list.pop(0))

	def clear(self):
		# remove all element
		

