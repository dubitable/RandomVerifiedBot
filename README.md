# RandomVerifiedBot
# Random WikiBot
Every day, this bot publishes a random verified twitter account to the [@randomcheckmark](https://twitter.com/randomcheckmark) account on Twitter. It's also immortal.
## How Does It Work?
This program was originally a challenge given by my friend that I did during a particularly boring French class. 
## How To Make Your Own WikiBot
#### Apply for a Twitter Developer Account
Although bots are usually not encouraged on most social medias, Twitter actually provides an API that allows an impressive range of actions, most notably tweeting for this use case. The first thing you need to do is create a Twitter account, and then apply for an associated developer account at https://developer.twitter.com/en/apply-for-access. Once you have access to this account, you can create a standalone app or a project (I chose a standalone app as I only needed the tweet feature). This will generate different keys (you can always generate new ones if you forget to copy and paste). You will need the "Consumer Key", "Consumer Key Secret", "AccessToken", and "Access Token Secret".
#### Configuration
You may have noticed that there is a half-empty json file in the repository called "template.json". This is where you will fill in each key received in the last step (between the quotation marks). Do not forget to rename it to "keyfile.json" in order for the program to open the correct file (or modify the path in the constructor of the wikibot class in wikibot.py). You will also need to install the following modules: "tweepy" and "Pillow" (use this [link](https://docs.python.org/3/installing/index.html) if you do not know how to). The program should be fully functional now.
#### Running in the cloud
This program is actually the second version of my WikiBot: I made the original when I was less experienced and when I used a janky Instagram bot library. Even if it was far from perfect, it worked. However, I soon came accross a sizeable problem: I had to run it locally and continuously, using "time.sleep()" to create periodic posting. This was inconvenient on an immense amount of levels, so I came up with a solution for this version: hosting the bot in the cloud using PythonAnywhere. They have a system called "Tasks" which can run a program daily for free users. After you have created an account, upload the project directory (containing "links.txt", "images" folder, "wikibot.py", and "keys.json") to the site. Open a console and create a [virtualenv](https://help.pythonanywhere.com/pages/Virtualenvs/) where you can install all the modules. Finally, you can add a task using this virtual environment by using this template:
```
/home/myusername/.virtualenvs/myvenv/bin/python /home/myusername/myproject/mytask.py
```
The bot will now tweet daily without you needing to intervene.
## Functionality
```
VerifiedBot(self, keyfile="keyfile.json")
```

The VerifiedBot Class allows for the extraction and tweeting of verified users and their profile images. The script does not need to run continuously, as already done users are stored in "done.txt". The constructor will connect the bot to the Twitter API and initialize the `VerifiedBot.api` variable.   

Parameters:
- `keyfile`: a path (`string`) to a local json file containing the twitter API keys (optional argument set at `"keyfile.json"` by default).  

```
VerifiedBot.getRandomVerified(self)
```

Returns a random verified account.

```
VerifiedBot.postInfo(self, user)
```

Posts the formatted information given a user object.

Parameters:
- `user`: a tweepy user object

```
VerifiedBot.uploadImage(self, url)
```
Returns a media object given an image url.

Parameters:
- `url`: a url (`string`) to an image to upload to the Twitter API

```
VerifiedBot.deleteImages(self)
```

Deletes all files in the images directory.

```
VerifiedBot.resetDone(self)
```

Reset the already done users file.
