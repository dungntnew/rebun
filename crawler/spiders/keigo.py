import scrapy
from crawler.items import CrawlerItem
import logging

logger = logging.getLogger(__name__)


class KeigoSpider(scrapy.Spider):
    name = "keigo"
    allowed_domains = ["xn--gdvx14f.xn--fsqv94c.jp", ]
    start_urls = ['http://xn--gdvx14f.xn--fsqv94c.jp', ]

    def parse(self, response):
        for href in response.css('#side dl.side-catlist a::attr("href")'):
            url = response.urljoin(href.extract())
            yield scrapy.Request(url, callback=self.parse_contents)

    def parse_contents(self, response):
        item = CrawlerItem()
        item['title'] = response.css('#content > h1::text').extract_first()
        item['text'] = ''.join(response.css('#e-body> p, blockquote').extract())
        item['tags'] = ','.join(response.css('#entry-tags a::text').extract())
        yield item
