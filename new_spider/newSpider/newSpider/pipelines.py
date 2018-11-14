# -*- coding: utf-8 -*-
import json
from scrapy.exceptions import DropItem
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class NewspiderPipeline(object):
    def __init__(self):
        self.count = 0
        self.file = open(r'newSpider/data/hudong_pedia.json', 'w',encoding='utf-8')

    # D:\人工智能一\项目\Agriculture_KnowledgeGraph农业知识图谱\new_spider\newSpider\newSpider\data\hudong_pedia.json
    def process_item(self, item, spider):
        if item['title'] != 'error':
            line = ""
            if (self.count > 0):
                line += ","
            # 用于将dict类型的数据转成str，因为如果直接将dict类型的数据写入json文件中会发生报错
            line += json.dumps(dict(item), ensure_ascii=False) + '\n'
            self.file.write(line)
            self.count += 1
            print("page count: " + str(self.count))
            return item
        else:
            raise DropItem("百科中找不到对应页面！")

    def open_spider(self, spider):
        self.file.write("[\n")
        print("==================开启爬虫 \"" + spider.name + "\" ==================")

    def close_spider(self, spider):
        self.file.write("\n]")
        print("==================关闭爬虫 \"" + spider.name + "\" ==================")
