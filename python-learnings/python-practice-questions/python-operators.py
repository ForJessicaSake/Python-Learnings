# ------------------ Exercise 1: Arithmetic & Expressions ------------------
# 1. Create two variables a and b with any numbers.
# 2. Create expressions to calculate:
#       - sum
#       - difference
#       - product
#       - quotient
# 3. Store each result in a variable.
# 4. Print all the results on separate lines.
a = 10
b= 4
sum_of_num = a + b
diff_of_num = a - b
prod_of_num = a * b
quotient_of_num = a / b
print(sum_of_num)
print(diff_of_num)
print(prod_of_num)
print(quotient_of_num)

# ------------------ Exercise 2: String Concatenation & Multiplication ------------------
# 1. Create two string variables for first name and last name.
# 2. Join them into a full name with a space in between.
# 3. Print the full name in uppercase.
# 4. Print the full name 5 times, each on a new line.
first_name = "Ray"
last_name = "Brent"
full_name = f"{first_name} {last_name}"
print(full_name.upper())
print(f"{full_name}\n" *5)

# ------------------ Exercise 3: Membership Operators ------------------
# 1. Create a string variable that stores a sentence.
# 2. Check if the letter "a" exists in the string.
# 3. Check if the word "python" exists in the string.
# 4. Print the results of both checks.
message = "Studying is a skill"
is_a_in_message="a" in message
is_python_in_message="python" in message
print(is_a_in_message)
print(is_python_in_message)

# ------------------ Exercise 4: Comparison Operators ------------------
# 1. Create a variable called age.
# 2. Compare it with the number 18 using:
#       - greater than
#       - less than
#       - equal to
#       - not equal to
# 3. Print all the comparison results.
age = 12
is_age_greater_than_18 = age > 18
is_age_less_than_18 = age < 18
is_age_equal_to_18 = age == 18
is_age_not_equal_to_18 = age != 18
print(is_age_greater_than_18)
print(is_age_less_than_18)
print(is_age_equal_to_18)
print(is_age_not_equal_to_18)

# ------------------ Exercise 5: Lists, Membership, and Comparison ------------------
# 1. Create a list containing 7 numbers.
# 2. Check if the number 10 is in the list.
# 3. Check if the first number in the list is greater than the last number.
# 4. Print the results of both checks.
list_of_numbers = [1, 4, 2, 10, 8, 3, 6]
# is_10_in_list_of_numbers = bool(list_of_numbers.count(10))
is_10_in_list_of_numbers = 10 in list_of_numbers
is_first_number_greater_than_last_number_in_list_of_numbers = list_of_numbers[0] > list_of_numbers[-1]
print(is_10_in_list_of_numbers)
print(is_first_number_greater_than_last_number_in_list_of_numbers)