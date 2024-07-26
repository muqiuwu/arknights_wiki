# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from pymongo import MongoClient

class DoubanPipeline:
    def __init__(self):
        self.client = MongoClient('mongodb://localhost:27017/')
        self.mongodb = self.client['quotes']
        self.collection = self.mongodb['quotes']

    def process_item(self, item, spider):
        if item is not None:  # 检查项目是否为空
            # 检查和处理项目的数据类型和结构，确保与MongoDB文档的需求匹配
            processed_item = self.process_data(item)
            if processed_item:
                self.collection.insert_one(processed_item)
        return item

    def process_data(self, item):
        # 在这里处理项目数据，确保它符合数据库的预期格式和类型
        # 例如，可以进行字段转换、数据清洗或其他必要的预处理
        processed_item = dict(item)  # 简单地将项目转换为字典，可以根据需要进行更复杂的转换
        return processed_item
    
    # def process_item(self, item, spider):
    #     document = self.mongodb['quotes']
    #     document.insert_one(dict(item))
    #     return item