from pymongo import MongoClient

class MongoDriver:
    db = None
    dbClient = None

    def __init__(self):
        MongoDriver.dbClient = MongoClient()  # automatically connects to local instance on port 27017
        MongoDriver.db = MongoDriver.dbClient.TwitterIdentiKit # Switch to the database named TwitterIdentiKit
        return None;

    def saveData(jsonField): # Will store the data in the database
        result = MongoDriver.db.TwitterData.insert_one(jsonField)
        return None

    def __del__(self):
        MongoDriver.dbClient.close()
