from random import shuffle

# Form : object.method(argc1 , argc2 ....)
lst = [1,2,3,4,5]
lst.append(6)

# Get down to brass tacks
def say_hello():
    print('hello')

def say_yes():
    print('yes')

say_hello()
say_yes()

# show it is a function
# say_hello
print(say_hello)

def greeting(name):
    print(f'Hello {name}')

greeting("byt")

def add_num(num1,num2):
    return num1+num2

def even_check(number):
    return number % 2 == 0

def check_even_list(num_list):
    # Go through each number
    for number in num_list:
        # Once we get a "hit" on an even number, we return True
        if number % 2 == 0:
            return True
        # This is WRONG! This returns False at the very first odd number!
        # It doesn't end up checking the other numbers in the list!
        else:
            return False
        
print(check_even_list([2,4,6,8]))

# can return list
def check_even_list(num_list):
    
    even_numbers = []
    
    # Go through each number
    for number in num_list:
        # Once we get a "hit" on an even number, we append the even number
        if number % 2 == 0:
            even_numbers.append(number)
        # Don't do anything if its not even
        else:
            pass
    # Notice the indentation! This ensures we run through the entire for loop    
    return even_numbers

print(check_even_list([1,2,3,4,5,6]))

examples = [1,2,3,4,5,6]

print(examples)
shuffle(examples)
print(examples)

# map quickly call every objects in a list or some set to invoke the same function
def splicer(mystring):
    if len(mystring) % 2 == 0:
        return 'even'
    else:
        return mystring[0]
    
mynames = ['John','Cindy','Sarah','Kelly','Mike']

print(list(map(splicer,mynames))) # can return also be a list

# filter only return the true expression  

# Lambda -  macro in c/c++ ? 
def square(num): return num**2

print((square(2) == 4 ))

s = lambda num: num ** 2
print(s(2))

# range can be replace with the intial and end value in the for cycle

# scope
x = 25

def printer():
    x = 50
    return x

print(x)
print(printer())
print(x)

