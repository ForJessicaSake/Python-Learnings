# ------------------ Exercise 1: Basic List Operations ------------------
# 1. Create a list of 5 friends' names
# 2. Print the first and last name in the list
# 3. Replace the third name with a new name
# 4. Add one more name to the end of the list
# 5. Print the final list

# write your code here
friends = ["Joy", "Dave", "Mary", "Becky", "Rachel"]
print("first name", friends[0])
print("last name", friends[-1])
friends[2] = "Michael"
friends.append("Joey")
print(friends)

# ------------------ Exercise 2: Slicing Practice ------------------
# 1. Create a list of 8 numbers
# 2. Print the first three numbers using slicing
# 3. Print the last three numbers using slicing
# 4. Print every second number in the list
# 5. Print the list in reverse using slicing

# write your code here
numbers =[4,5,9,7,8,3,2,1]
first_three_numbers = numbers[:3]
print(first_three_numbers)
length_of_list = len(numbers)
last_three_numbers = numbers[length_of_list-3:length_of_list]
print(last_three_numbers)
print(numbers[::2])
print(numbers[::-1])

# ------------------ Exercise 3: List Methods ------------------
# 1. Create a list of colors
# 2. Add a new color using append()
# 3. Add three colors at once using extend()
# 4. Remove one color using remove()
# 5. Print how many times a particular color appears using count()

# write your code here
list_of_colors = ["red", "green", "blue", "pink", "yellow"]
list_of_colors.append("black")
list_of_colors.extend(["red", "white", "purple"])
list_of_colors.remove("white")
red_count = list_of_colors.count("red")
print(red_count)

# ------------------ Exercise 4: Numbers List ------------------
# 1. Create a list of numbers
# 2. Find and print the sum of the numbers using sum()
# 3. Find and print the largest number using max()
# 4. Find and print the smallest number using min()
# 5. Sort the list in ascending order and print it

# write your code here
sum_of_numbers =sum(numbers)
print(sum_of_numbers)
max_number = max(numbers)
print(max_number)
min_number = min(numbers)
print(min_number)
print(sorted(numbers))

# ------------------ Exercise 5: Nested Lists ------------------
# 1. Create a nested list representing students and their scores:
#    Example: [["Ann", 80], ["Bob", 90], ["Sam", 75]]
# 2. Print the score of the second student
# 3. Change the first student's score to 95
# 4. Add a new student with a score
# 5. Print all student names only

# write your code here
scores_of_students =[["Ann", 80], ["Bob", 90], ["Sam", 75]]
score_of_Bob = scores_of_students[1][1]
print(score_of_Bob)
scores_of_students[0][1]=95
scores_of_students.extend([["Joey", 85]])
for students in scores_of_students:print(students[0])