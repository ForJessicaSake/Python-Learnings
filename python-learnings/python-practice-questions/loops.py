# ------------------ Exercise 1: Count and Skip ------------------
# Using a for loop, print numbers from 1 to 30.
# Skip the numbers that are divisible by 3 using 'continue'.
for i in range(1, 31):
    if i % 3 == 0:
        continue
    print(i)

# ------------------ Exercise 2: Sum of Even Numbers ------------------
# Create a list of numbers.
# Using a loop, calculate the sum of ONLY the even numbers in the list.
# Print the final total.
list_of_numbers = [1,2,3,4,5,6,7,8,9]
sum_of_list_of_numbers = 0
for number in list_of_numbers:
    if number%2== 0:
        sum_of_list_of_numbers += number
print(sum_of_list_of_numbers)

# ------------------ Exercise 3: Multiplication Table ------------------
# Ask the user to enter a number.
# Using a for loop, print the multiplication table of that number from 1 to 12.
# Example output format: 3 x 1 = 3
user_input = input("Enter a number: ")
user_input_int = int(user_input)
for number in range(1,13):
    print(f"{user_input_int} x {number} = {user_input_int * number}")

# ------------------ Exercise 4: Reverse Countdown ------------------
# Using a while loop, start counting down from 10 to 0.
# When the loop finishes, print "Blast off!".
count = 10
while count >= 0:
    print(count)
    count -=1
print("Blast off")

# ------------------ Exercise 5: Largest Number ------------------
# Create a list containing at least 6 numbers.
# Using a loop (without using max()), find the largest number in the list.
# Print the largest number.
list_of_six_numbers = [1,2,3,4,5,6]
max_number = list_of_six_numbers[0]
for number in list_of_six_numbers:
    if number > max_number:
        max_number = number
print(max_number)

# ------------------ Exercise 6: Count Vowels ------------------
# Ask the user to enter a word.
# Using a loop, count how many vowels (a, e, i, o, u) are in the word.
# Print the number of vowels.
vowels = ('a', 'e', 'i', 'o', 'u')
word_input = input("Enter a word: ").lower()
count = 0
for letter in word_input:
    if letter in vowels:
        count += 1
print(count)

# ------------------ Exercise 7: Squares of Numbers ------------------
# Using a for loop, print the squares of the numbers from 1 to 10.
# Example: 2 -> 4, 3 -> 9
for num in range(1, 11):
    print(num ** 2)

# ------------------ Exercise 8: Login Attempts System ------------------
# The user has only 3 attempts to enter the correct password.
# Ask the user for a password in a loop.
# If the password is correct, print "Access granted" and stop the loop.
# If the user fails 3 times, print "Account locked".
password_attempt_trial =0
password ="admin"
while password_attempt_trial <3:
    user_password = input("Enter a password: ")
    if password == user_password:
        print("Access granted")
        break
    else:
        print("Wrong password")
        password_attempt_trial +=1
    if password_attempt_trial ==3:
        print("Account locked")
        break


# ------------------ Exercise 9: Stop at Negative Number ------------------
# Create a list of numbers containing both positive and negative values.
# Loop through the list.
# Stop looping when a negative number is found using 'break'.
# Print the negative number that stopped the loop.
list_of_positive_and_negative_nos = [1, -2, -6, 6, 8, 12]
for no in list_of_positive_and_negative_nos:
    if no < 0:
        print(f'The negative number that broke the loop is {no}')
        break
    print(no)

# ------------------ Exercise 10: Nested List Items ------------------
# Given the list: items = [["a", "b"], ["c", "d", "e"]]
# Using nested loops, print each element separately.
items = [["a", "b"], ["c", "d", "e"]]
for item in items:
    for letter in item:
        print(letter)