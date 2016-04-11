from pymongo import MongoClient

class TIKMongoDriver:
    dbClient = MongoClient() #automatically connects to local instance on port 27017
    def __init__(self):
        return None;