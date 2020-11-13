# class ListNode:
# 	def __init__(self, data):
# 		self.data = data
# 		self.next = None
# a= ListNode(11)
# b = ListNode(52)
# c =ListNode(18)
# a.next = b
# b.next = c

# print(a.data)
# print(a.next.data)
# print(a.next.next.data)
# print(c.next)
# def traversal(head):
# 	curNode = head
# 	while curNode is not None:
# 		print (curNode.data)
# 		curNode = curNode.next
# traversal(a)
# tao mot lop hoc sinh gom ten, diem
# nhap 1 danh sach gom muoi phan tu, tao 10 lien ket giua cac phan tu
# in ra danh sach

class HocSinh:
	def __init__(self, name, score):
		self.name = name
		self.score = score
		self.next = None

a = HocSinh(input("Enter name"), int(input("Enter score")))
kt = "y"
dem = 0
b = None
c =None
while kt == "y":
	if dem == 0:
		b =  HocSinh(input("Enter name"), int(input("Enter score")))
		a.next = b
		c = b
	else:
		b = HocSinh(input("Enter name"), int(input("Enter score")))
		c.next = b
		c = b
	kt = input("Press y to continue")
	dem +=1

def travel(head):
	curNode = head
	i = 0
	q = 0
	while curNode is not None:
		i = i + curNode.score
		curNode = curNode.next
		q = q + 1
	u = i / q
	curNode = head
	while curNode is not None:
		# if curNode.score < u:
		print(curNode.name)
		print(curNode.score)
		curNode = curNode.next
travel(a)


# def unorderedSearch(head, target):
# 	curNode = head
# 	while curNode is not None and curNode.score != target:
# 		curNode = curNode.next
# 	return curNode is not None
# print(unorderedSearch(a, 45))


# tinh diem trung binh cua tat ca hoc sinh vua nhap vao + viet lai nhap vao danh sach + in ra cac hoc sinh co diem duoi trung binh cua ca lop 
# def removeNode(head, target):
# 	predNode = None
# 	curNode = head
# 	while curNode is not None and curNode.score != target:
# 		predNode = curNode
# 		curNode = curNode.next
# 	if curNode is not None:
# 		if curNode is head:
# 			head = curNode.next
# 		else:
# 			predNode.next = curNode.next	
# 	return head
	

# head = removeNode(a, 15)
# while head is not None:
# 	print (head.score)
# 	head = head.next
	# Nhap vao 1 danh sach hoc sinh sau do chon remove mot diem bat ky va in ra danh sach con lai















































