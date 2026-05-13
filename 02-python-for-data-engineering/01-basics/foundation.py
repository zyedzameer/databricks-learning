#Arithmetic Operators ---------------------------------------------------
num1 = 25
num2 = 5
add = num1 + num2
diff = num1 - num2
mul = num1 * num2
div = num1 / num2

# Assignment operations ---------------------------------------------------
x = 50 #assigment
x += 10 #increment

# Relational operations ---------------------------------------------------
y = 50
result = x==y #returns boolean result
notEqual = x!=y
lessThan = x<y
greaterThan = x>y

#Logical Operators ---------------------------------------------------
age = 30
marks = 450

andOperation = age > 20 and marks > 500
orOperation = age > 20 or marks > 450
notOperation = not age > 20

print(f" {'#' * 10} Arithmetic Operators {'#' * 10} ")
print(f"addition of given numbers {num1} and {num2} is {add}")
print(f"subtraction of given numbers {num1} and {num2} is {diff}")
print(f"multiplication of given numbers {num1} and {num2} is {mul}")
print(f"division of given numbers {num1} and {num2} is {num1 / num2}")

print(f" {'#' * 10} Assignment Operators {'#' * 10} ")
print(f"value of x is {x}")

print(f" {'#' * 10} Relational Operators {'#' * 10} ")
print(f"result after comparing x and y is {result}")
print(f"not equal: {notEqual}")
print(f"less than: {lessThan}")
print(f"greater than: {greaterThan}")

print(f" {'#' * 10} Logical Operators {'#' * 10} ")
print(f"and operation: {andOperation}")
print(f"or operation: {orOperation}")
print(f"not operation: {notOperation}")

#Conditional statements ---------------------------------------------------

dept = 'civil'
studentName = 'john'

if age >= 30 and marks < 500:
    if dept == 'civil':
        print(f" {'#' * 10} Conditional statements {'#' * 10} ")
        print("welcome to civil dept..")
        if studentName=='mark':
            print("Hi Mark")
        elif studentName=='wilson':
            print("Hi Wilson")
        elif studentName=='john':
            print("Hi John")
        else:
            print("New student onboarded..")
    else:
        print("welcome to IT dept")
        print("New student onboarded..")

if studentName.startswith('j'):
    print(f"yes {studentName} starts with J")

if dept[1]=='i':
    print(f"welcome again to {dept}..")

#Looping statements ---------------------------------------------------
'''
for -> iterative, fixed level, unconditional
while -> entry controlled, not fixed (loop happens until the given condition is satisfied)
do while -> exit controlled, not fixed (loop happens at least once and then the given condition is checked)
            (note - there is no do while in python but there is work around to achieve it)
'''

for chars in studentName:
    print(chars)

while_num = 10

#while while_num > 1: #this will run forever since condition is always true
while while_num > 10 : #this will not get executed proving its entry controlled
    print(f"value of while_num is {while_num}")
    while_num += 1

givenRange = int(input("Enter a range.."))
operation = input("Enter operation (odd or even)...")

for i in range(1,givenRange):
    if operation=='odd':
        if i%2==1:
            print(f"{i} is odd number")
    elif operation=='even':
        if i%2==0:
            print(f"{i} is even number")
    else:
        print("operation should either odd or even")