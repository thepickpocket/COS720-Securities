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
        text = Cleanup().HTMLCharEscaping(content)
        text = Cleanup().NonPrintableChars(text)
        text = Cleanup().ToLowercase(text)
        text = Cleanup().RemoveLinks(text)
        text = Cleanup().RemoveMentions(text)
        text = Cleanup().RemoveStopWords(text)
        text = Cleanup().RemovePunctuation(text)

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

while True:
    print("COS 720 Securities Practical: \n")
    print("1. Create Content WordCloud")
    print("2. Create Location WordCloud")
    print("3. Create Location Bar Graph")
    print("4. Generate Location Sharing Statistics")
    print("5. Generate number of distinct twitter profiles")
    print("Type X to exit.")
    input = Cleanup().ToLowercase(raw_input("Please choose an operation:"))

    if input == 'x':
        break
    elif input == '1':
        print("Creating word cloud from twitter content data...")
        WordCloud().CreateWordcloud(DATA, '../images/image.png')
        print("Word cloud created.")
    elif input == '2':
        print("Creating word cloud on locations..")
        WordCloud().CreateWordcloud(getLocations(allData), '../images/locations.png')
        print("Word cloud created.")
    elif input == '3':
        print("Generating statistics on language of twitter posts...")
        Statistics().languageStats(db)
        print("Complete.")
    elif input == '4':
        print("Generating statistics on location sharing of twitter posts...")
        Statistics().shareLocation(db)
        print("Complete.")
    elif input == '5':
        print("Generating the number of distinct twitter profiles...")
        Statistics().distinctProfiles(db)
        print("Complete.")

dbClient.close()

