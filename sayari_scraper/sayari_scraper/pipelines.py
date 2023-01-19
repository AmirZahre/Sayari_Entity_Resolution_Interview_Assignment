# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from scrapy.exceptions import DropItem


"""
Filters out the business names that do not begin with the letter X
This includes both lower and uppercase (x, X) letters.
To filter out lowercase X, remove the '.lower()' method in the if statement below.
"""
class ConfirmBusinessStartsWithX:
    def process_item(self, item, spider):
        business_name = str(item['business'][1]
                            ['Business Info']['TITLE'][0].split('\n')[0])
        if business_name.lower().startswith('x'):
            return item
        else:
            raise DropItem(
                f"Business '{business_name}' as it does not begin with the letter X.")
