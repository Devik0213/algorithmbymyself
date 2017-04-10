class FunStrings :

	def __init__(self) :

		self.list = []

	def append(self, input) :
		
		self.list.append(input)

	def show(self) :

		for x in self.list :
			print(x)

	def showReverse(self) :

		reversedList = self.list
		reversedList.reverse()

		for x in reversedList :
			print(x)

funStrings = FunStrings()
funStrings.append("abc`")
funStrings.append("dfge")
funStrings.append("hshfj")
funStrings.append("ongp")
funStrings.append("sgogj")
funStrings.append("zzzmzmkzmkz")
funStrings.append("xxxxxx")
print("--------list")
funStrings.show()
print("--------reverse list")
funStrings.showReverse()
print("--------list") # ???????
funStrings.show() #엇.. 레퍼런스라 값이 바뀌네............
