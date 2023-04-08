# print string
print ("string")

#len
a = "123"
print(len(a))

#op
s = "Hello World"

#reverse
print(s[::-1])

# Grab everything, but go in step sizes of 2
print(s[::2])

# multify
letter = 'z'
letter = letter * 10
print(letter)

# append
print (s + letter)

# different case
print(s.upper())

print(s.lower())

# split something
a = s.split("o")

print(a)

# insert another string 
print('Insert another string with curly brackets: {}'.format(s))

# format string % %
# \t -> tab

print('I wrote %s programs today.' %3.75)
print('I wrote %d programs today.' %3.75)   

# Padding and Precision of Floating Point Numbers

print('Floating point numbers: %5.2f' %(13.144))
print('Floating point numbers: %6.2f' %(13.144))

print('First: %s, Second: %5.2f, Third: %r' %('hi!',3.1415,'bye!'))

# format string {} 

# indexing
print('The {2} {1} {0}'.format('fox','brown','quick'))

# variable
print('First Object: {name}, Second Object: {b}, Third Object: {c}'.format(name=1,b='Two',c=12.3))


print('A %s saved is a %s earned.' %('penny','penny'))
# vs.
print('A {p} saved is a {p} earned.'.format(p='penny'))

# f - string

name = 'Fred'
name = 1

print(f"He said his name is {name}.")

