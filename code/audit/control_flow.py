from random import shuffle
from random import randint
# if elif else something:

loc = 'Bank'

if (loc == 'Auto Shop'):
    print('Welcome to the Auto Shop!')
elif (loc == 'Bank'):
    print('Welcome to the bank!')
else:
    print('Where are you?')

# for num in the list1

list1 = [1,2,3,4,5,6,7,8,9,10]
for num in list1:
    if num % 2 == 0:
        print(num)
    else:
        print('Odd number')

# input 
# number = int(input("Enter a number : \n"))
# print(number)

# tricky
list2 = [(2,3),(4,5),(6,7)]

# frist case : 
for list in list2:
    print(list)

# second case : 
for (t1,t2) in list2:
    print(t1)

# dictionary
# how to get the key value and item ? .keys() .values() .items() 
d = {'k1':1,'k2':2,'k3':3}

for k,v in d.items():
    print(k)
    print(v)


d2 = {'k1':1,'k2':4,'k3':3}
print(d2.items())
print(d2.keys())
print(d2.values())
print(sorted(d2.values()))


# while loop
x = 0
while x < 10:
    print('x is currently: ',x)
    print(' x is still less than 10, adding 1 to x')
    x+=1
    
else:
    print('All Done!')
    print(x)

#endless loop
cnt = 0
while True:
    print("I'm stuck in an infinite loop!")
    if(cnt == 10):
        print(cnt)
        break
    cnt+=1
    
# enumerate
for i,letter in enumerate('abcde'):
    print("At index {} the letter is {}".format(i,letter))

# random
mylist = [1,2,3,4,5]
print (shuffle(mylist))
print (randint(0,10))

# useful list (some op can build list very quickly)
lst1 = [x for x in 'word']
print(lst1)

lst2 = [x**2 for x in range(0,11)]
print(lst2)

lst3 = [x for x in range(11) if x % 2 == 0]
print(lst3)

celsius = [0,10,20.1,34.5]
fahrenheit = [((9/5)*temp + 32) for temp in celsius ]
print(fahrenheit)

# even can be nested

lst4 = [ x**2 for x in [x**2 for x in range(11)]]
print(lst4)

# ramdon list or tuple or dictionary : shuffle()

# create ramdom integer : randint(range begin, range ending)