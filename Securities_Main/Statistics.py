from bson.code import Code
import plotly.plotly as plt
import plotly.graph_objs as go

class Statistics:
    def languageStats(self, database):
        reducer = Code("""function(obj, prev){
                        prev.count++;
                    }""")
        results = database.group(key={"Language":""}, condition="", initial={"count": 0}, reduce=reducer)
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

        base.pop(0)
        values.pop(0)

        data = [
            go.Bar(
                x=base,
                y=values
            )
        ]
        plot_url = plt.plot(data, filename='LanguageStatsWithoutEnglish')

        print plot_url

    def shareLocation(self, database):
        allRecords = database.count()
        sharesLocation = database.count(filter={"Geo_Enabled": 1})
        doesNotShareLocation = database.count(filter={"Geo_Enabled": 0})

        figure = {
            'data' : [{
                'labels': ['Location Sharing Enabled', 'Location Sharing Disabled', 'Other'],
                'values': [(sharesLocation/float(allRecords))*100, (doesNotShareLocation/float(allRecords))*100, allRecords - (sharesLocation + doesNotShareLocation)],
                'type': 'pie'
            }],
            'layout': {'title': 'Percentage of Users Sharing/Hiding Location When Tweeting'}
        }

        print(plt.plot(figure, filename='LocationSharingEnabled'))

    def distinctProfiles(self, database):
        results = len(database.distinct("UserID"))
        return results
