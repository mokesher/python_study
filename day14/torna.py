#!/usr/bin/env python 
# -*- coding:utf-8 -*-

import tornado.web
class MainHandler(tornado.web.RequestHandler):
    def get(self):
        u = self.get_argument('user')
        p = self.get_argument('pwd')
        if u =='moke' and p =='123':
            self.write("ojbk")
        else:
            self.write("out")
    def post(self):
        print(123)
        self.write('POST')

application = tornado.web.Application([
    (r"/index",MainHandler),
])

if __name__ == "__main__":
    application.listen(8800)
    tornado.ioloop.IOLoop.instance().start()
