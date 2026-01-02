# Conditional statements are used to add logic to python
# if, elif, else statements

# if statement syntax
condition = True
do_something = "conditional statements"
if condition:
    print(do_something)

# Indentation
# The tab space after some code to tell Python that some block of code is related to each other
age = 18
if age <=12:
    print('This user is a child')
elif 12 < age <=17:
    print("This user is a teenager")
else:
    print("This user is an adult")

# Logical operators
# And - all conditions need to be true to be True
# Or - one of the condition need to be true to be True
# Not - by default False
if age <=12:
    print("This user is a child")
elif age <12 and age <=17:
    print("This user is a teenager")
elif age <18 and age <=60:
    print('This user is an adult')
else:
    print('This user is an elder')

list_of_number = [1,3,5,]
if 2 not in list_of_number:
    print('This is not a list of even numbers')
    if 3 or 5 in list_of_number:
        print('This list is even numbers')
else: print('This is a list of even numbers')
