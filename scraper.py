import requests

class Parser:

    def pre_crawl(self):
        pass

    def crawl(self):
        pass

    def map_data(self):
        pass

    def crawl(self):
        pass

class Selenium_parser(Parser):

    def crawl(self):
        for url in self.url_list:
            html = requests.post(url)
        pass

    def map_data(self):
        pass

class HTML_site(Parser):

    def crawl(self):

        for url in self.url_list:
            html = requests.post(url)
            # for json in output:
            #     line = self.map_data(json)

    def map_data(self):
        pass

class Rest_api_parser:

    def crawl(self):

        self.prepare_url_list()

        for url in self.url_list:
            output = requests.post(url)
            for json in output:
                line = self.map_data(json)
        pass

    def map_data(self):
        pass




class Site:

    def __init__(self, url, parser):

        self.name = 0
        self.url_list = [url]
        self.parser = parser  # HTML_site/Rest_api

    def prepare_url_list(self):
        self.url_list =[]
        pass




 

all_sites_objects = []


json_parser_obj = Rest_api_parser()
venue1= Site('<example url>', json_parser_obj)
all_sites_objects.append(venue1)







# main


output_list=[]
for venue in all_venues_objects:
    output_list.append(venue.parser.crawl())

# write to csv