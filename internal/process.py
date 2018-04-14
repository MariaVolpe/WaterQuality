from pymongo import MongoClient
from pprint import pprint
import csv

client = MongoClient()

class ProcessFile:

    def __init__(self):
        self.db = client.WaterQualityDB

        #collection: bacteria
        self.bacteria = self.db.bacteria
        #collection: site keys
        self.income = self.db.income
        
        #self.bacteria.drop()
        #self.income.drop()

        # for doc in self.bacteria.find({}):
        #     pprint( doc )

        # for doc in self.income.find({}):
        #     pprint( doc )

    #in this demo, file comes precleaned and not pulled from web

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
        data_dict = self.parse_csv('./data/harbor_sampling_ytd_2017.csv')
        for i in data_dict:
            self.bacteria.insert(i)
    
    def load_sites(self):
        data = [
            { "site" : "E2", "income" : 540 },
            { "site" : "N4", "income" : 492 },
            { "site" : "N3B", "income" : 349 },
            { "site" : "NR1", "income" : 349 },
            { "site" : "H3", "income" : 321 },
            { "site" : "WC2", "income" : 369 },
            { "site" : "E13", "income" : 305 },
            { "site" : "K5", "income" : 607 },
            { "site" : "K6", "income" : 527 },
            { "site" : "GB1", "income" : 410 },
            { "site" : "N9", "income" : 389 },
            { "site" : "NC3", "income" : 443 },
            { "site" : "E4", "income" : 347 },
            { "site" : "BR5", "income" : 302 }
        ]

        for i in data:
            self.income.insert(i)

    def parse_csv(self, csv_file):
        data = []
        with open(csv_file, 'rt') as cf:
            reader = csv.DictReader(cf)
            for line in reader:
                data.append(line)
        return data