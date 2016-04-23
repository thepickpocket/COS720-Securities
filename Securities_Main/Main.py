# COS 720 Securities
# Assignment by Jason R. Evans 13032608 & Vivian L. Venter 13238435
# Project 14

from pytagcloud import create_tag_image, make_tags, LAYOUTS
from pytagcloud.lang.counter import get_tag_counts
from pymongo import MongoClient
from DataCleanup import Cleanup

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

def CreateWordcloud():
    global DATA
    tags = make_tags(get_tag_counts(DATA))
    create_tag_image(tags, 'image.png', size=(900, 600), background=(0, 0, 0, 0), fontname='Lobster')


##Main implementation

dbClient = MongoClient()
db = dbClient['COS720']
collection = db['TwitterData']
allData = collection.find({})

cleanupContent(allData)
CreateWordcloud()


dbClient.close()

