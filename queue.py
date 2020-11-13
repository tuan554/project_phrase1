class Queue :
	def __init__(self):
		self.qList = list()

	def isEmpty(self):
		return len(self) == 0

	def __len__(self):
		return len(self.qList)

	def enqueue(self, item):
		self.qList.append(item)

	def dequeue(self):
		assert not self.isEmpty(), "Cannot dequeue from an empty queue"
		return self.qList.pop(0)

	def list(self):
		return self.qList

a = Queue()
a.enqueue(100)
a.enqueue(2888)
print(a.list())
a.dequeue()
print(a.list())