from bson.code import Code
import plotly.plotly as plt
import plotly.graph_objs as go
from WordClouds import WordCloud

class Statistics:
    THRESHOLD = 1500
    AVERAGE_FRIENDS = 0
    AVERAGE_FOLLOWERS = 0

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

    '''
    ### Counts the distinct profiles in the database
    '''
    def distinctProfiles(self, database):
        results = len(database.distinct("UserID"))
        return results

    '''
    ### Calculate and present popular topics
    '''
    def getPopularTopics(self, database, collection, topicCount=10):
        collectionName = "WordCount"
        database[collectionName].drop()
        allRecords = database[collection].find({}, {'Content': 1, '_id':0})
        for tweet in allRecords:
            arr = tweet['Content'].split()
            for word in arr:
                if (database[collectionName].count({'Word': word}) > 0):
                    database[collectionName].update_one({'Word': word}, {"$inc":{"Count": 1}})
                else:
                    database[collectionName].insert_one({"Word": word, "Count": 1})

        result = list(database[collectionName].find({}, {'_id':0}).sort("Count", -1).limit(topicCount))

        base = []
        values = []
        index = 0
        for i in result:
            base.append(i['Word'])
            values.append(i['Count'])
            index += 1

        data = [
            go.Bar(
                x=base,
                y=values
            )
        ]
        plot_url = plt.plot(data, filename='Popular Topics (Words)')
        print plot_url
        return result

    '''
    ### Calculate and present popular hastags
    '''
    def getPopularHashtags(self, database, topicCount = 10):
        hashtags = list(database["WordCount"].find({"Word": {"$regex": '^#'}}, {'_id':0}).sort("Count", -1).limit(topicCount))
        base = list()
        values = list()
        for tag in hashtags:
            base.append(tag["Word"])
            values.append(tag["Count"])
        WordCloud().CreateWordcloud(base, "Hashtags.png")

        data = [
            go.Bar(
                x=base,
                y=values
            )
        ]
        plot_url = plt.plot(data, filename='Popular Hashtags')
        print plot_url
        return

    def setAverageFriendsFollowers(self, database):
        result = list(database.aggregate([{
            "$group":
                {
                    "_id": None,
                    "avgFriends": {"$avg": "$Friends"},
                    "avgFollowers": {"$avg": "$Followers"}
                }
        }]))
        self.AVERAGE_FRIENDS = result[0]["avgFriends"]
        self.AVERAGE_FOLLOWERS = result[0]["avgFollowers"]
        return

    def setDeceptionScores(self, database):
        self.setAverageFriendsFollowers(database)
        users = list(database.distinct("UserID"))

        for user in users:
            user = int(round(user))
            userTweets = list(database.find({"UserID": user}))
            score = 0
            if (userTweets[0]["Followers"] > (self.AVERAGE_FOLLOWERS + self.THRESHOLD) or userTweets[0]["Followers"] < (
                self.AVERAGE_FOLLOWERS - self.THRESHOLD)):
                score += 10
            if (userTweets[0]["Friends"] > (self.AVERAGE_FRIENDS + self.THRESHOLD) or userTweets[0]["Friends"] < (
                self.AVERAGE_FRIENDS - self.THRESHOLD)):
                score += 10
            if (userTweets[0]["Description"] == ""):
                score += 25
            if (userTweets[0]["Followers"] >= 2001 and userTweets[0]["Friends"] < 2000):
                score += 25
            if (userTweets[0]["IsDefaultProfile"] == 0):
                score += 5
            uniqueTweets = len(list(database.distinct("Content", {"UserID": user})))
            if not uniqueTweets == len(userTweets):
                score += (len(userTweets)-uniqueTweets)*2
            for tweet in userTweets:
                if tweet["Content"] == "":
                    score += 1

            database.update_one({"_id": user}, {"$set": {"DeceptionScore": score}})

        self.getDeceptions(database)
        return

    def getDeceptions(self, database, limit=10):
        result = list(database.find({}).limit(limit))
        for res in result:
            seq = (res["Username"] , "     " , str(res["StatusCount"]) , "     " , str(res["DeceptionScore"]))
            print("".join(seq))
        return
