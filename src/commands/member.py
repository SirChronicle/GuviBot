from dbmongo import db
import asyncio
from datetime import datetime
import pymongo
import discord
global times_used

dbs = db.connection()

# mydb = dbs.DiscordBot

client = discord.Client()
async def membr(message):
    index = message.content.index(' ')
    index = index + 1
    main_message = message.content[index:]
    sch = main_message.split()
    arg1 = sch[0]
    arg2 = sch[1]
    memb=[]
    if arg1 == 'count':
        member = dbs.Data.find()
        for item in member:
            item_id = item["ids"]
            if int(item_id) == int(arg2):
                memb = item["members"]
                no = len(memb)
                # if '@everyone' in memb:
                #     no-=1
                if 'r' in memb:
                    no-=1
                await message.channel.send(f"No. of members: {no}")
    # elif arg1 == 'show':
    #     member = dbs.Data.find()
    #     await message.channel.send("Members:\n")
    #     for item in member:
    #         item_id = item["ids"]
    #         if int(item_id) == int(arg2):
    #             memb = item["members"]
    #             # if '@everyone' in memb:
    #             #     memb.remove('@everyone')
    #             if 'r' in memb:
    #                 memb.remove('r')
    #             print(memb)
    #             for mem in memb:
    #                 mek = mem[3:-1]
    #                 user = await client.fetch_user(mek)
    #                 await message.channel.send(f"{user.name}\n")