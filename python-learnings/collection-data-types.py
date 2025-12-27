# Collection data types
# Python has other data types for collections: lists, tuples, sets, dicts.

# List  |       |Mutable   |Ordered |
# Tuple |       |Immutable |Ordered |
# Set   |Unique |Mutable   |Unordered|
# Dict  |Mapped |Mutable  |Unordered|

# Mutable - You can make changes to them
# Immutable - You cannot make changes to them

# List
#---------------------
# A collection of items defined by a square bracket or the list function, where each item is separated by comma
empty_list = []
print(empty_list)

my_list = ["Will", "Sam", "Ray", "Joe", "Brad", "Max", "Roy"]

# Getting items from a list
print(my_list[0]) # Will
print(my_list[1]) # Sam
print(my_list[-1]) # Brad

# Slicing items in a list
print(my_list[:2]) # --> start from the beginning of the array and stop just before index 2 ["Will", "Sam"]
print(my_list[:6:2]) #--> ["Will", "Ray", "Brad"]
print(my_list[::2])  #--> ["Will", "Ray", "Brad", "Roy"]

# Length of a list
# len() function returns the length of a list passed as an argument
print(len(my_list)) #7

# List methods
# list.clear() - clears a list or empties a list
my_list.clear()
print(my_list)

# list.append() - adds a single item to the back of a list
my_list.append("Rachel")
print(my_list)

# list.extend() - adds multiple item to the back of a list
my_list.extend(["Joe", "Brad", "Max", "Roy", "Will", "Silvie", "Cara"])
print(my_list)

# list.sort() - sorts items in an array alphabetically and numerically
my_list.sort()
print(my_list)

nums=[5,8,2,1,6]
nums.sort()
print(nums)

# list.count() - returns count of the number of item present in that list
print(my_list.count("Will"))
print(my_list.count("Cara"))

# list.index() - returns the index number of that item
print(my_list.index("Silvie"))

# list.insert() - inserts an item depending on the index number passed
my_list.insert(2, "Ray")
print(my_list)

# list.remove() - remove a specific item from a list that matches the argument passed
my_list.remove("Ray")
print(my_list)

# list.pop() - remove the last item from a list and returns the item removed
popped_value = my_list.pop()
print(popped_value, "popped value")
print(my_list)

# list.reverse() - reverses the order of items in a list
my_list.reverse()
print(my_list)

# list.copy() - Creates an independent copy of a list
new_list = my_list.copy()
print(new_list)

# Replacing items in a list
my_list[2] = "Denzel"
my_list[-1]= "Sandra"
print(my_list)

# Nested lists
# These are lists which contain one or multiple lists
points =[[0,1], [55, 21], [80, 92]]
print(points[0], points[1], points[2])
print(points[0][0], points[0][1], points[1][0], points[1][1], points[2][0], points[2][1])

numbers = [2, 5, 2, 4]
# Sum of values
total = sum(numbers)
print(total)

# Min and Max values
min_value = min(numbers)
print(min_value)
max_value = max(numbers)
print(max_value)




