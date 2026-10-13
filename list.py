# Create a list
fruits = ["apple", "banana", "mango"]

# Print the list
print(fruits)

# Access an element
print(fruits[0])

# Add an element
fruits.append("orange")

# Remove an element
fruits.remove("banana")

print(fruits)

# Loop through the list

numbers = [10, 20, 30]

for num in numbers:
    print(num)
    
    
numbers = [1, 2, 3, 4]
total = 0

for num in numbers:
    total += num

print("Sum:", total)


numbers = [12, 45, 7, 89, 23]

largest = numbers[0]

for num in numbers:
    if num > largest:
        largest = num

print("Largest:", largest)


numbers = [1, 2, 3, 4, 5, 6]

even_count = 0
odd_count = 0

for num in numbers:
    if num % 2 == 0:
        even_count += 1
    else:
        odd_count += 1

print("Even:", even_count)
print("Odd:", odd_count)


numbers = [1, 2, 3, 4]
reversed_list = []

for i in range(len(numbers) - 1, -1, -1):
    reversed_list.append(numbers[i])

print(reversed_list)


numbers = [10, 20, 30, 40]
target = 30

found = False

for num in numbers:
    if num == target:
        found = True
        break

if found:
    print("Found")
else:
    print("Not found")
    
    
numbers = [4, 2, 8, 1, 6]

smallest = numbers[0]

for num in numbers:
    if num < smallest:
        smallest = num

print("Smallest:", smallest)





numbers = [10, 5, 20, 20, 8]

largest = float("-inf")
second_largest = float("-inf")

for num in numbers:
    if num > largest:
        second_largest = largest
        largest = num
    elif num > second_largest and num < largest:
        second_largest = num

if second_largest == float("-inf"):
    print("No second-largest distinct number")
else:
    print("Second largest:", second_largest)
    
    
numbers = [1, 2, 2, 3, 1, 4]
unique = []

for num in numbers:
    if num not in unique:
        unique.append(num)

print(unique)




numbers = [1, 2, 1, 3, 2, 1]
frequency = {}

for num in numbers:
    if num in frequency:
        frequency[num] += 1
    else:
        frequency[num] = 1

print(frequency)


numbers = [-2, 3, -1, 4, 0, 5]

positive = []
negative = []
zeros = []

for num in numbers:
    if num > 0:
        positive.append(num)
    elif num < 0:
        negative.append(num)
    else:
        zeros.append(num)

print("Positive:", positive)
print("Negative:", negative)
print("Zeros:", zeros)