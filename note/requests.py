import requests
import re
import json
 
data = {'some': 'data'}
headers = {'content-type': 'application/json',
           'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:22.0) Gecko/20100101 Firefox/22.0'}

first_url = "http://cn.bing.com/images/search?q=%E5%B0%91%E5%A5%B3&go=%E6%90%9C%E7%B4%A2&qs=ds&form=QBI"

response = requests.get(first_url,data=data,headers=headers)
print(response.status_code)
response.encoding = "utf-8"
html = response.text
reg = re.findall(r'quot;(.*?\.jpg)&quot',html,re.S)
print(reg)	

'''
requests

方法

requests.request(get|post|method,url,**kwargs')
requests.get()
requests.head()
requests.post()
.put
.patch
.delete

response
属性
r.status_code   #状态妈
r.encoding
r.text
r.apparent_encoding从内容分析
r.content二进制数据
