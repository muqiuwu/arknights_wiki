# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class DoubanItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    cname = scrapy.Field()
    ename = scrapy.Field()
    jname = scrapy.Field()
    code = scrapy.Field()
    sub_occupation = scrapy.Field()
    influnce = scrapy.Field()
    place_of_birth = scrapy.Field()
    race = scrapy.Field()
    hp = scrapy.Field()
    atk = scrapy.Field()
    defe = scrapy.Field()
    res = scrapy.Field()
    re_deploy = scrapy.Field()
    cost = scrapy.Field()
    block = scrapy.Field()
    interval = scrapy.Field()
    sex = scrapy.Field()
    position = scrapy.Field()
    obtain = scrapy.Field()
    tag = scrapy.Field()
    feature=scrapy.Field()
    pass
