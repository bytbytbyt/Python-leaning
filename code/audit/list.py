# almost hold different type
my_list = ['A string',23,100.232,'o']
print(len(my_list))

#indexing 
print(my_list[0])
print(my_list[1:])
print(my_list[:3])

# not change the original one
my_list + ['new item']
print(my_list)
my_list = my_list * 2
print(my_list)

# append and pop (remove)
list1 = [1,2,3]
list1.append("add one")
print(list1)
list1.pop(3)
print(list1)
list1.insert(2,'2')
print(list1)
# traditional get the lastest indexing
popped_item = list1.pop()
print(popped_item)

# caues indecxing error
# print(list1[100])

# revease and sorted
new_list = ['a','e','x','b','c']

new_list.reverse()
print(new_list)
new_list.sort()
print(new_list)

# print("try : " + new_list[-6])

# nesting list

# Let's make three lists
lst_1=[1,2,3]
lst_2=[4,5,6]
lst_3=[7,8,9]

# Make a list of lists to form a matrix
matrix = [lst_1,lst_2,lst_3]

print(matrix)

first_col = [row[0] for row in matrix]

print(first_col)