import tweepy
amountToRemove = 50
username = "alexpimania"

def initTwitterApi():
    twitterKeys = open("twitterKeys.txt").read().strip().split() 
    auth = tweepy.OAuthHandler(twitterKeys[0], twitterKeys[1])
    auth.set_access_token(twitterKeys[2], twitterKeys[3])
    api = tweepy.API(auth, wait_on_rate_limit=True)
    return api
api = initTwitterApi()

i = 0
for page in tweepy.Cursor(api.friends, screen_name=username, count=100).pages():
    for user in page:
        i+=1
        if i <= amountToRemove:
            api.destroy_friendship(user.id)
