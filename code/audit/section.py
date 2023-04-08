# 1 map(function, iterable) return a list of iterable
# single paremeter

def fahrenheit(celsius):
    return (9/5)*celsius + 32
    
temps = [0, 22.5, 40, 100]

F_temps = list(map(lambda x: (9/5)*x + 32, temps))
print(F_temps)

# multiple iterable
# map(function,iterable1,iterable2...)

a = [1,2,3,4]
b = [5,6,7,8]
c = [9,10,11,12]

print(list(map(lambda x,y:x+y,a,b)))

print(list(map(lambda x,y,z:x+y+z,a,b,c)))


# 2 reduce(function,list) return single value
from functools import reduce
lst = [47,11,42,13]
print(reduce(lambda x,y: x+y,lst))

#Find the maximum of a sequence (This already exists as max())
# 三目运算符 !!!
max_find = lambda a,b: a if (a > b) else b
print(reduce(max_find,lst))


# 3 filter(function,list) return boolen (only true returned just like filter )
def even_check(num):
    if num%2 ==0:
        return True

lst =range(20)

print(list(filter(even_check,lst)))
print(list(filter(lambda x: x%2==0,lst)))

# 4 zip return several 

x = [1,2,3]
y = [4,5,6,7,8]

# zip the lists together
print(list(zip(x,y)))

d1 = {'a':1,'b':2}
d2 = {'c':4,'d':5}

# for dictionary return keys
print(list(zip(d1,d2)))
print(list(zip(d1.values(),d2)))
print(list(zip(d1.values(),d2.values())))

def switcharoo(d1,d2):
    dout = {}
    
    for d1key,d2val in zip(d1,d2.values()):
        dout[d1key] = d2val
    
    return dout

print(switcharoo(d1,d2))


# 5 enumerate()

lst = ['a','b','c']
# print(type('s'))
for number,item in enumerate(lst):
    print(number) # print indexes
    print(item)   # print values

# useful for tracker
for count,item in enumerate(lst):
    if count >= 2:
        break
    else:
        print(item)

months = ['March','April','May','June']
# different start
print(list(enumerate(months,start=3)))

# all() (all True -> True)& any())(any True -> True)
lst = [True,True,False,True]
print(all(lst))
print(any(lst))

# complex
print(complex(2,3))
print(complex(10,1))
print(complex('3+4j'))
print(complex('1+j'))

# some test
# p1
words = ('How long are the words in this phrase')

def word_lengths(phrase):
    lst = phrase.split(' ')
    return list(map(lambda x : len(x),lst))

print(word_lengths(words))

# p2
digits = ([3,4,3,2,1])
def digits_to_num(digits):
    return(reduce(lambda x,y : x*10+y,digits))

print(digits_to_num(digits))    

# p3
def filter_words(word_list, letter):
    return list(filter(lambda x: x[0] == letter,word_list))
l = ['hello','are','cat','dog','ham','hi','go','to','heart']
print(filter_words(l,'h'))

# p4
def concatenate(L1, L2, connector):
    lout = []
    # for index, d1, d2 in (L1.keys(),zip(L1.values(),L2.values())):
    #     lout[index] = 
    for s1,s2 in zip(L1,L2):
        lout.append(s1 + connector + s2)
    return lout
print(concatenate(['A','B'],['a','b'],'-'))
# p5
def d_list(L):
    dout = {}
    for index,value in enumerate(L):
        dout[index] = value
        # dout[value] = index
    return dout

print(d_list(['a','b','c']))

# p6
def cout_match_index(L):
    count = 0
    for index,value in enumerate(L):
        if index == value:
            count = count + 1
    return count

print(cout_match_index([0,2,2,1,5,5,6,10]))