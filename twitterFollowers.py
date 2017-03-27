import tweepy
import time
import json

userToCopy = "KidKrypt0"
auth = tweepy.OAuthHandler("hRpT6tywILCNZ0bXAkuEfsoAB", "Ge0c1CiwGwelPZjX2B0TepoGicNlR6w0mvSwxPThe9aPiuOVAq")
auth.set_access_token("3685943952-BTfjGnef7QNdqnh9EMHtO5SInUcE2ZaROX9MMi8", "vD1q0887Cof3N8GKNQMHHW2Ad5vjFJCTsBONJZ47zNqC9")

api = tweepy.API(auth, wait_on_rate_limit=True)

def followUsersFollowers(userName):
    userIDs = []
    newFollowing = []
    for page in tweepy.Cursor(api.followers_ids, screen_name=userName, count=10000).pages():
        userIDs.extend(page)

    for userID in userIDs:
        if not api.exists_friendship(userID, 3685943952):
            api.create_friendship(userID)
            newFollowing.append(userID)
            
    with open("userIDs.txt", "w+") as userIDsFile:
        currentIDs = userIDsFile.read().strip()
        userIDsFile.write(currentIDs + " ".join(newFollowing))
    
def unfollowFollowers():
    with open("userIDs.txt", "r") as userIDsFile:
        userIDs = userIDsFile.read().strip().split(" ")
        
    for userID in userIDs:
        if api.exists_friendship(userID, 3685943952):
            api.destroy_friendship(userID)
            
if not userToCopy == "":            
    followUsersFollowers(userToCopy)
    
unfollowFollowers()

