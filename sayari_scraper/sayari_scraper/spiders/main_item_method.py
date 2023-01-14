# task: https://gist.github.com/jvani/57200744e1567f33041130840326d488
# nested parser: https://medium.com/geekculture/nested-scrapy-spiders-explained-with-airbnbs-website-scraping-with-976b2762ef34

# SOLUTION TO ITEM CLONE: https://stackoverflow.com/questions/41778543/scrapy-why-item-inside-for-loop-has-the-same-value-while-accessed-in-another-p
# and https://stackoverflow.com/questions/57566087/scrapy-duplicate-item-fields-due-to-multiple-for-loops

# scrapy crawl sayari_x_item_method -O item_crawler3.json
import scrapy
import json
from scrapy.http import JsonRequest
from sayari_scraper.items import BusinessResults

class TestSpider(scrapy.Spider):

    name = 'sayari_x_item_method'

    def start_requests(self):
        url = "https://firststop.sos.nd.gov/api/Records/businesssearch"
        payload = {
            "SEARCH_VALUE": "X",  # Filter for names that contain the letter 'X'
            "STARTS_WITH_YN": "true",  # Begin with 'X'
            "ACTIVE_ONLY_YN": "true"  # Active only
        }

        # POST request while passing off the above payload
        yield JsonRequest(
            url=url,
            data=payload,
            callback=self.parse_initial_company_data
        )

    def parse_initial_company_data(self, response):

        data = json.loads(response.body)

        for id, value in data['rows'].items():
            results = BusinessResults()
            # Ensure the title of the business begins with X
            if value['TITLE'][0].startswith('X'):
                # Assign 'Business ID', 'Business Info' to business = scrapy.Field()
                results['business'] = [{'ID': id}, {'Business Info': value}]

                yield JsonRequest(url=f"https://firststop.sos.nd.gov/api/FilingDetail/business/{id}/false",
                                  callback=self.parse_additional_company_data,
                                  cb_kwargs={'id': id, 'results': results})

    def parse_additional_company_data(self, response, id, results):
        data = json.loads(response.body)
        additional_data_list = data['DRAWER_DETAIL_LIST']

        temp = {}
        for item in additional_data_list:
            # squish DRAWER_DETAIL_LIST (list of dicts) into a single-level dict (temp)
            temp[item['LABEL']] = item['VALUE']

        # Assign 'temp' data to additional_information = scrapy.Field()
        results['additional_information'] = {'DRAWER_DETAIL_LIST': temp}
        yield results
