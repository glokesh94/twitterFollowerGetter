import tweepy


auth = tweepy.OAuthHandler("hRpT6tywILCNZ0bXAkuEfsoAB", "Ge0c1CiwGwelPZjX2B0TepoGicNlR6w0mvSwxPThe9aPiuOVAq")
auth.set_access_token("3685943952-BTfjGnef7QNdqnh9EMHtO5SInUcE2ZaROX9MMi8", "vD1q0887Cof3N8GKNQMHHW2Ad5vjFJCTsBONJZ47zNqC9")
api = tweepy.API(auth, wait_on_rate_limit=True)


expireTime = 60*60*24*7

def chunks(listToCut, maxLength):
    for i in range(0, len(listToCut), maxLength):
        yield listToCut[i:i+maxLength]

def getUserToCopy():
    userToCopy = open("userToCopy.txt").read().strip()
    if userToCopy:
        with open("userToCopy.txt", "w") as userToCopyFile:
            userToCopyFile.write("")
        return [True, userToCopy]
    return [False, ""]
    
    
def followUsersFollowers(userName):
    import json
    import time
    
    followed = json.loads(open("userIDs.txt").read())
    usersFollowers = []
    relationships = []
    
    for page in tweepy.Cursor(api.followers_ids, screen_name=userName, count=100).pages():
        relationships.extend(api.lookup_friendships(user_ids=page))
    try:
        for user in relationships:
            if not user.is_following and not user.is_following:
                api.create_friendship(user.id_str)
                followed.append({"userId": user.id_str, "timeFollowed": time.time()})
    except:
        with open("userIDs.txt", "w") as userIdFile:
            userIdFile.write(json.dumps(followed))
    else:
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
    
    relationships = []
    followingFollowed = []
    followed = json.loads(open("userIDs.txt").read())
    followedUserIds = [user["userId"] for user in followed]
    splitFollowedUserIds = chunks(followedUserIds, 100)
    for chunk in splitFollowedUserIds:
        relationships.extend(api.lookup_friendships(user_ids=chunk))
        
    for user in relationships:
        if user.is_followed_by:
            followingFollowed.append(user.id_str)
    return followingFollowed
    
    
def unfollowUsers(userIdsToUnfollow):
    import json
    for userId in userIdsToUnfollow:
        api.destroy_friendship(userId)
        
    followed = json.loads(open("userIDs.txt").read())
    for user in followed:
        if user["userId"] in userIdsToUnfollow:
            del userIdsToUnfollow[userIdsToUnfollow.index(user["userId"])]
    with open("userIDs.txt", "w") as userIdFile:
        userIdFile.write(json.dumps(userIdsToUnfollow))
        
    
copy, userToCopy = getUserToCopy()
if copy:
    followUsersFollowers(userToCopy)
    print("googd")
expiredFollowers = getExpiredFollowed(expireTime)
followingFollowed = getFollowingFollowed()
usersToUnfollow = []
usersToUnfollow.extend(expiredFollowers)
usersToUnfollow.extend(followingFollowed)
unfollowUsers(usersToUnfollow)
