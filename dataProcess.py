#encoding=utf-8

import MySQLdb, sys, time, config, urllib, urllib2, xml.dom.minidom
reload(sys)
sys.setdefaultencoding('utf-8')

class Query():
    def __init__(self):
        self.library = MySQLdb.connect(host=config.getDatabaseDSN(),user=config.getDatabaseUser(),passwd=config.getDatabasePwd(),db=config.getDatabase(),port=3306,charset='utf8')
        self.cursor = self.library.cursor()
        # self.pool = redis.ConnectionPool(host=config.getRedisDsn(), port=config.getRedisPort(), password=config.getRedisPwd())
        # self.cache = redis.Redis(connection_pool=self.pool)

    def login(self, email, pwd):
    	results = self.cursor.execute("select id, email, password, name from `rss_users` where `email` = '%s'"%str(email))
    	user = self.cursor.fetchone()
    	if user != None and user[2] == pwd:
    		return {'id':user[0], 'email':user[1], 'name':user[3]}
    	else:
    		return False

    def register(self, email, pwd, name):
    	results = self.cursor.execute("select id from `rss_users` where `email` = '%s'"%str(email))
    	exist = self.cursor.fetchone()
    	if exist != None:
    		return {'code':500, 'message':'Email address already exists!'}
    	else:
    		self.cursor.execute("insert into `rss_users` (`email`, `password`, `name`) values ('%s','%s', '%s')"%(str(email), str(pwd), str(name)))
    		self.library.commit()
    		return {"code":200, "message":"Got it", "data":{"id":"%d"%self.cursor.lastrowid}}

    def addRss(self, url, user, title, desc):
		try:
			self.cursor.execute("insert into `rss_subscribe` (`user_id`, `rss_source`, `title`, `desc`, `add_time`, `last_update`) values ('%s','%s','%s','%s','%s','%s')"%(str(user), str(url), str(title), str(desc), str(int(time.time())), str(int(time.time()))))
			self.library.commit()
			return {"code":"200", "message":"已订阅！"}
		except:
			return {"code":"200", "message":"已订阅！"}

    def getArticles(self, last_update, channel_id):
    	results = self.cursor.execute("select * from `rss_data` where `channel_id`='%s' and `create_time` > %s"%(str(channel_id),str(last_update)))
    	data = self.cursor.fetchmany(results)
    	news = {}
    	for i in data:
    		item = {}
    		item['title'] = i[2]
    		item['desc'] = i[3]
    		item['link'] = i[4]
    		item['channel_id'] = i[1]
    		news['item_%s'%str(i[0])] = item
    	return news

    def loop(self):
    	subscribe = self.cursor.execute("select id, rss_source from `rss_subscribe`")
    	channels = self.cursor.fetchmany(subscribe)
    	for channel in channels:
			release = urllib2.urlopen(channel[1]).read()
			doc = xml.dom.minidom.parseString(release)
			items = doc.documentElement.getElementsByTagName("item")
			for item in items:
				title = item.getElementsByTagName("title")
				title = title[0].childNodes[0].data
				desc = item.getElementsByTagName("description")
				desc = desc[0].childNodes[0].data
				link = item.getElementsByTagName("link")
				link = link[0].childNodes[0].data
				# print 'insert into `rss_data` (`channel_id`, `title`, `desc`, `link`, `create_time`) values ("%s",\'%s\',\'%s\',"%s","%s")'%(str(channel[0]),str(title), str(desc), str(link), str(int(time.time())))
				try:
					self.cursor.execute('insert into `rss_data` (`channel_id`, `title`, `desc`, `link`, `create_time`) values ("%s",\'%s\',\'%s\',"%s","%s")'%(str(channel[0]),str(title), str(desc), str(link), str(int(time.time()))))
					self.library.commit()
				except:
					continue

    def longToInt(self,value):
        if value > 2147483647 :
            return (value & (2 ** 31 - 1))
        else :
            return value

    def __del__(self):
    	self.cursor.close()
    	self.library.close()