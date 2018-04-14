from pymongo import MongoClient
from pprint import pprint

client = MongoClient()

class Calculations:
    
    def __init__:
        self.db = client.WaterQualityDB
        #collection: bacteria
        self.bacteria = self.db.bacteria
        #collection: sites with income
        self.income = self.db.income

    #return average of day with specified condition
    def weather_calculations(self, condition):
        data = []
        n = self.bacteria.find( {"Weather":condition} )
        for i in n:
            if i["Enterococcus"] != "NS":
                data.append( int(i["Enterococcus"]) )

        return self.average(data)

    #condition: "W" (Wet) or "D" (Dry)
    def site(self, site, condition):
        data = []
        n = self.bacteria.find( "$AND" : [{"Site": site}, {"Weather":condition}]})
        for i in n:
            if i["Enterococcus"] != "NS":
                data.append( int(i["Enterococcus"] ))

        return self.average(data)

    #data = int[]
    def average(self, data):
        x = 0
        for i in data:
            x += i

        return ( x/len(data) )