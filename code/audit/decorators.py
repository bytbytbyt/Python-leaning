# This part is for decorator (function in function)

s = 'Global Variable'

def check_for_locals():
    print(locals())

def hello(name = "Jack"):
    print("hello " + name)

hello()
greet = hello
greet()
del hello
# hello()
greet()

# function within function

def hello(name='Jose'):
    print('The hello() function has been executed')
    
    def greet():
        return '\t This is inside the greet() function'
    
    def welcome():
        return "\t This is inside the welcome() function"
    
    print(greet())
    print(welcome())
    print("Now we are back inside the hello() function")

hello()
# pat attention to the slope this code can cause error
# welcome()
del hello

# returning function

def hello(name='Jose'):
    
    def greet():
        return '\t This is inside the greet() function'
    
    def welcome():
        return "\t This is inside the welcome() function"
    
    if name == 'Jose':
        return greet
    else:
        return welcome

x = hello()
print(x)
print(x())

# function as Argument
del hello
def hello():
    return "Hi, Jack!"

def other(func):
    print("other code would be here")
    print(func())

other(hello)

# Decorator
def new_decorator(func):

    def wrap_func():
        print("Code would be here, before executing the func")

        func()

        print("Code here will execute after the func()")

    return wrap_func

# def func_needs_decorator():
#     print("This function is in need of a Decorator")

# # Reassign func_needs_decorator
# func_needs_decorator = new_decorator(func_needs_decorator)
# func_needs_decorator()

@new_decorator
def func_needs_decorator():
    print("This function is in need of a Decorator")

func_needs_decorator()