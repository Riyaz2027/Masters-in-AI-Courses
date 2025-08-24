my_list = ["cat", "dog", "horse", "hen", "goat", "cat", "dog", "hen"]

# Modification methods
my_list.sort()                # Sorts alphabetically
sorted_list = sorted(my_list)   # Returns sorted copy, original unchanged
my_list.reverse()             # Reverses in place
my_list.clear()               # Removes all elements
my_list.pop(2)                # Removes and returns the third element
del my_list[0]                # Deletes the first element
sliced_list = my_list[1:4]    # Gets a slice from index 1 to 3 (inclusive of 1, exclusive of 4)