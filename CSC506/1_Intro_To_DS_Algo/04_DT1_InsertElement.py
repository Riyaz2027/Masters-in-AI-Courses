# python program to insert element using insert operation
def insert(arr, element):
	arr.append(element)
# Driver's code
if __name__ == '__main__':
	# declaring array and value to insert
	LA = [0, 0, 0]
	x = 0
	# array before inserting an element
	print(f"Array Before Insertion: ")
	for x in range(len(LA)):
		print("LA", [x], " = " , LA[x])
	print(f"Inserting elements....")
	# array after Inserting element
	for x in range(len(LA)):
		LA.append(x)
		LA[x] = x+1
	print(f"Array After Insertion: ")
	for x in range(len(LA)):
		print("LA", [x], " = " , LA[x])