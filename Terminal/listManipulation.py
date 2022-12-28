
numbers = [1, 2, 3, 4, 5]

# Use len() to get the length of the list
length = len(numbers)
print(length)  # Output: 5

# Use max() to get the maximum value in the list
maximum = max(numbers)
print(maximum)  # Output: 5

# Use min() to get the minimum value in the list
minimum = min(numbers)
print(minimum)  # Output: 1

# Use sorted() to get a new sorted list
sorted_numbers = sorted(numbers)
print(sorted_numbers)  # Output: [1, 2, 3, 4, 5]

# Use sum() to get the sum of all the elements in the list
total = sum(numbers)
print(total)  # Output: 15

# Use append() to add an element to the end of the list
numbers.append(6)
print(numbers)  # Output: [1, 2, 3, 4, 5, 6]

# Use extend() to add all the elements of another list to the end of the list
numbers.extend([7, 8, 9])
print(numbers)  # Output: [1, 2, 3, 4, 5, 6, 7, 8, 9]

# Use insert() to insert an element at a specific index in the list
numbers.insert(3, 10)
print(numbers)  # Output: [1, 2, 3, 10, 4, 5, 6, 7, 8, 9]

# Use remove() to remove an element from the list
numbers.remove(10)
print(numbers)  # Output: [1, 2, 3, 4, 5, 6, 7, 8, 9]

# Use pop() to remove and return the last element of the list
last = numbers.pop()
print(last)  # Output: 9
print(numbers)  # Output: [1, 2, 3, 4, 5, 6, 7, 8]

# Use index() to get the index of the first occurrence of a value
index = numbers.index(4)