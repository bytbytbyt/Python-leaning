#!/usr/bin/python3

import sys

print ('参数个数为:', len(sys.argv), '个参数。')
print ('参数列表:', str(sys.argv))
print ('脚本名:', str(sys.argv[0]))
a = 3.
b = complex(2+3j)
print (a*b)
# if(len(sys.argv) >=2 )
# x = sys.argv[1]
# print(x)