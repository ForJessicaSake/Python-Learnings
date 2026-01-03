# In Python there are two types of loops - for and while loop.
# The for loop when you already know the number of items to loop through (lists, strings, range, etc.)
# The while loop when you only know the condition, not how many times it will run

count = 0
# Create a loop that runs till count is 50 and logs each item value
# no specific number of items here so logically we would up for a while loop
while count <=50:
    print(count)
    count +=1

tickets = 100
while tickets <= 100 and tickets > 0:
    no_of_ticket = input("How many tickets do you want to purchase? ")
    no_of_ticket_int = int(no_of_ticket)
    if no_of_ticket_int<=0:
        print('Enter a valid number of ticket purchase')
        continue

    tickets -= no_of_ticket_int

    if tickets <0:
        print("Ticket purchase has exceeded ticket limit")
        break

    print(f'there are only {tickets} tickets left')

numbers = [1,2,3,4,5,6,7,8,9,10]
# calculate the sum of numbers in the array using loop
# There is a specified number here so we can opt to using the for loop

sum_of_numbers = 0
for number in numbers:
    sum_of_numbers +=number
print(sum_of_numbers)

# Continue and Break Keyword
# continue is used to skip an iteration of a loop if the condition of the loop does not align with the expected result

for number in numbers:
    if number%2 ==0:
        continue #Skip all even numbers and only print odd numbers
    print(number)

for number in numbers:
    print(number)
    if number%2 ==0:
        print(f"The first even number is {number}")
        break # when you get the first even number end the loop

# Range for loops
for number in range(50):
    print(number) # 0-49

for number in range(10, 51):
    print(number) # 10-50

for number in range(10,51,5):
    print(number) # 10-50 in counts of 5

# Nested loops
list_of_items = [["bag", "shoes"], ["towel", "pillow case", "wristwatch"], ["socks", "lamp"]]
for item in list_of_items:
    # print(item)
    for thing in item:
        print(item, thing)