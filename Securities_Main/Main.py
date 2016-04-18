# COS 720 Securities
# Assignment by Jason R. Evans 13032608 & Vivian L. Venter 13238435

import sys
import re
import HTMLParser
from pytagcloud import create_tag_image, make_tags
from pytagcloud.lang.counter import get_tag_counts
from pymongo import MongoClient

DATA = unicode("")

##Helper Functions
def cleanupContent(data):
    count = 0
    htmlParser = HTMLParser.HTMLParser()

    for tweet in data:
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
        global DATA
        DATA = DATA + unicode(escapedContent)

        count = count + 1
        if count == 10:
            break

def CreateWordcloud():
    global DATA
    tags = make_tags(DATA)
    create_tag_image(tags, 'tester-image.png', size=(900, 600), fontname='Lobster')

##Main implementation

dbClient = MongoClient()
db = dbClient['COS720']
collection = db['TwitterData']
allData = collection.find({})

cleanupContent(allData)
CreateWordcloud()


dbClient.close()

