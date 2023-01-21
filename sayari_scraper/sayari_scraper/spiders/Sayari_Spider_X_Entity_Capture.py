from sys import path
path.append('/Users/amir/Projects/personal/sayari/sayari_scraper')
import json
import scrapy
from scrapy.http import JsonRequest
from scrapy.crawler import CrawlerProcess
from sayari_scraper.items import BusinessResults
from datetime import datetime
from scrapy.exceptions import CloseSpider


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

            # Assign 'Business ID', 'Business Info' to business = scrapy.Field()
            results['business'] = [{'ID': id}, {'Business Info': value}]

            yield JsonRequest(url=f"https://firststop.sos.nd.gov/api/FilingDetail/business/{id}/false",
                              callback=self.parse_additional_company_data,
                              cb_kwargs={'results': results})

    # Second parse (additional info)
    def parse_additional_company_data(self, response, results):
        data = json.loads(response.body)
        additional_data_list = data['DRAWER_DETAIL_LIST']


        ### testing purpose. limit to 10 items
        scrape_count = self.crawler.stats.get_value('item_scraped_count')
        print (scrape_count)
        limit = 10
        if scrape_count == limit:
            raise CloseSpider('Limit Reached')



        temp = {}
        for item in additional_data_list:
            # squish DRAWER_DETAIL_LIST (list of dicts) into a single-level dict (temp)
            temp[item['LABEL']] = item['VALUE']

        # Assign 'temp' data to additional_information = scrapy.Field()
        results['additional_information'] = {'DRAWER_DETAIL_LIST': temp}

        yield results  # when Item() results is yielded, it passes through the pipeline


if __name__ == '__main__':  # == scrapy crawl sayari_x_item_method -O crawler_results.json
    date_today = datetime.today().strftime('%Y-%m-%d')
    settings = dict()
    # invokes ConfirmBusinessStartsWithX pipeline to filter out non-X companies
    settings['ITEM_PIPELINES'] = {
        'sayari_scraper.pipelines.ConfirmBusinessStartsWithX': 1,
        'sayari_scraper.pipelines.GoogleMySqlUpload': 2}
    # saves the file as crawler_results.json within the /data folder
    settings['FEEDS'] = {
        f"data/{date_today}_crawler_results.json": {"format": "json", "overwrite": True}, }

    process = CrawlerProcess(settings=settings)
    process.crawl(SayariSpider)
    process.start()