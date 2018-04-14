from pymongo import MongoClient
from pprint import pprint
import plotly.plotly as py
import plotly.graph_objs as go

client = MongoClient()

class Calculations:
    
    def __init__(self):
        self.db = client.WaterQualityDB
        #collection: bacteria
        self.bacteria = self.db.bacteria
        #collection: sites with income
        self.income = self.db.income

        self.generate_line_graph()
        #self.generate_weather_bar()

    #x is income
    #y is bacteria averages
    def generate_line_graph(self):

        income_arr = []
        wet_arr = []
        dry_arr = []
        n = self.income.find()
        for i in n:
            income_arr.append( int(i["income"]) )
            wet_arr.append( self.site(i["site"], "W") )
            dry_arr.append( self.site(i["site"], "D") )

        wet_line = go.Scatter(
            y= wet_arr,
            x= income_arr,
            name = 'Wet Day'
        )

        dry_line = go.Scatter(
            y= dry_arr,
            x= income_arr,
            name = 'Dry Day'
        )

        graph_data = [wet_line, dry_line]

        py.plot(graph_data, filename = 'income-to-site-line')


    def generate_weather_bar(self):
        
        wet = self.weather_calculations("W")
        dry = self.weather_calculations("D")

        data = [go.Bar(
                y = [wet, dry],
                x = ["Wet Weather", "Dry Weather"]
        )]

        py.plot(data, filename='wet-dry-bar')


    #return average total with specified condition
    def weather_calculations(self, condition):
        data = []
        n = self.bacteria.find( {"Weather":condition} )
        for i in n:
            if i["Enterococcus"] != "NS":
                data.append( float(i["Enterococcus"]) )

        return self.average(data)

    #condition: "W" (Wet) or "D" (Dry)
    def site(self, site, condition):
        data = []
        n = self.bacteria.find( {"$and" : [{"Site": site}, {"Weather":condition}]})
        for i in n:
            if i["Enterococcus"] != "NS":
                data.append( float(i["Enterococcus"] ))

        return self.average(data)

    #data = int[]
    def average(self, data):
        x = 0
        for i in data:
            x += i

        return ( x/len(data) )