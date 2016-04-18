# COS 720 Securities
# Assignment by Jason R. Evans 13032608 & Vivian L. Venter 13238435

import sys
import re
import HTMLParser
from pymongo import MongoClient

##Helper Functions
def cleanupContent(data):
    count = 0
    htmlParser = HTMLParser.HTMLParser()

    for tweet in allData:
        '''
        ### Escaping HTML Characters ###
        '''
        content = tweet['Content']
        escapedContent = htmlParser.unescape(content)

        '''
        ### Removing non-printable characters ###
        '''
        stripped = lambda s: "".join(i for i in s if 31 < ord(i) < 127)
        escapedContent = stripped(escapedContent)

        '''
        ### Changing all letters to lowercase letters ###
        '''
        escapedContent = escapedContent.lower()

        '''
        ### Removing of URLs ###
        '''
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

        '''
        ### Removing of Mentioned usernames ###
        '''
        listOfMentions = re.findall(r'(?<=@)\w+', escapedContent)
        for person in listOfMentions:
            escapedContent = escapedContent.replace('@'+person+' ', '');

        '''
        ### Removing of stopping words ###
        '''
        stoppingWords = ["a", "an", "is", "are", "i", "she", "he", "this", "they", "their", "that", "the", "there", "any", "to", "too"]
        for stopWord in stoppingWords:
            escapedContent = re.sub('\\b'+stopWord+'\\b', '', escapedContent)
            escapedContent = escapedContent.strip()

        print(escapedContent)

        count = count + 1
        if count == 10:
            break

##Main implementation

dbClient = MongoClient()
db = dbClient['COS720']
collection = db['TwitterData']
allData = collection.find({})

cleanupContent(allData)


dbClient.close()

