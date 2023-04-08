import math

class Animal:
    def __init__(self, name):    # Constructor of the class
        self.name = name

    def speak(self):              # Abstract method, defined by convention only
        raise NotImplementedError("Subclass must implement abstract method")


class Dog(Animal):
    
    def speak(self):
        return self.name+' says Woof!'
    
class Cat(Animal):

    def speak(self):
        return self.name+' says Meow!'
    
fido = Dog('Fido')
isis = Cat('Isis')

print(fido.speak())
print(isis.speak())


# more 

class Book:
    def __init__(self, title, author, pages):
        print("A book is created")
        self.title = title
        self.author = author
        self.pages = pages

    def __str__(self):
        return "Title: %s, author: %s, pages: %s" %(self.title, self.author, self.pages)

    def __len__(self):
        return self.pages

    def __del__(self):
        print("A book is destroyed")

book = Book("Python Rocks!", "Jose Portilla", 159)

#Special Methods
print(book)
print(len(book))
del book

# some test

# task1 line class
 
class Line:
    
    def __init__(self,coor1,coor2):
        self.coor1 = coor1
        self.coor2 = coor2

    def distance(self):
        return math.sqrt(math.pow((self.coor1[0] - self.coor2[0]),2) + math.pow((self.coor1[1] - self.coor2[1]),2))
    
    def slope(self):
        if(self.coor1[0] == self.coor2[0]) and (self.coor1[1] == self.coor2[1]):
            return "same point, no slope!"
        elif(self.coor1[0] == self.coor2[0]):
            return "inf"
        elif(self.coor1[1] == self.coor2[1]):
            return 0
        else:
            return (self.coor1[1] - self.coor2[1])/(self.coor1[0] - self.coor2[0])
    
line1 = Line((3,2),(8,10))
print("%.2f" %(line1.distance()))
print(line1.slope())


# task 2
class Cylinder:
    pi = 3.14
    def __init__(self,height=1,radius=1):
        self.height = height
        self.radius = radius
        
    def volume(self):
        return self.pi * math.pow(self.radius,2) * self.height
    
    def surface_area(self):
        return 2 * self.pi * self.radius * self.height + 2 * self.pi * math.pow(self.radius,2)

c = Cylinder(2,3)
print(c.volume())
print(c.surface_area())

# challenge 
class Account:

    def __init__(self, owner, balance = 0):
        self.owner = owner
        self.balance = balance
    
    def __str__(self):
        return ("Account owner: %s\n" %(self.owner)) +  ("Accont balance: $%s" %(self.balance))
    
    def deposit(self, deposit):
        print("Deposit Accepted")
        self.balance += deposit
    
    def withdraw(self, withdraw):
        if(withdraw >= self.balance):
            print("Funds Unavailable!")
        else:
            print("Withdrawal Accepted")
            self.balance -= withdraw

acct1 = Account('Jose',100)

print(acct1)
print(acct1.owner)
print(acct1.balance)

acct1.deposit(50)

acct1.withdraw(75)

acct1.withdraw(500)

