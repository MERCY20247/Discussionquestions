# Question 4(a)
# Create a list of five of your favourite foods. Write a Python program to:
# Add two more items to the list.
# Remove one item from the list.
# Print the updated list.
# Solution
favorite_foods = ['Pizza', 'Chicken', 'Chocolate', 'Ice Cream', 'Chappati']
favorite_foods.append('Yorghut')
favorite_foods.append('Apples')
favorite_foods.remove('Chappati')
print(favorite_foods)

# Question 4(b)
# Given the list numbers = [2,5,8,10,3,6], write a Python program to:
# Print the first and last elements of the list.
# Print the list in reverse order.
# Calculate and print the sum of all the elements in the list.
# Solution

numbers = [2, 5, 8, 10, 3, 6]
print("First element:", numbers[0])
print("Last element:", numbers[-1])

print("Reversed list:", numbers[::-1])
# the sum of all the elements in the list
total_sum = sum(numbers)
print(f"The sum of all the elements is {total_sum}")
