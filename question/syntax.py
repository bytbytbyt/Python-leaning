# str

# 1 only string can use operator +=
str1 = "hello"
str2 = "world"
str3 = str1 + str2

print(str3)

# 2 format string
 
# (1) % num1.num2f (num1: total len, if not enough ,black compensation , num2 : digits output

print('First: %s, Second: %5.2f, Third: %r' %('hi!',3.1415,'bye!'))

# (2) even allow different type in {}

print('The {2} {1} {0}'.format(1 + 2j,'brown','quick'))

# (3) f - string

name = 'Fred'
# name = 1
print(f"He said his name is {name}.")
# 3 spilt
s = 'hohohoo'.split('h') 
print(s)

# list 

# only append | insert | extend can add  element , + list  += is not available
list = [1,2,3]
# can add integer , but will add list tuple dictionary as an integral whole 
list.append(4)
list.append([5,6])
list.append((90,93))
list.append({"!":1})
print(list)
# can not  integer , but will add list tuple dictionary as parts
list.extend('c')
list.extend(["java", "cpp"])
print(list)
# insert(position, obj)
list.insert(5,5)
print(list)
# add list
list = list + [7]
print(list)

# list += 8 # error

# package 
# use method from different package , don't forget the class name when invoking  
# for example:
# import math
# num = (math).pow(2,3)
