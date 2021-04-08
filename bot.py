import tweepy, json, random, pickle
from PIL import Image

class VerifiedBot():
    def __init__(self, keyfile = "keys.json"):
        """Connects the script to the Twitter API."""
        #get the keys found in the json file
        with open(keyfile,"r") as file: keys = json.loads(file.read())

        #initialize the api variable with the correct keys
        auth = tweepy.OAuthHandler(keys["consumerkey"], keys["consumerkeysecret"])
        auth.set_access_token(keys["accesstoken"], keys["accesstokensecret"])
        self.api = tweepy.API(auth)

    def getRandomVerified(self):
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

bot = VerifiedBot()
bot.resetDone()
print("@"+bot.getRandomVerified().screen_name)