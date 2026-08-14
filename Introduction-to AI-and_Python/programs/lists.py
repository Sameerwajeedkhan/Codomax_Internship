numbers = [10, 20, 30, 20, 40, 10]

print("Original list:", numbers)

print("Length:", len(numbers))
print("Maximum:", max(numbers))
print("Minimum:", min(numbers))

numbers.append(50)

print("After adding 50:", numbers)

numbers.remove(20)

print("After removing 20:", numbers)

unique_numbers = list(set(numbers))

print("Without duplicates:", unique_numbers)