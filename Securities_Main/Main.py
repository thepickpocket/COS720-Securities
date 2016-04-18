# COS 720 Securities
# Assignment by Jason R. Evans 13032608 & Vivian L. Venter 13238435

import sys
import re
from pytagcloud import create_tag_image, make_tags
from pytagcloud.lang.counter import get_tag_counts
from pymongo import MongoClient
from DataCleanup import Cleanup

DATA = unicode("")

##Helper Functions
def cleanupContent(data):
    count = 0

    for tweet in data:
        content = tweet['Content']
        print("Before Cleanup: " + content)
        text = Cleanup().HTMLCharEscaping(content)
        text = Cleanup().NonPrintableChars(text)
        text = Cleanup().ToLowercase(text)
        text = Cleanup().RemoveLinks(text)
        text = Cleanup().RemoveMentions(text)
        text = Cleanup().RemoveStopWords(text)
        print("After Cleanup: " + text)

        global DATA
        DATA = DATA + unicode(text)

        count = count + 1
        if count == 10:
            break

def CreateWordcloud():
    global DATA
    tags = make_tags(get_tag_counts(DATA))
    create_tag_image(tags, 'tester-image.png', size=(900, 600), fontname='Lobster')


##Main implementation

dbClient = MongoClient()
db = dbClient['COS720']
collection = db['TwitterData']
allData = collection.find({})

cleanupContent(allData)
CreateWordcloud()


dbClient.close()

