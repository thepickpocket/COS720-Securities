# COS 720 Securities
# Assignment by Jason R. Evans 13032608 & Vivian L. Venter 13238435
# Project 14

import HTMLParser
import re
from StoppingWords import StopWords
from pymongo import MongoClient

class Cleanup:
    def __init__(self):
        return None

    '''
    ### Escaping HTML Characters ###
    '''
    def HTMLCharEscaping(self, line):
        htmlParser = HTMLParser.HTMLParser()
        return htmlParser.unescape(line)

    '''
    ### Removing non-printable characters ###
    '''
    def NonPrintableChars(self, line):
        stripped = lambda s: "".join(i for i in s if 31 < ord(i) < 127)
        return stripped(line)

    '''
    ### Removing of punctuation ###
    '''
    def RemovePunctuation(self, line):
        out = "".join(c for c in line if c not in StopWords().Punctuation)
        return out

    '''
    ### Changing all letters to lowercase letters ###
    '''
    def ToLowercase(self, line):
        return unicode(line).lower()

    '''
    ### Removing of URLs ###
    '''
    def RemoveLinks(self, line):
        while line.find("http") > -1:
            foundPosition = line.find("http")
            if foundPosition > 0:
                newString = line[0:foundPosition - 1]
            else:
                newString = ""
            spacePos = line.find(" ", foundPosition)
            if spacePos == -1:
                line = newString
            else:
                line = newString + line[spacePos:]

        return line

    '''
    ### Removing of Mentioned usernames ###
    '''
    def RemoveMentions(self, line):
        listOfMentions = re.findall(r'(?<=@)\w+', line)
        for person in listOfMentions:
            line = line.replace('@' + person + ' ', '')
        return line

    '''
    ### Removing of stopping words ###
    '''
    def RemoveStopWords(self, line):
        for word in StopWords.Words:
            line = re.sub('\\b' + unicode(word) + '\\b', '', line)
            line = line.strip()
        return line

    '''
    ### Seperation of Retweets ###
    '''
    def SeperateRetweets(self, obj):
        if obj['Retweet'] == 0:
            dbClient = MongoClient()
            db = dbClient['COS720']
            collection = db['TwitterDataNoRetweets']
            collection.insert_one(obj)
            dbClient.close()
