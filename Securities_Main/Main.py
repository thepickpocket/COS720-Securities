# COS 720 Securities
# Assignment by Jason R. Evans 13032608 & Vivian L. Venter 13238435

import sys
import HTMLParser
from pymongo import MongoClient

##Helper Functions
def cleanupContent(data):
    count = 0
    htmlParser = HTMLParser.HTMLParser()

    for tweet in allData:
        content = tweet['Content']
        escapedContent = htmlParser.unescape(content)
        print escapedContent

        stripped = lambda s: "".join(i for i in s if 31 < ord(i) < 127)
        escapedContent = stripped(escapedContent)

        while escapedContent.find("http") > -1:
            foundPosition = escapedContent.find("http")
            if foundPosition > 0:
                newString = escapedContent[0:foundPosition-1]
            else:
                newString = ""
            spacePos = escapedContent.find(" ", foundPosition)
            if spacePos == -1:
                escapedContent = newString
            else:
                escapedContent = newString + escapedContent[spacePos:]
        print(escapedContent)

        count = count + 1
        if count == 100:
            break

##Main implementation

dbClient = MongoClient()
db = dbClient['COS720']
collection = db['TwitterData']
allData = collection.find({})

cleanupContent(allData)


dbClient.close()

