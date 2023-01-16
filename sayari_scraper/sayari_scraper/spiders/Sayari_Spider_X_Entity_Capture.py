from sayari_scraper.items import BusinessResults
from scrapy.crawler import CrawlerProcess
from scrapy.http import JsonRequest
import scrapy
import json


class SayariSpider(scrapy.Spider):
    name = 'sayari_x_item_method'

    def start_requests(self):
        url = "https://firststop.sos.nd.gov/api/Records/businesssearch"
        payload = {
            "SEARCH_VALUE": "X",  # Filter for names that contain the letter 'X'
            "STARTS_WITH_YN": "true",  # Begin with 'X'
            "ACTIVE_ONLY_YN": "true"  # Active only
        }

        yield JsonRequest(  # POST request while passing off the above payload
            url=url,
            data=payload,
            callback=self.parse_initial_company_data
        )

    def parse_initial_company_data(self, response):  # Initial parse
        data = json.loads(response.body)

        for id, value in data['rows'].items():
            results = BusinessResults()
            # Ensure the title of the business begins with X
            if value['TITLE'][0].startswith('X'):
                # Assign 'Business ID', 'Business Info' to business = scrapy.Field()
                results['business'] = [{'ID': id}, {'Business Info': value}]

                yield JsonRequest(url=f"https://firststop.sos.nd.gov/api/FilingDetail/business/{id}/false",
                                  callback=self.parse_additional_company_data,
                                  cb_kwargs={'results': results})

    # Second parse (additional info)
    def parse_additional_company_data(self, response, results):
        data = json.loads(response.body)
        additional_data_list = data['DRAWER_DETAIL_LIST']

        temp = {}
        for item in additional_data_list:
            # squish DRAWER_DETAIL_LIST (list of dicts) into a single-level dict (temp)
            temp[item['LABEL']] = item['VALUE']

        # Assign 'temp' data to additional_information = scrapy.Field()
        results['additional_information'] = {'DRAWER_DETAIL_LIST': temp}
        yield results


if __name__ == '__main__':  # == scrapy crawl sayari_x_item_method -O crawler_results.json
    process = CrawlerProcess(settings={
        "FEEDS": {
            # save item to json, overwrite existing
            "data/crawler_results.json": {"format": "json", "overwrite": True},
        },
    })
    process.crawl(SayariSpider)
    process.start()
