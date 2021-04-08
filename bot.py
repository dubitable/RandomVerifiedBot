import tweepy, json, random, pickle, os, requests, io
from PIL import Image

class VerifiedBot():
    def __init__(self, keyfile = "keyfile.json"):
        """Connects the script to the Twitter API."""
        #get the keys found in the json file
        with open(keyfile,"r") as file: keys = json.loads(file.read())

        #initialize the api variable with the correct keys
        auth = tweepy.OAuthHandler(keys["consumerkey"], keys["consumerkeysecret"])
        auth.set_access_token(keys["accesstoken"], keys["accesstokensecret"])
        self.api = tweepy.API(auth)

    def getRandomVerified(self):
        """
        Returns a random verified account.
        """
        with open("done.txt", "rb") as file: 
            try: done = pickle.load(file)
            except Exception: done = []
        if done is None: done = []
        followers = [follower for follower in self.api.friends_ids(63796828)]
        choice = random.choice(followers)
        with open("done.txt", "wb") as file: pickle.dump(done.append(choice), file)
        return self.api.get_user(choice)
    
    def resetDone(self):
        with open("done.txt", "rb"): pass
    
    def deleteImages(self):
        """
        Deletes all files in the images directory.
        """
        for elem in os.listdir("images"):
            os.remove(os.path.join("images",elem))

    def uploadImage(self, url):
        """"
        Returns a media object given an image url.
        """
        #delete all local images
        self.deleteImages()
        #get the url, save it locally, and upload it
        response = requests.get(url)
        image = Image.open(io.BytesIO(response.content))
        image.save(os.path.join("images","image")+os.path.splitext(url)[-1])
        #return a media object for twitter upload
        media = self.api.media_upload(os.path.join("images",os.listdir("images")[0]))
        return media

    def postInfo(self, user):
        """
        Posts the formatted information given a user object.
        """
        mediaID = self.uploadImage(user.profile_image_url).media_id_string
        self.api.update_status(".@{} {}\n".format(user.screen_name, user.description), media_ids = [mediaID])

if __name__ == "__main__":
    bot = VerifiedBot()
    bot.resetDone()
    bot.postInfo(bot.getRandomVerified())