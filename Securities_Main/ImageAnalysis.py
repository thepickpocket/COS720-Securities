from PIL import Image
import urllib2
import cStringIO
import facebook

CollectionName = "ProfilePictures"
GraphAPI = facebook.GraphAPI(access_token='EAACEdEose0cBAFxC66rhsznW4tpCfSLDFhgL8Chwp32I8qsH7SteKyK9c49GuSV5sZASAtZAnixJINwXYl2OBNxsF8WCIHp0E4BBKcLuZBatgde7IZAseWjTwoObn5U90IqAIx8PebrLikP3WkqiZA36m9qtovuExEB0ssWeZCsgZDZD', version='2.2')

class ImageAnalysis:
    '''
    This function will retrieve all links to profiles that have changed their profile pics on twitter, then
    search other social media for profile pics of the same person.
    Database structure:
    _id, userId, Twitter, Facebook, etc...
    '''
    def getAccountsWithProfilePics(self, db, collection):
        cursor = list(db[collection].find(
            {"IsDefaultProfile" : 0},
            {
                "_id":0,
                "UserID":1,
                "FullName": 1,
                "ProfileImage": 1
            }
        ))

        failedCount = 0
        for doc in cursor:
            try:
                urllib2.urlopen(doc["ProfileImage"])
                db[CollectionName].insert_one(doc)
            except urllib2.HTTPError:
                failedCount += 1

        print("Failed to insert %i documents as profile images no longer exists" %failedCount)
        return

    def analyze(self):
        post = GraphAPI.request('/search?q=Jason.Evans&type=user')
        print(post)
        try:
            #file = cStringIO.StringIO(
            urllib2.urlopen("http://pbs.twimg.com/profile_images/695830357178916864/vjTjcBUG.png")
            #img = Image.open(file)
            #img.show()
        except urllib2.HTTPError:
            print("Sorry dumbass!!")
        return

ImageAnalysis().analyze()