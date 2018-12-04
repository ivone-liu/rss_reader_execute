#encoding=utf-8

import tornado.ioloop
import tornado.web
from tornado import gen
from tornado.concurrent import run_on_executor
from concurrent.futures import ThreadPoolExecutor
import sys, json, hashlib, dataProcess
reload(sys)
sys.setdefaultencoding("utf-8")

#测试保留模块
class HelloHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello")

#登入模块
class SignInHandler(tornado.web.RequestHandler):
    def post(self):
        email = self.get_argument("email")
        password = self.get_argument("password")
        pwdType = hashlib.md5()
        pwdType.update(password+"reader")
        encode_pwd = pwdType.hexdigest()
        login = dataProcess.Query().login(email, encode_pwd)
        if login == False:
            result = json.dumps({"code":"500","message":"Failed to Sign In"})
        else:
            result = json.dumps({"code":"200","message":"Got it", "data":login})
        self.write("%s"%str(result))

#注册模块
class RegHandler(tornado.web.RequestHandler):  
    def post(self):
        email = self.get_argument("email")
        password = self.get_argument("password")
        name = self.get_argument("name")
        pwdType = hashlib.md5()
        pwdType.update(password+"reader")
        encode_pwd = pwdType.hexdigest()
        register = dataProcess.Query().register(email, encode_pwd, name)
        result = json.dumps(register)
        self.write("%s"%str(result))

#添加RSS模块
class AddRssSourceHandler(tornado.web.RequestHandler):  
    executor = ThreadPoolExecutor(40)
    @gen.coroutine
    def post(self):
        link = self.get_argument("link")
        user = self.get_argument("user")
        title = self.get_argument("title")
        desc = self.get_argument("desc")
        add = yield self.execute(link, user, title, desc)
        result = json.dumps(add)
        self.write("%s"%str(result))

    @run_on_executor
    def execute(self, link, user, title, desc):
        addRss = dataProcess.Query().addRss(link, user, title, desc)
        return addRss


#读取新数据模块
class GetArticleFromSourceHandler(tornado.web.RequestHandler):  
    executor = ThreadPoolExecutor(40)
    @gen.coroutine
    def get(self):
        last_time = self.get_argument("last")
        channel = self.get_argument("channel")
        data = yield self.execute(last_time, channel)
        result = json.dumps({"code":"200","message":"Got it","data":data})
        self.write("%s"%str(result))

    @run_on_executor
    def execute(self, last_time, channel):
        data = dataProcess.Query().getArticles(last_time, channel)
        return data

#苦工，起到遍历作用
class LaborHandler(tornado.web.RequestHandler):    
    executor = ThreadPoolExecutor(40)
    @gen.coroutine
    def get(self):
        yield self.execute()
        
    def execute(self):
        dataProcess.Query().loop()

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
