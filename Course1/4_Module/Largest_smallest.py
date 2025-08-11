#Generate the code which calculates the largest and smallest number from a list of numbers
numbers = []
while True:
    try:
        line = input()
        if line == "":
            break
        numbers.append(int(line))
    except EOFError:
        break
largest = numbers[0]
smallest = numbers[0]
for number in numbers:
    if number > largest:
        largest = number
    if number < smallest and number > 0:
        smallest = number
print(smallest, largest)