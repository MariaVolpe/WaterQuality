from pymongo import MongoClient
from pprint import pprint

client = MongoClient()

class ProcessFile:
    
    def __init__:
        self.db = client.WaterQualityDB

        #collection: bacteria
        self.bacteria = self.db.bacteria
        #collection: site keys
        self.sites = self.db.sites

    #pull file from web
    def get_file():
        dummy = 0

    #clean file:
    #trim off headers
    #clean headers
    #clean unnessary data
    #result: reduced to a few columns
    def clean_file():
        dummy = 0


    #load into collection in db
    def load_bacteria(self):

        data_dict = self.parse_csv('data/harbor_sampling_ytd_2018')
        for i in data_dict:
            self.bacteria.insert(i)

        # site_dict = self.parse_csv('data/harbor_sampling_coordinates')
        # for i in site_dict:
        #     self.site.insert(i)

    def parse_csv(self, csv_file):
        data = []
        with open(csv_file, 'rt') as cf:
            reader = csv.DictReader(cf)
            for line in reader:
                data.append(line)
        return data