print('\n ****************** Decorator example ***************************\n')


# step 1 - Declare function: hello_decorator(func).
# step 4 - Run hello_decorator(func) with function_to_be_used() as a parameter.
def hello_decorator(func):
    # step 5 - Run 1 line of hello_decorator(function_to_be_used), declare inner().
    # step 7 - Run function inner().
    def inner():
        # step 8 - Run 1 line of inner(); print("Hello, this is before function execution").
        print("Hello, this is before function execution")
        # step 9 - Run 2 line of inner(); call function_to_be_used().
        func()
        # step 12 - Run 3 line of inner();  print("This is after function execution").
        print("This is after function execution")

    # step 6 - Call 2 line of hello_decorator(function_to_be_used), run inner1().
    return inner()


# step 2 - Declare function: function_to_be_used().
# step 10 - Run function inner().
def function_to_be_used():
    # step 11 - Run 1 line of run function inner();  print("This is inside the function !!").
    print("This is inside the function !!")


# step 3 - Call function: hello_decorator(function_to_be_used).
hello_decorator(function_to_be_used)
# step 13 Functions execution are finished; print('all done').
print('\nAll done\n')

# *********************** Decorator declaration using "@" notation ********************
# Same function with same decorator using "@" notation to declare hello_decorator(func)
# as a decorator to function_to_be_used() when this is defined.
# *************************************************************************************

print('\n ****************** Same example using "@" notation ************************\n')


def hello_decorator(func):
    def inner():
        print("Hello, this is before function execution")
        func()
        print("This is after function execution")

    # First difference (return the inner function not call it).
    return inner


# Second difference declare hello_decorator as a decorator for function_to_be_used().
# when we define function_to_be_used().
@hello_decorator
def function_to_be_used():
    print("This is inside the function !!")


# Third and last difference run function_to_be_used() normal
# instead passing it as a parameter to  hello_decorator().
# hello_decorator(function_to_be_used) this is not necessary
function_to_be_used()

print('\nAll done\n')

# ******** My conclusions ************************************************************
# From my knowledge the decorators are wrapper used to modify behavior of a function mainly
# by adding code before and/or after the decorated function or modify the arguments passed
# to it. They contain an inner function that wrap around the decorated function and can be executed
# before or after the decorated function is called
# *************************************************************************************
