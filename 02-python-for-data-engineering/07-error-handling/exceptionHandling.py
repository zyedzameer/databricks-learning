'''
Handling unexpected runtime error, instead of failing the app either continue with
other way or exit gracefully with proper logs

Python structure for exception handling -> try - except - else - finally

try -> actual code trying
except -> invoke when an exception occurs
else -> if no exception occurs
finally -> exception or not, execute always

'''

exe_example = int(input("Which example to run: "))

if exe_example == 1:
    print("*********** Exception handling with generic string output for every exception...")
    try:
        num = int(input("Enter a number :"))
        div = int(input("Enter a divider:"))
        result = num // div
        print(result)
    except:
        print("Oops..! Something went wrong:")

elif exe_example == 2:
    print("*********** Exception handling with generic string output for every exception and also print the exception message...")
    try:
        num = int(input("Enter a number :"))
        div = int(input("Enter a divider:"))
        result = num // div
        print(result)
    except Exception as e:
        print("Oops..! Something went wrong:")
        print(e)

elif exe_example == 3:
    print("*********** Exception handling with specific exception handling for each exception type and also print the exception message...")
    try:
        num = int(input("Enter a number :"))
        div = int(input("Enter a divider:"))
        result = num // div
        print(result)
    except ValueError as ve:
        print("value error occured, error msg: " + str(ve))
    except ZeroDivisionError as zde:
        print("ZeroDivisionError occured , error msg: " + str(zde))
    except Exception as e:
        print("Oops..! Something went wrong:" + str(e))

elif exe_example == 4:
    print("*********** Exception handling with else block to execute code when no exception occurs...")
    try:
        num = int(input("Enter a number :"))
        div = int(input("Enter a divider:"))
        result = num // div
        print(result)
    except Exception as e:
        print("Oops..! Something went wrong:")
    else:
        print("Division performed successfully, result is :" + str(result))

elif exe_example == 5:
    print("*********** Exception handling with else and finally block to execute code when no exception occurs and also execute code in finally block...")
    try:
        num = int(input("Enter a number :"))
        div = int(input("Enter a divider:"))
        result = num // div
        print(result)
    except Exception as e:
        print("Oops..! Something went wrong:")
    else:
        print("Division performed successfully, result is :" + str(result))
    finally:
        print("This will get executed no matter what, exception or not")

#use raise to throw an error

elif exe_example == 6:
    age = int(input("Enter age :"))
    print("Use raise to throw an error if age is less than 18")
    if age >= 18:
        print("You are old enough to vote")
    else:
        raise Exception("You are not old enough to vote")

elif exe_example == 7:
    try:
        age = int(input("Enter age :"))
        if age >= 18:
            print("You are old enough to vote")
        else:
            raise Exception("You are not old enough to vote")
    except Exception as e:
        print("Error: " + str(e)) #handling the raised exception and printing the error message gracefully