from PIL import Image
import urllib2
import cStringIO

CollectionName = "ProfilePictures"

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
                "ProfileImage":1
            }
        ))

        db[CollectionName].insert_many(cursor)
        return

    def analyze(self):
        file = cStringIO.StringIO(urllib2.urlopen("http://marek.online/wp-content/uploads/2015/09/helloworld1.gif").read())
        img = Image.open(file)
        img.show()
        return

ImageAnalysis().analyze()