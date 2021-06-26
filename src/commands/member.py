from dbmongo import db
import discord
global times_used

dbs = db.connection()



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
                if 'r' in memb:
                    no-=1
                await message.channel.send(f"No. of members: {no}")