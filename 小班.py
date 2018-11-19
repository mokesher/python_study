#!/usr/bin/env python
# -*- coding:utf-8 -*-
import requests,json,re,threading
url_list = ["http://www.wassk.cn/ssk-ssqr-hybrid/index.html?b=B20150609164118729107#/home/books",
            "http://www.wassk.cn/ssk-ssqr-hybrid/index.html?b=B20150609164742556377#/home/books",
            "http://www.wassk.cn/ssk-ssqr-hybrid/index.html?b=B20150609164909564774",
            "http://www.wassk.cn/ssk-ssqr-hybrid/index.html?b=B20150609164905717324#/home/books",
            "http://www.wassk.cn/ssk-ssqr-hybrid/index.html?b=B20150609164915888313#/home"
            ]

def run(url):
    num = re.split("=|#",url)[1]
    u1 = "http://www.wassk.cn/ssk-ssqr-web/mobile/exec?m=getBookInfo&bookNumber={}&noGoods=true&webver=1.0".format(num)
    u1_text = requests.get(u1).text
    u1_text = json.loads(u1_text)
    bookId = u1_text["data"][0]["bookId"]
    for page in [1,2]:
        u2 = "http://www.wassk.cn/ssk-ssqr-web/mobile/exec?m=getGoodsOfBook&bookId={}&page={}&rows=10&webver=1.0".format(bookId,page)
        u2_text = requests.get(u2).text
        codeNumber = json.loads(u2_text)["data"]
        for i in codeNumber:
            codeNumber = i["codeNumber"]
            u3 = "http://www.wassk.cn/ssk-ssqr-web/mobile/exec?m=getGoodsInfo&S=&codeNumber={}&dataType=json&userId=&webver=1.0".format(codeNumber)
            u3_text = requests.get(u3).text
            u3_text = json.loads(u3_text)
            u3_text = u3_text["data"][0]["goodsContent"]
            mp3_src = json.loads(u3_text)["content"][0]["src"]
            audioTitle = json.loads(u3_text)["content"][0]["audioTitle"]
            print(audioTitle)
            with open("%s.mp3"%(audioTitle), "wb") as down:
                down.write(requests.get(mp3_src).content)
for i in url_list:
    run(i)
print("下载完毕")