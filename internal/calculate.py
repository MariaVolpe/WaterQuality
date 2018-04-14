from pymongo import MongoClient
from pprint import pprint
import plotly.plotly as py
import plotly.graph_objs as go

client = MongoClient()

class Calculations:
    
    def __init__:
        self.db = client.WaterQualityDB
        #collection: bacteria
        self.bacteria = self.db.bacteria
        #collection: sites with income
        self.income = self.db.income


    #y is income
    #x is bacteria averages
    def generate_line_graph(self):

        income_arr = []
        wet_arr = []
        dry_arr = []
        n = self.incomes.find()
        for i in n:
            income_arr.append( int(i["income"]) )
            wet_arr.append( self.site(i["site"], "W") )
            dry_arr.append( self.site(i["site"], "D") )

        wet_line = go.Scatter(
            x= wet_arr,
            y= income_arr
        )

        dry_line = go.Scatter(
        x= dry_arr,
        y= income_arr
        )
        graph_data = Data([wet_line, dry_line])

        py.plot(graph_data, filename = 'income-to-site-scatter')


    def generate_weather_bar(self):
        
        wet = self.weather_calculations("W")
        dry = self.weather_calculations("D")
    
        y_labels = ["Wet Weather", "Dry Weather"]
        x_labels = []

        data = [go.Bar(
            #x = x_labels,
            y = y_labels,
            text = y,
            textposition = 'auto',
            marker=dict(
                color='rgb(158,202,225)',
                line=dict(
                    color='rgb(8,48,107)',
                    width=1.5),
            ),
            opacity=0.6
        )]

    py.plot(data, filename='wet-dry-bar')


    #return average total with specified condition
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