# --- 1. Functions are first class citizens which can be
# assigned to variables,
# passed as arguments,
# and returned from other functions.

def square(x):
    return x ** 2

# Assigning a function to a variable
f = square
print(f(5))  # Output: 25

# Passing a function as an argument
def apply_function(func, value):
    return func(value)

print(apply_function(square, 5))  # Output: 25

# Returning a function from another function
def get_multiplier(factor):
    def multiply(x):
        return x * factor
    return multiply

double = get_multiplier(2)
print(double(5))  # Output: 10

# --- 2. side effects and variable scope -  Functions can access global variables,
# but if the variable is not defined at the time of function definition,
# it will cause a NameError when the function is called.

def funcitonCallingGlobalVariable():
    return var1

# meaningful error - calling before the global variable is defined
try:
    print(funcitonCallingGlobalVariable())
except NameError as ne:
    print(f"error occured: " + str(ne))

# now create the variable and call the function

var1 = 'hello'
print(funcitonCallingGlobalVariable())


# --- 3. Higher order functions - functions that accept/return other functions

def getResults(n1, n2, fn):
    return fn(n1, n2)

def getSum(n1, n2):
    return n1 + n2

def getDiff(n1, n2):
    return n1 - n2

print('***************HOF*************')
print(getResults(5, 2, getSum))
print(getResults(5, 2, getDiff))

# --- 4. Map - apply the function on every item in iterable

fruit_list = ['apple','orange','banana']

def getCharCount(in_list):
    result=[]
    for i in in_list:
        result.append(len(i))
    return result

print(getCharCount(fruit_list))
print(list(map(len,fruit_list))) # -- returns same result in single line


# map with custom function
def get_len(item):
    return (item, len(item))

print(list(map(get_len, fruit_list)))

# map to convert string to uppercase
def to_upper(s):
    return s.upper()

print(to_upper("hello"))
print(list(map(to_upper, fruit_list)))


# --- 5. filter() - keep only items that satisfies the condition

def onlyEven(num):
    return num % 2 == 0
print(list(filter(onlyEven, [1, 2, 3, 4, 5, 6])))


# --- 6. Lambda functions (anonymous,single-expression functions)

#map
print(list(map(lambda x : x*x,[1,2,3,4])))
print(list(map(lambda x:x[0],fruit_list)))
print(list(map(lambda x:(x,len(x)),fruit_list)))
print(list(map(lambda x:x.upper() if len(x)>5 else x,fruit_list)))

#filter
print(list(filter(lambda x: x%2 == 0,[1,2,3,4,5,6,7,8]))) #one-liner onlyEven function with lambda
print(list(filter(lambda x: len(x)>5,fruit_list)))



# --- 7. List comprehension (concise alternative to map/filter

#map alternative
print([x*x for x in [1,2,3,4]])
print([x[0] for x in fruit_list])
print([(x,len(x)) for x in fruit_list])
print([x.upper() if len(x)>5 else x for x in fruit_list])

#filter alternative
print([x for x in [1,2,3,4,5,6] if x%2 == 0])
print([x for x in fruit_list if len(x) > 5])

# --- 8. Building your own map function

def z_map(iterable,fn):
    res = []
    for item in iterable:
        res.append(fn(item))
    return res

print(z_map([1,2,3],lambda x:x*x))
