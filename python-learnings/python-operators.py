# An operator is a symbol that performs operation on variables or value. There are assignment, comparison, logic and arithmetic operators.

# Expression
# A combination of values, variables, operator or function call that produces a result.
x = 10
y= 20
z= x + y # expression - combination of values or variables that produces a result
total = 20 + 10 # expression
print(z) # expression

# String Operation
# Concatenation of String
a = "Hello"
b = "World"
c = a + " " + b
print(c)
d = f"{a} {b}"
print(d)

# Multiply string
print(a*5)
print(f'{a}\n' *5)

# Membership operators
# in not in
print("e" in a)
print("z" not in b)
list_numbers = [1, 2, 5, 4, 6, 3]
list_numbers_2 = [1, 2, 5, 4, 6, 8, 3]
list_numbers_3 = [[1, 2, 5, 4, 6, 8, 3], [1, 2, 5, 4, 6, 3]]
print(10 in list_numbers) #False
print(list_numbers in list_numbers_2) #False
print(list_numbers_2 in list_numbers_3) #True

# Equal operators
num_1 =10
num_2=10
print(num_1 == num_2)
print(num_1 != num_2)

# Arithmetic operators
# addition +
# subtraction -
# multiplication *
# division /
# floor division //
# modulus %
# Raised to power **
x = 10
y= 3
print(x + y)
print(x - y)
print(x * y)
print(x / y)
print(x // y)
print(x % y)
print(x ** y)

# Comparison operator
# > greater than
# < less than
# >= greater than or equal to
# <= less than or equal to
# == equal to
# != not equal to
print(x > y)
print(x < y)
print(x >= y)
print(x <= y)
print(x==y)
print(x!=y)

string_x = "10"
print(x == string_x) # Python will not convert type it is strict string 10 and int 10 is not equal