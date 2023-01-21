# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from scrapy.exceptions import DropItem
import os
import mysql.connector
from datetime import datetime


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


class GoogleMySqlUpload:

    def __init__(self):
        self.date_today = datetime.today().strftime('%Y-%m-%d')

        print("UPLOADING ITEM")
        # credentials saved as env variables. source ~/.bash_profile 
        self.conn = mysql.connector.connect(
                host=os.environ['mysql_host'],
                user=os.environ['mysql_user'],
                password=os.environ['mysql_pass'],
                database=os.environ['mysql_db']
        )

        self.cur = self.conn.cursor()

        # create the table `scrapy_crawl_results` if it does not exist
        self.cur.execute("""
        CREATE TABLE IF NOT EXISTS scrapy_crawl_results (
            scrape_date DATE,
            business_name TEXT,
            owners TEXT,
            owner_name TEXT,
            commercial_registered_agent TEXT,
            registered_agent TEXT
        )
        """)
        self.conn.commit()

    # feed the item into the SQL Insert function
    def process_item(self, item, spider):
        self.store_db(item)
        return item

    # assign variable names to parsed item data, Insert to SQL table
    def store_db(self, item):
        additional_info_root = item['additional_information']['DRAWER_DETAIL_LIST']

        business_name = item['business'][1]['Business Info']['TITLE'][0].split('\n')[
            0]

        try:
            owners = additional_info_root['Owners'].split('\n')[0]
        except:
            owners = "NULL"

        try:
            owner_name = additional_info_root['Owner Name'].split('\n')[0]
        except:
            owner_name = "NULL"

        try:
            commercial_registered_agent = additional_info_root['Commercial Registered Agent'].split('\n')[
                0]
        except:
            commercial_registered_agent = "NULL"

        try:
            registered_agent = additional_info_root['Registered Agent'].split('\n')[
                0]
        except:
            registered_agent = "NULL"

        # additional logging of items to be inserted
        print("ITEMS TO BE UPLOADED: ", self.date_today, business_name, owners, owner_name,
              commercial_registered_agent, registered_agent)

        # upload items
        self.cur.execute(f"""
        INSERT into scrapy_crawl_results (scrape_date, business_name, owners, owner_name, commercial_registered_agent, registered_agent) 
        values ('{self.date_today}', "{business_name}", "{owners}", "{owner_name}", "{commercial_registered_agent}", "{registered_agent}")
        """)
        self.conn.commit()
