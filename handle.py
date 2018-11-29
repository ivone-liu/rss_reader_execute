#encoding=utf-8

import tornado.ioloop
import tornado.web
import sys, json, hashlib, dataProcess
reload(sys)
sys.setdefaultencoding('utf-8')

#测试保留模块
class HelloHandler(tornado.web.RequestHandler):
    self.write("Hello")

#登入模块
class SignInHandler(tornado.web.RequestHandler):
    def post(self):
        email = self.get_argument('email')
        password = self.get_argument('password')
        pwdType = hashlib.md5()
        pwdType.update(password)
        encode_pwd = pwdType.hexdigest()


#注册模块
class RegHandler(tornado.web.RequestHandler):  

#添加RSS模块
class AddRssSourceHandler(tornado.web.RequestHandler):  

#读取新数据模块
class GetArticleFromSourceHandler(tornado.web.RequestHandler):  

#苦工，起到遍历作用
class LaborHandler(tornado.web.RequestHandler):    

#路由设置
def make_app():
    return tornado.web.Application([
        (r"/", HelloHandler),
        (r"/signin",SignInHandler),
        (r"/reg",RegHandler),
        (r"/addRss",AddRssSourceHandler),
        (r"/getArticles",GetArticleFromSourceHandler),
        (r"/labor",LaborHandler),
    ])

if __name__ == "__main__":
    app = make_app()
    app.listen(8000)
    tornado.ioloop.IOLoop.current().start()
