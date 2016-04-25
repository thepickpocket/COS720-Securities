import collections
from DataCleanup import Cleanup
from pymongo import MongoClient
from bson.code import Code
import plotly.plotly as plt
import plotly.graph_objs as go

class Statistics:
    def languageStats(self, database):
        reducer = Code("""function(obj, prev){
                        prev.count++;
                    }""")
        results = database.TwitterData.group(key={"Language":""}, condition="", initial={"count": 0}, reduce=reducer)
        base = list()
        values = list()
        for doc in results:
            base.append(doc['Language'])
            values.append(doc['count'])

        data = [
            go.Bar(
                x = base,
                y = values
            )
        ]
        plot_url = plt.plot(data, filename='LanguageStats')

        print plot_url