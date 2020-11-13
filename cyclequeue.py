
class Queue:
	def __init__(self, maxSize):
		self.count = 0
		self.front = 0
		self.back = maxSize - 1
		self.qArray = [None]*maxSize

	def isEmpty(self):
		return self.count == 0

	def isFull(self):
		return self.count == len(self.qArray)

	def __len__(self):
		return self.count

	def enqueue(self, item):
		assert not self.isFull(), "Cannot enqueue to a full queue."
		maxSize = len(self.qArray)
		self.back = (self.back + 1) % maxSize
		self.qArray[self.back] = item
		self.count +=1

	def dequeue(self):
		assert not self.isEmpty(), "Cannot dequeue from an empty queue"
		item = self.qArray[self.front]
		maxSize = len(self.qArray)
		self.front = (self.front + 1) % maxSize

		self.count -=1
		return self.qArray.pop(0)

	def list(self):
		return self.qArray
a = Queue(3)
a.enqueue(1)
a.enqueue(2)
a.enqueue(3)
a.dequeue()
a.dequeue()
print(a.list())
