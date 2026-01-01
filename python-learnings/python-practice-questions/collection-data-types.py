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

# ------------------ Exercise 1 ------------------
# Create a list of 6 foods.
# Print the first item, the middle item, and the last item.
# Change one of the items to something else.
# Add a new food to the collection.
# Print the final result.
list_of_food=["apple", "rice", "bread", "ice-cream", "beans", "pineapple"]
length_of_items =len(list_of_food)
middle_item_count= int(length_of_items/2) -1
first_item =list_of_food[0]
middle_item=list_of_food[middle_item_count]
last_item = list_of_food[-1]
print(first_item)
print(middle_item)
print(last_item)
list_of_food[4]= "pasta"
list_of_food.append("pizza")
print(list_of_food)

# ------------------ Exercise 2 ------------------
# Create a list of 10 numbers.
# Print the first three numbers.
# Print the last three numbers.
# Print the numbers in reverse order.
# Print every second number in the list.
list_of_ten_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(list_of_ten_numbers[:3])
print(list_of_ten_numbers[len(list_of_ten_numbers)-3:])
list_of_ten_numbers.reverse()
print(list_of_ten_numbers)
list_of_ten_numbers.reverse()
print(list_of_ten_numbers[::2])

# ------------------ Exercise 3 ------------------
# Create a tuple of 5 animals.
# Print the second and fourth animal.
# Check how many times one animal appears.
# Get the position of one of the animals.
tuple_of_animals =("dog", "cow", "lion", "giraffe", "snail")
print(tuple_of_animals[1])
print(tuple_of_animals[3])
no_of_cow= tuple_of_animals.count("cow")
print(no_of_cow)
position_of_cow =tuple_of_animals.index("cow")
print(position_of_cow)

# ------------------ Exercise 4 ------------------
# Create a tuple containing your name, age, and country.
# Store each value into separate variables.
# Print each variable on its own line.
tuple_data = ("Jess", 10, "Nigeria")
first_name = tuple_data[0]
age = tuple_data[1]
country = tuple_data[2]
print(first_name)
print(country)
print(age)

# ------------------ Exercise 5 ------------------
# Create a set containing at least 8 numbers with some duplicates.
# Print the set.
# Add a new number to the set.
# Remove a number from the set.
# Convert the set into a list and print it.

set_of_numbers = {1,2,4,3,2,4,6,5,}
print(set_of_numbers)
set_of_numbers.add(7)
set_of_numbers.discard(7)
list_of_set = list(set_of_numbers)
print(list_of_set)

# ------------------ Exercise 6 ------------------
# Create two sets of numbers with some common values.
# Find elements that exist in both sets.
# Find elements that exist only in the first set.
# Find elements that are in either set but not both.

set_a ={1,2,3,6,7}
set_b={5,6,7,1,8}
intersection_a_b=set_a.intersection(set_b)
print(intersection_a_b)
difference_a_b=set_a.difference(set_b)
print(difference_a_b)
symmetric_difference = set_a.symmetric_difference(set_b)
print(symmetric_difference)

# ------------------ Exercise 7 ------------------
# Create a dictionary with your details: name, age, city.
# Print your name from the dictionary.
# Change your city to another city.
# Add a new key-value pair for hobby.
# Remove one key-value pair.
person_dict={
    "name": "Jess",
    "age": 5,
    "city":"lagos"
    }
print(person_dict["name"])
person_dict["city"] ="Ikeja"
person_dict["hobby"]= "singing"
person_dict.pop("age")

# ------------------ Exercise 8 ------------------
# Create a dictionary of three countries and their capitals.
# Print all the country names.
# Print all the capital names.
# Change the capital of one country.

# countries_dic = {
#     "Nigeria": "Abuja",
#     "Ghana": "Accra",
#     "France": "Paris"
# }

countries_dic={
    "Nigeria":{
       "capital":"Abuja"
    },
    "Ghana": {
        "capital": "Accra"
    },
    "France": {
        "capital": "Paris"
    }
}
for country, obj in countries_dic.items():
        print(country)
for country, obj in countries_dic.items():
    for capital in obj:
        print(obj[capital])
countries_dic["France"].update({"capital":"Rome"})

# ------------------ Exercise 9 ------------------
# Create a list that contains three dictionaries.
# Each dictionary should store a person's name and age.
# Print the age of the second person.
# Change the name of the first person.
# Add a new person's dictionary to the list.
list_of_dic= [
    {
    "name":"Jess", "age":10
    },
    {
    "name":"Joe", "age":15
    },
    {
    "name":"Roy", "age":12
    },
]
print((list_of_dic[1]["age"]))
list_of_dic[0]["name"]= "Ken"
list_of_dic.append({"name":"Rose", "age":12})
print(list_of_dic)

# ------------------ Exercise 10 ------------------
# Create a dictionary where each key is a student's name
# and each value is a list of their three test scores.
# Print the scores of one student.
# Change one of the scores.
# Add a new student and their scores.
# Print only the student names.


student_dict={
    "Ray":[55, 85, 99],
    "Sarah":[71,79,92],
    "Brad":[58,86,72],
    "Rose":[88,85,96]
    }

print(student_dict["Sarah"])
student_dict["Sarah"][2]=95
student_dict["Queen"]=[75, 88, 91]
for student in student_dict.keys(): print(student)
