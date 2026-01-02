# ------------------ Exercise 1: Age Category ------------------
# 1. Create a variable age with any number.
# 2. Using if/elif/else:
#       - print "Child" if age is less than 13
#       - print "Teenager" if age is between 13 and 17
#       - print "Adult" if age is 18 or above
age = 12
if age < 13:
    print('Child')
elif 13 <= age <= 17:
    print("Teenager")
else:
    print('Adult')

# ------------------ Exercise 2: Login Check ------------------
# 1. Create two variables:
#       - username
#       - password
# 2. Write an if statement that checks:
#       - username is "admin"
#       - AND password is "1234"
# 3. If both are correct print "Login successful"
# 4. Else print "Login failed"
user_name = input('What is your username? ')
password = input('What is your password? ')
if user_name == 'admin' and password == '1234':
    print("Login successful")
else:
    print("Login failed")

# ------------------ Exercise 3: Even or Odd List Number ------------------
# 1. Create a list of 6 numbers.
# 2. Check if the last number in the list is even or odd.
# 3. If even, print "Even number"
# 4. If odd, print "Odd number"
list_of_numbers =[1,2,3,4,5,6]
last_number = list_of_numbers[-1]
if last_number%2 ==0:
    print('Even number')
else:
    print('Odd number')

# ------------------ Exercise 4: String Membership & Condition ------------------
# 1. Create a string that contains a sentence.
# 2. Using if statements:
#       - check if the word "python" is in the sentence
#       - if yes print "Python found"
#       - else print "Python not found"
# 3. Also check:
#       - if the length of the string is greater than 15
#       - AND it contains the letter "a"
#       - print "Long string with a"
#       - otherwise print "Condition not met"
sentence = "It is 5am in the morning"
if "python" in sentence:
    print("python found")
else:
    print("python not found")

if len(sentence) > 15 and "a" in sentence:
    print('Long string with a')
else:
    print('Condition not met')

# ------------------ Exercise 5: Grades with Logical Operators ------------------
# 1. Create a variable score.
# 2. Using if/elif/else and comparison operators:
#       - 90–100 print "A"
#       - 70–89 print "B"
#       - 50–69 print "C"
#       - below 50 print "Fail"
# 3. Also print:
#       - "Perfect score!" if score is exactly 100
score = 79
if score == '100':
    print('Perfect score')
if 90 <= score <= 100:
    print('A')
elif 70 <= score <=89:
    print('B')
elif 50 <=score <=69:
    print('C')
else:
    print('Fail')

color_one = input("Enter a color, red, yellow or blue? ").lower()
color_two = input("Enter a color, red, yellow or blue. Do not enter the previous color ").lower()

if color_one == "red" and color_two == "yellow" or color_one == "yellow" and color_two == "red":
    print('orange')
elif color_one == "blue" and color_two == "yellow" or  color_one == "yellow" and color_two == "blue":
    print('green')
elif color_one == "red" and color_two == "blue" or color_one == "blue" and color_two == "red":
    print('purple')
elif color_one == "red" and color_two == "red":
    print('red')
elif color_one == "yellow" and color_two == "yellow":
    print('yellow')
elif color_one == "blue" and color_two == "blue":
    print('blue')
else:
    print('Invalid color combination')
