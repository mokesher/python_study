'''
json:python中字典 列表数据类型转换为字符串
dumps
转换为字符串
反序列化
loads—>>转换为dict

pickle和json一样
'''
import json
obj = {'one':1,'two':2,'three':3}
encoded = json.dumps(obj)
print(type(encoded))
print(encoded)

decoded = json.loads(encoded)
print(type(decoded))
print(decoded)
