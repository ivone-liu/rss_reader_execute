#encoding=utf-8

import MySQLdb, sys, time, config
reload(sys)
sys.setdefaultencoding('utf-8')

class Query():
    def __init__(self):
        self.library = MySQLdb.connect(host=config.getDatabaseDSN(),user=config.getDatabaseUser(),passwd=config.getDatabasePwd(),db=config.getDatabase(),port=3306,charset='utf8')
        self.cursor = self.library.cursor()
        # self.pool = redis.ConnectionPool(host=config.getRedisDsn(), port=config.getRedisPort(), password=config.getRedisPwd())
        # self.cache = redis.Redis(connection_pool=self.pool)

    def login(self, email, pwd):
    	results = self.cursor.execute("select id, email, password from `rss_users` where `email` = '%s'"%str(email))
    	user = self.cursor.fetchone()
    	self.cursor.close()
    	if user != None and user[2] == pwd:
    		return {'id':user[0], 'email':user[1]}
    	else:
    		return False

    def register(self, email, pwd):
    	results = self.cursor.execute("select id from `rss_users` where `email` = '%s'"%str(email))
    	exist = self.cursor.fetchone()
    	if exist != None:
    		return {'code':500, 'message':'Email address already exists!'}
    	else:
    		self.cursor.execute("insert into `rss_users` (`email`, `password`) values ('%s','%s')"%(str(email),str(pwd)))
    		self.library.commit()
    		self.cursor.close()
    		return {'code':200, 'message':'Got it'}