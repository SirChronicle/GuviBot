import pymongo

def connection():
    client = pymongo.MongoClient(
        'mongodb+srv://GuviBot:guvibot123@storageofguvibot.s5xv9.mongodb.net/myFirstDatabase?retryWrites=true&w=majority')
    mydb = client.DiscordBot
    return mydb
