numbers = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]

# Find and print the sum of all even numbers in the list

even_sum = sum(num for num in numbers if num % 2 == 0)
print("Sum of even numbers:", even_sum)

# Create a new list of squares of odd numbers

squares_of_odd = [x * x for x in numbers if x % 2 != 0]

#Sort the original list in ascending order
numbers.sort(reverse=False)

#Remove duplicates from the original list
numbers = list(set(numbers))

#Print the updated original list and list of squares of odd numbers
print("Updated original list:", numbers)
print("Squares of odd numbers:", squares_of_odd)