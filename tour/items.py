# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class TourItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    url = scrapy.Field()
    name =scrapy.Field()
    price =scrapy.Field()
    #description1 =scrapy.Field()
    day1= scrapy.Field()
    day2 =scrapy.Field()
    day3 =scrapy.Field()
    day4=scrapy.Field()
    day5 =scrapy.Field()
    day6 =scrapy.Field()
    day7 =scrapy.Field()
    day8 =scrapy.Field()
    day9 =scrapy.Field()
    day10 =scrapy.Field()
    day11 =scrapy.Field()
    day12 =scrapy.Field()
    day13 =scrapy.Field()
    day14 =scrapy.Field()
  
    rating= scrapy.Field()
    touroperator =scrapy.Field()
    maxgroupsize=scrapy.Field()
    physicalrating=scrapy.Field()
    age =scrapy.Field()
    operatedin=scrapy.Field()
    tourid=scrapy.Field()
    duration =scrapy.Field()
    #discount =scrapy.Field()
    
    citi =scrapy.Field()
    pass
