from collections import deque

prompt = "Enter an int value (<0 to end):"
myStack = deque()
value = int(input(prompt))
while value >= 0:
	myStack.append(value)
	value = int(input(prompt))

while len(myStack) > 0:
	value = myStack.pop()
	print(value)
print (myStack)
