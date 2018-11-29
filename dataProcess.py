#encoding=utf-8

import MySQLdb, sys, time, config
reload(sys)
sys.setdefaultencoding('utf-8')

class Query():
    def __init__(self):
        self.argv = param
        self.library = MySQLdb.connect(host=config.getDatabaseDSN(),user=config.getDatabaseUser(),passwd=config.getDatabasePwd(),db=config.getDatabase(),port=3306,charset='utf8')
        self.cursor = self.library.cursor()
        self.pool = redis.ConnectionPool(host=config.getRedisDsn(), port=config.getRedisPort(), password=config.getRedisPwd())
        self.cache = redis.Redis(connection_pool=self.pool)

    def login(email, pwd):
    	results = self.cursor.execute("select * from `rss_users` where `email` = %s"%str(email))
    	print results