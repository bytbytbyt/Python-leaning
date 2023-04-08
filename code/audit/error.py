import math

# erroe and handing

# try - except

try:
    f = open('testfile','w')
    # f = open('testfile','r')
    f.write('Test write this')
except IOError:
    # This will only check for an IOError exception and then execute this print statement
    print("Error: Could not find file or read data")
else:
    print("Content written successfully")
    f.close()

 # finally

# def askint():
#     try:
#         val = int(input("Please enter an integer: "))
#     except:
#         print("Looks like you did not enter an integer!")

#     finally:
#         print("Finally, I executed!")
#     print(val)


def askint():
    while True:
        try:
            val = int(input("Please enter an integer: "))
        except:
            print("Looks like you did not enter an integer!")
            continue
        else:
            print("Yep that's an integer!")
            print(val)
            break
        finally:
            print("Finally, I executed!")
        print(val)
askint()

# fianlly will execute before continue, break or return in the try - catch - finally module (can within else)

# test time ！
# problem 1 

try:
    for i in ['a','b','c']:
        print(i**2)
except TypeError:
    print("unsupported operand type(s) for ** or pow(): 'str' and 'int'")
finally:
    print("check please!")

# problem 2

try:
    x = 5
    y = 0
    z = x/y
except ZeroDivisionError:
    print("the value of y can not be zero, check please !")
finally:
    print("All Done")

# problem 3

def ask():
    while True:
        try:
            num = int(input("Input an integer : "))
            square = math.pow(num, 2)
            print("Thank you, your number squared is %d" %(square))
            break
        except:
            print("An error occurred! Please try again!")
            continue
        else:
            pass
ask() 

class qp:
    def __init__(self,q  = 0, p = 0):
        self.q = q
        self.p = p

    def __str__(self):
        return ("q = %d and p = %d" %(self.q ,self.p))

list = [1,2,3]
o = qp(1,2)
list.append(o)
print(o)
print(list)
