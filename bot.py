import tweepy, json, random
from PIL import Image

class VerifiedBot():
    TWITTER_VERIFIED_ID = 63796828
    def __init__(self, keyfile = "keys.json"):
        """Connects the script to the Twitter API."""
        #get the keys found in the json file
        with open(keyfile,"r") as file: keys = json.loads(file.read())

        #initialize the api variable with the correct keys
        auth = tweepy.OAuthHandler(keys["consumerkey"], keys["consumerkeysecret"])
        auth.set_access_token(keys["accesstoken"], keys["accesstokensecret"])
        self.api = tweepy.API(auth)

    def getRandomVerified(self):
        with open("done.txt", "r") as file: done = [line.strip() for line in file.readlines()]
        followers = [follower for follower in self.api.followers(TWITTER_VERIFIED_ID) if follower not in done]
        return random.choice(followers)