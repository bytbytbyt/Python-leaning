# type()

a, b, c, d = 20, 5.5, True, 4+3j
print(type(a), type(b), type(c), type(d))
print('----------------------------')

# isinstance
e = 111
print(isinstance(e,int))
print('----------------------------')

# superclass and subclass
class A:
    pass
class B(A):
    pass

print(isinstance(A(),A))
print(type(A()) == A)

print(isinstance(B(),A))
print(type(B()) == A)
print('----------------------------')

# issubclass 
print(issubclass(bool,int))
print(issubclass(B,A))
print('----------------------------')
print("True and False")
True == 1
False == 0
