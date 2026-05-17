def calc_sum(num1, num2):
    """Calculate the sum of two numbers and return it."""
    return num1 + num2

result = calc_sum(5, 10) #positional arguments
print(result)

result = calc_sum(num2=6,num1=5) # keyword arguments (note how the position of the arguments doesn't matter)
print(result)

#note - python won't allow positional arguments after keyword arguments.

def get_sum(a,b,c):
    return a + b + c

print(get_sum(2,3,4)) #positional
print(get_sum(a=2, b=3, c=4)) #keyword
print(get_sum(2, b=3, c=4)) #mix of positional and keyword (positional must come first)
print(get_sum(2, c=4, b=3)) #mix of positional and keyword (positional must come but keyword order does not matter)

# a function with default argument

def get_sum_with_discount(price,discount=0.1):
    """Calculate the final price after applying a discount (default 10%)"""
    final_price = price * (1 - discount)
    return final_price

print(get_sum_with_discount(100))  # uses default discount
print(get_sum_with_discount(100, 0.2))  # uses provided discount

# a custom range function with default start and stop args

def custom_range(stop,start=1,step=1):
    lst_res=[]
    counter = start
    while counter <= stop:
        lst_res.append(counter)
        counter += step
    return lst_res

print(custom_range(5))
print(custom_range(100, start=10, step=10))

# *args - variable length positional arguments

def get_sum_var_args(*args):
    return sum(args)

print(get_sum_var_args(1, 2, 3))

'''
note - sum function excepts an iterable , not unpacked value like below. (common error)
def get_sum_var_args(*args):
    return sum(*args)

'''

# **kwargs - variable length keyword arguments

def keywordArgs(**kwargs):
    return kwargs #accepts any number of arguments and return them as dictionary

result = keywordArgs(name="Bob",city="New York",zip=10001)
print(result)

'''
note : 
keywordArgs("name"="Bob","city"="New York","zip"=10001)) --> this will throw an error because you cannot use
keyword arguments without unpacking them.
keywordArgs("name":"Bob","city":"New York","zip":10001) --> this will also throw an error because it's not a valid
syntax for keyword arguments.
'''

data = {"name":"Bob","city":"New York","zip":10001}
result2 = keywordArgs(**data) #example of passing a dictionary using ** to unpack as keyword arguments
print(result2)

# *args , **kwargs together

def greetWithargsKwargs(*args,**kwargs):
    print(args)
    print(kwargs)

greetWithargsKwargs("Hello","Hi",name="Alice",city="NYC")

def emailIDGenerator(**kwargs):
    fname = str(kwargs.get("fname")).lower()
    lname = str(kwargs.get("lname")).lower()
    domain = str(kwargs.get("domain","unknown")).lower()
    email = (f"your email ID is {fname}.{lname}@{domain}.com")
    print(email)

emailIDGenerator(fname="Bob",lname="Johnson",domain="yahoo")
emailIDGenerator(fname="Alice",lname="Smith") # domain will use default value "unknown"