# COS 720 Securities
# Assignment by Jason R. Evans 13032608 & Vivian L. Venter 13238435
# Project 14

from pymongo import MongoClient
from DataCleanup import Cleanup
from WordClouds import WordCloud
from Statistics import Statistics

##Helper Functions
def cleanupContent(db):
    data = db.find({})
    for tweet in data:
        content = tweet['Content']
        text = Cleanup().HTMLCharEscaping(unicode(content))
        text = Cleanup().NonPrintableChars(text)
        text = Cleanup().ToLowercase(text)
        text = Cleanup().RemoveLinks(text)
        text = Cleanup().RemovePunctuation(text)
        text = Cleanup().RemoveMentions(text)
        text = Cleanup().RemoveStopWords(text)

        content = tweet['Description']
        desc = Cleanup().HTMLCharEscaping(unicode(content))
        desc = Cleanup().NonPrintableChars(desc)
        desc = Cleanup().ToLowercase(desc)
        desc = Cleanup().RemoveLinks(desc)
        desc = Cleanup().RemovePunctuation(desc)
        desc = Cleanup().RemoveMentions(desc)
        desc = Cleanup().RemoveStopWords(desc)

        db.update_one(
            {'ID': tweet['ID']},
            {
                '$set':{
                    'Content': text,
                    'Description': desc
                }
            }
        )

def getLocations(data):
    locations = unicode("")
    count = 0
    for tweet in data:
        location = Cleanup().ToLowercase(tweet['Location'])
        location = Cleanup().NonPrintableChars(location)
        if (location != unicode("")):
            locations += unicode(" ") + unicode(location) + unicode(" ")
        count += 1
        if (count == 1000):
            break
    return locations

##Main implementation
dbClient = MongoClient()
dbName = raw_input("Please enter the name of the database to use: ")
db = dbClient[dbName]
collectionName = raw_input("Please enter the name of the collection to use: ")
collection = db[collectionName]

while True:
    print("==========================================================")
    print("COS 720 Securities Practical:")
    print("==========================================================\n")
    print("1. Clean data in database")
    print("2. Clean Retweets in database")
    print("3. Score and remove bots")
    print("4. Create Content WordCloud")
    print("5. Create Location WordCloud")
    print("6. Create Location Bar Graph")
    print("7. Generate Location Sharing Statistics")
    print("8. Generate number of distinct twitter profiles")
    print("Type X to exit.")
    input = Cleanup().ToLowercase(raw_input("Please choose an operation: "))

    if input == 'x':
        break
    elif input == '1':
        cleanupContent(collection)
    elif input == '2':
        print("Seperating non retweets into collection TwitterDataNoRetweets...")
        Cleanup().SeperateRetweets(db, collectionName)
        print("Complete.")
    elif input == '3':
        print("Tagging and removing bots...")
        Cleanup().tagAndRemoveBots(collection, 0.3)
        print("Complete.")
    elif input == '4':
        print("Creating word cloud from twitter content data...")
        WordCloud().CreateWordcloud(collection.find({}), '../images/image.png')
        print("Word cloud created.")
    elif input == '5':
        print("Creating word cloud on locations..")
        WordCloud().CreateWordcloud(getLocations(collection.find({})), '../images/locations.png')
        print("Word cloud created.")
    elif input == '6':
        print("Generating statistics on language of twitter posts...")
        Statistics().languageStats(collection)
        print("Complete.")
    elif input == '7':
        print("Generating statistics on location sharing of twitter posts...")
        Statistics().shareLocation(collection)
        print("Complete.")
    elif input == '8':
        print("Generating the number of distinct twitter profiles...")
        print("Number of Distinct profiles: " + str(Statistics().distinctProfiles(collection)))
        print("Complete.")

dbClient.close()

