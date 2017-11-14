#_*_coding:utf-8_*_
# Author:Topaz
import os
output = open('a').read()
print(output)
# output = output.strip()
print("===================")
print(output)
print("===================")
for  item in output.split('\n'):
    key,value = item.split(':')
    print(key,value)