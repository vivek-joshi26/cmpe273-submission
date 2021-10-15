users = {}

id = 99

def createUser(request):
   global  id
   id += 1
   print(users)
   print(request)
   users[id] = {
      "name" : request["name"],
      "email"   : request["email"],
   }
   users[id]["tweets"] = []
   users[id]["followers"] = []
   users[id]["tweets_counter"] = 0
   print(users)
   response = {
      "id": id,
      "name" : request["name"],
      "email": request["email"],
      "tweets": users[id]["tweets"],
      "followers" : users[id]["followers"],
   }
   return response


def addFollower(user_id, follower_id):


   followers = users[int(user_id)]["followers"]
   followers.append(follower_id)

   response = {
      "id": id,
      "name" : users[int(user_id)]["name"],
      "email": users[int(user_id)]["email"],
      "tweets": users[int(user_id)]["tweets"],
      "followers" : users[int(user_id)]["followers"],
   }

   return response


def addTweet(user_id, request):
   tweetCounter = users[int(user_id)]["tweets_counter"]
   tweetCounter += 1
   users[int(user_id)]["tweets_counter"] = tweetCounter

   tweets =  users[int(user_id)]["tweets"]
   tweets.append({"tweet_id": tweetCounter, "tweet": request["tweet"]})

   response = {
      "tweet_id": tweetCounter,
      "tweet": request["tweet"]
   }
   return response


def getUser(user_id):

   response = {
      "id": user_id,
      "name" : users[int(user_id)]["name"],
      "email": users[int(user_id)]["email"],
      "tweets": users[int(user_id)]["tweets"],
      "followers" : users[int(user_id)]["followers"],
   }
   return response



def getTweets(user_id):
   tweets =  users[int(user_id)]["tweets"]
   timeline = []
   for tweet in tweets:
      obj = {
         "user_id" : user_id,
         "tweet_id" : tweet["tweet_id"],
         "tweet" : tweet["tweet"]
      }
      timeline.append(obj)
   response = {
      "timeline": timeline
   }
   return response
