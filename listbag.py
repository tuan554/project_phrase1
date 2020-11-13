class _BagListNode:
	def __init__(self, item):
		self.item = item
		self.next =None

class Bag:
	def __init__(self):
		self.head = None
	
	def add(self, item):
		newNode = _BagListNode(item)
		newNode.next = self.head
		self.head = newNode


	def listprint(self):
		printval = self.head
		while(printval):
			print(printval.item)
			printval = printval.next
bag = Bag()
item1 = _BagListNode("Erazer")
bag.add(item1)
item2 = _BagListNode("Pencil")
bag.add(item2)

bag.listprint()

