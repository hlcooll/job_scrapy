# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import MySQLdb
import MySQLdb.cursors
from twisted.enterprise import adbapi

class JobPipeline(object):
    def process_item(self, item, spider):
        return item
# //同步
class MysqlPipeline(object):
    def __init__(self):
        self.conn=MySQLdb.connect('127.0.0.1','root','','job',charset="utf8",use_unicode=True)
        self.cursor=self.conn.cursor()


    def process_item(self,item,spider):
        insert_sql="""
            insert into python_job(position,salary,t_company,address,touch,url)
            VALUES (%s,%s,%s,%s,%s,%s)
        """
        self.cursor.execute(insert_sql,(item["position"],item["salary"],item["t_company"],item["address"],item["touch"],item["url"]))
        self.conn.commit()

# //异步
class MysqlPipelineY(object):
    def __init__(self,dbpool):
        self.dbpool=dbpool
    @classmethod
    def from_settings(cls,settings):
        dbparms=dict(
                    host=settings["MYSQL_HOST"],
                    db = settings["MYSQL_DBNAME"],
                    user = settings["MYSQL_USER"],
                    password = settings["MYSQL_PASSWORD"],
                    charset='utf8',
                    cursorclass=MySQLdb.cursors,
                    use_unicode=True,
        )
        dbpool=adbapi.ConnectionPool("MySQLdb",**dbparms)

        return cls(dbpool)

    def process_item(self,item,spider):
        #使用twisted 将mysql插入变成异步执行
        query=self.dbpool.runInteraction(self.do_insert,item)
        query.addErrback(self.handle_error,item,spider)

    def do_insert(self,cursor,item):
        insert_sql="""
            insert into python_job(position,salary,t_company,address,touch,url)
            VALUES (%s,%s,%s,%s,%s,%s)
        """
        cursor.execute(insert_sql,(item["position"],item["salary"],item["t_company"],item["address"],item["touch"],item["url"]))
    def handle_error(self,failure,item,spider):
         #处理异步异常
         print(failure+"++++这是错误++++")


