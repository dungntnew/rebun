# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class CrawlerItem(scrapy.Item):
    title = scrapy.Field()
    link = scrapy.Field()
    text = scrapy.Field()
    tags = scrapy.Field()

    __table__ = 'rebun'
    __sql__ = 'INSERT INTO {0} ({1}) VALUES ({2})'

    def to_sql(self):
        return self.__sql__.format(
            self.__table__,
            ','.join(['`{0}`'.format(key) for key in self.keys()]),
            ','.join(['"{0}"'.format(value) for value in self.values()])
        )

    def __unicode__(self):
        return repr(self).decode('unicode_escape')
