#encoding=utf-8

import tornado.ioloop
import tornado.web
import sys, json, hashlib, dataProcess
reload(sys)
sys.setdefaultencoding('utf-8')

#测试保留模块
class HelloHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello")

#登入模块
class SignInHandler(tornado.web.RequestHandler):
    def post(self):
        email = self.get_argument('email')
        password = self.get_argument('password')
        pwdType = hashlib.md5()
        pwdType.update(password+'reader')
        encode_pwd = pwdType.hexdigest()
        login = dataProcess.Query().login(email, encode_pwd)
        if login == False:
            result = json.dumps({'code':'500','message':'Failed to Sign In'})
        else:
            result = json.dumps({'code':'200','message':'Got it', 'data':login})
        self.write("%s"%str(result))

#注册模块
class RegHandler(tornado.web.RequestHandler):  
    def post(self):
        email = self.get_argument('email')
        password = self.get_argument('password')
        pwdType = hashlib.md5()
        pwdType.update(password+'reader')
        encode_pwd = pwdType.hexdigest()
        register = dataProcess.Query().register(email, encode_pwd)
        self.write("%s"%str(register))

#添加RSS模块
class AddRssSourceHandler(tornado.web.RequestHandler):  
    def get(self):
        print self.get_argument()

#读取新数据模块
class GetArticleFromSourceHandler(tornado.web.RequestHandler):  
    def get(self):
        print self.get_argument()

#苦工，起到遍历作用
class LaborHandler(tornado.web.RequestHandler):    
    def get(self):
        print self.get_argument()

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
