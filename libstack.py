class Stack:
	def __init__(self):
		self._theItems = []

	def isEmpty(self):
		return len(self) == 0

	def __len__(self):
		return len(self._theItems)

	def pop(self):
		assert not self.isEmpty(), "jndsjnfjnfkw"
		return self._theItems.pop()

	def push(self, item):
		self._theItems.append(item)

	def list(self):
		return self._theItems	


a = Stack()
a.push(10)
a.push(20)
a.push(30)
a.push(40)
a.push(50)
a.push(60)
a.push(70)
a.push(80)
a.push(90)
a.push(100)

def bubbleSort( theSeq ):
	n = len( theSeq )

	for i in range( n - 1 ) :

		for j in range(n -i-1) :
			if theSeq[j] > theSeq[j + 1]: 
				tmp = theSeq[j]
				theSeq[j] = theSeq[j + 1]
				theSeq[j + 1] = tmp
	return theSeq
print(bubbleSort(a.list()))