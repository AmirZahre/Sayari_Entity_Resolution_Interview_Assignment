import scrapy
import json
from scrapy.http import JsonRequest


class TestSpider(scrapy.Spider):

    name = 'sayari_x_dict_method'

    def __init__(self):
        super().__init__()
        self.results = {}

    def start_requests(self):
        url = "https://firststop.sos.nd.gov/api/Records/businesssearch"
        payload = {
            "SEARCH_VALUE": "X",  # Filter for names that contain the letter 'X'
            "STARTS_WITH_YN": "true",  # Begin with 'X'
            "ACTIVE_ONLY_YN": "true"  # Active only
        }
        yield JsonRequest(
            url=url,
            data=payload,
            callback=self.parse_initial_company_data
        )

        # equivalent to:
        # yield Request(
        #     url=url,
        #     body=json.dumps(payload),
        #     method = 'POST', # default GET
        #     callback = self.parse_initial_company_data,
        #     headers={
        #         'Accept': 'application/json, text/javascript, */*; q=0.01',
        #         'Content-Type':'application/json'
        #         })

    """
    Initial run through to retreive company names
    TODO: For unknown reasons, some companies retrieved do not begin with the letter X, 
    look into cleaning the output data once I move onto the second stage of the assignment.
    """

    def parse_initial_company_data(self, response):
        data = json.loads(response.body)

        for id, value in data['rows'].items():
            # Ensure the title of the business begins with X
            if value['TITLE'][0].startswith('X'):
                self.results[id] = {'Business Name': value}

                yield JsonRequest(url=f"https://firststop.sos.nd.gov/api/FilingDetail/business/{id}/false",
                                  callback=self.parse_additional_company_data,
                                  # method="GET", # default is get
                                  cb_kwargs={'id': id})

    """
    To retreive data pertaining to a company's Commercial Registered Agent, Registered Agent, and/or Owners,
    We need to dive further into each retreived item.
    Looking into the network request once a company is clicked results in the following:

    ```
    Request URL: https://firststop.sos.nd.gov/api/FilingDetail/business/319429/false
    Request Method: GET
    ```
    """

    def parse_additional_company_data(self, response, id):
        data = json.loads(response.body)
        additional_data_list = data['DRAWER_DETAIL_LIST']

        for item in additional_data_list:
            self.results[id][item['LABEL']] = item['VALUE']

        # create a filename with the respective pages' number
        filename = 'final_result2.json'
        with open(filename, 'w') as f:
            # writes the entire html from the page
            json.dump(self.results, f, indent=4)
