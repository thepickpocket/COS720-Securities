# COS 720 Securities
# Assignment by Jason R. Evans 13032608 & Vivian L. Venter 13238435
# Project 14

from pymongo import MongoClient
from DataCleanup import Cleanup
from WordClouds import WordCloud
from Statistics import Statistics

DATA = unicode("")

##Helper Functions
def cleanupContent(data):
    count = 0

    for tweet in data:
        content = tweet['Content']
        print(str(count) + " Before Cleanup: " + content)
        text = Cleanup().HTMLCharEscaping(content)
        text = Cleanup().NonPrintableChars(text)
        text = Cleanup().ToLowercase(text)
        text = Cleanup().RemoveLinks(text)
        text = Cleanup().RemoveMentions(text)
        text = Cleanup().RemoveStopWords(text)
        print(str(count) + " After Cleanup: " + text)

        global DATA
        DATA = DATA + unicode(text)

        count = count + 1
        if count == 50:
            break

def getLocations(data):
    locations = unicode("")
    count = 0
    for tweet in data:
        location = Cleanup().ToLowercase(tweet['Location'])
        if (location != unicode("")):
            locations += unicode(" ") + unicode(location) + unicode(" ")
        count += 1
        if (count == 100):
            break
    return locations

##Main implementation

dbClient = MongoClient()
db = dbClient['COS720']
collection = db['TwitterData']
allData = collection.find({})

cleanupContent(allData)
WordCloud.CreateWordcloud(DATA, 'image.png')
WordCloud().CreateWordcloud(getLocations(allData), 'locations.png')
Statistics().languageStats(db)

dbClient.close()

