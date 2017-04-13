import tweepy
import time
import json

userToCopy = input("Enter user to copy: ")
auth = tweepy.OAuthHandler("hRpT6tywILCNZ0bXAkuEfsoAB", "Ge0c1CiwGwelPZjX2B0TepoGicNlR6w0mvSwxPThe9aPiuOVAq")
auth.set_access_token("3685943952-BTfjGnef7QNdqnh9EMHtO5SInUcE2ZaROX9MMi8", "vD1q0887Cof3N8GKNQMHHW2Ad5vjFJCTsBONJZ47zNqC9")

api = tweepy.API(auth, wait_on_rate_limit=True)

def followUsersFollowers(userName):
    import json
    import time
    
    followed = json.loads(open("userIDs.txt").read())

    for page in tweepy.Cursor(api.followers_ids, screen_name=userName, count=10000).pages():
        usersFollowers.extend(page)
    print(usersFollowers)

    relationships = api.lookup_friendships(user_ids=usersFollowers)
    for user in relationships:
        if not user.is_following:
            api.create_friendship(user.id_str)
            followed.append({"userId": user.id_str, "timeFollowed": time.time())
            
            
    with open("userIDs.txt", "w") as userIdFile:
        userIdFile.write(json.dumps(followed))
    
    
def getExpiredFollowed(expireTime):
    import json
    import time
    
    expiredUsers = []
    followed = json.loads(open("userIDs.txt").read())
    for user in followed:
        if time.time() - user["timeFollowed"] >= expireTime:
            expiredUsers.append(user["userId"])
    return expiredUsers
            
def getFollowingFollowed():
    import json
    
    followingFollowed = []
    followed = json.loads(open("userIDs.txt").read())
    followedUserIds = [user["userId"] for user in followed]
    relationships = api.lookup_friendships(user_ids=followedUserIds)
    for user in relationships:
        if user.is_followed_by:
            followingFollowed.append(user.id_str)
    return followingFollowed
    
def unfollowUsers(userIdsToUnfollow):
    import json
    for userId in userIdsToUnfollow:
        api.destroy_friendship(userID)
        
    followed = json.loads(open("userIDs.txt").read())
    for user in followed:
        if user["userId"] in userIdsToUnfollow:
            del userIdsToUnfollow[user["userId"]]
    with open("userIDs.txt", "w") as userIdFile:
        userIdFile.write(json.dumps(userIdsToUnfollow))
        
    
unfollowFollowers()
