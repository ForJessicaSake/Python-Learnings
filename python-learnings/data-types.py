# Variables in Python
# --------------------------------------------
# Variables are like a box used to store a data of different data types.
# In Python variables are declared using the variable name known as the label followed by an equal to sign and the variable value or data.
# Variables cannot be special keywords or functions, cannot start with a number, cannot have special characters and should be in snake case.
# Python built-in functions - print, type, sum, filter, id.
# Python built-in keywords - not, in, break, continue, if, elif, else.

name_of_person = "Michael"
print(name_of_person)

total = 100
print(total)

isValid = total == 100
print(isValid)

# Data Types in Python
#--------------------------------------------
# string, integer, float, boolean, none-type

# string data type represents texts in general
name_of_school = "Michigan college of medicine"
print(name_of_school)

# In python only strings can be concatenated together. Concatenating another data type will create a syntax error.
print(name_of_school + "United Kingdom")
# print(name_of_school + 5) syntax error

# To concatenate other data types into a string is called - string formatting using the f keyword and curly braces as seen below:
print(f"number of registered accredited courses in {name_of_school} is {44}")

# Integer known as int data type represents whole numbers in general
number_of_student = 555
print(f"number of students {number_of_student}")

# Float data type represents decimal numbers in general
average_number_of_students = 227.5
print(f"average number of students {average_number_of_students}")

# Boolean data type represents values true and false
print(f"Does the college of medicine offer Dentistry as a course, True/False? {True}")

# Checking Data type of values
#--------------------------------------------
# Python comes with a built-in function "type" that is used to check the data type of any value
x = 11
type_of_x = type(x)
print(type_of_x)

y = 12.55
type_of_y = type(y)
print(type_of_y)

name= "Max"
type_of_name= type(name)
print(type_of_name)

yes = name == "Max"
type_of_yes = type(yes)
print(type_of_yes)

# Converting Data type of values
convert_x_to_float = float(x)
print(convert_x_to_float) #11.0

convert_y_to_int= int(y)
print(convert_y_to_int) #12



