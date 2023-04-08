my_dict = {"key1" : "mao ","key2" : "si ", "key3" : "yuan"}
for d in my_dict:
    print(my_dict[d], end = "")
print("\n")

# slicing in dictionary
dict1 = {"animal": "tiger","friut" : "apple","insect":"ant"}
slicing_list = ["animal","insect"]
slicing_dict = {key: dict1[key] for key in slicing_list}
print(slicing_dict)

# fromkeys

dict2 = dict1.fromkeys(dict1)
print(dict2)

# get
print(dict1.get("animal"))  
print(dict1.get("s"))  # return none
# print(dict1["s"])    # cause error

# add
numbers = {"one":1,"two":2}
numbers["three"] = 3
numbers.update({"four" : 4})
print(numbers)

numbers_new = {"five" : 5,"six":6}
numbers.update(numbers_new)
print(numbers)

# sorted use lambda

students = [('john', 'A', 15), ('jane', 'B', 12), ('dave', 'B', 10)]
sorted(students, key=lambda s: s[2])            # 按年龄排序
# sorted(students, key=students[2]) 
[('dave', 'B', 10), ('jane', 'B', 12), ('john', 'A', 15)]
print(students)