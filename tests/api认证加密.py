#_*_coding:utf-8_*_
# Author:Topaz
import hashlib
import time
KEY = '299095cc-1330-11e5-b06a-a45e60bec08b'
print(type(KEY))    #<class 'str'>
a = KEY.encode('utf-8')
print(type(a))  #<class 'bytes'>
b = a.decode()
print(type(b))  #<class 'str'>

ha = hashlib.md5(a) #2210bef23d69a4cac3d0c1c633c8cb9d
time_span = time.time()
ha.update(bytes("%s|%f" % (KEY, time_span), encoding='utf-8'))  #f0e057a2c2d64eb8b7b5fe8f1e3bf318
encryption = ha.hexdigest()
print(encryption)
result = "%s|%f" % (encryption, time_span)
print(result)
get_result  = result.split('|')
# print(type(get_result[1]))
# test = get_result[1]
# print(float(test))
if time.time() - float(get_result[1]) <10:
    my_time = float(get_result[1])
    my_key = '299095cc-1330-11e5-b06a-a45e60bec08b'
    a = hashlib.md5(my_key.encode('utf-8'))
    ha.update(bytes("%s|%f" % (my_key, my_time), encoding='utf-8'))  # f0e057a2c2d64eb8b7b5fe8f1e3bf318
    print(ha.hexdigest())
else:
    print("滚蛋")


