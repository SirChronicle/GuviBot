import pymongo

def connection():
    print("Connecting to DataBase")
    client = pymongo.MongoClient(
        'mongodb+srv://prominato500:sonai2001@discbot.imdep.mongodb.net/myFirstDatabase?retryWrites=true&w=majority')
    mydb = client.DiscordBot
    return mydb
