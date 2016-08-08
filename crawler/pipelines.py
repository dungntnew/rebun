# -*- coding: utf-8 -*-

import MySQLdb
from crawler.settings import dbconf


class CrawlerPipeline(object):
    def __init__(self):
        pass

    def process_item(self, item, spider):
        return item


class MySQLStorePipeline(object):
    def __init__(self):
        self.conn = MySQLdb.connect(**dbconf)
        self.cursor = self.conn.cursor()

    def process_item(self, item, spider):
        try:
            query = item.to_sql()
            spider.logger.info(query)
            self.cursor.execute(query)
            self.conn.commit()
        except MySQLdb.Error as e:
            print("Error %d: %s" % (e.args[0], e.args[1]))

        return item
