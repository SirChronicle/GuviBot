from dbmongo import db
from datetime import datetime
import discord
global times_used

dbs = db.connection()

async def scheduleMeet(message, Client):
    index = message.content.index(' ')
    index = index + 1
    main_message = message.content[index:]
    sch = main_message.split('  ')
    arg1 = sch[0]
    arg2 = sch[1]
    arg3 = sch[2]
    format = '%Y-%m-%d %H:%M:%S'
    format2 = '%d %b %Y(%a) %I:%M %p'
    sch_time = datetime.strptime(arg3, format)
    sch_stamp = datetime.timestamp(sch_time)
    countmeet = dbs.Count_Meet.find()
    for item in countmeet:
        counter = item["count"]
        dbs.Data.insert_one({"ids": str(counter), "Topic": str(arg1), "DateTime": sch_time, "Description": str(arg2), "TimeStamp": sch_stamp, "Reminder": 2})
        print("Scheduled successfully!")
        await message.channel.send(f"Scheduled successfully! ID: {counter}")
        dbs.Count_Meet.update_one({"ids": "4"}, {"$inc": {"count": 1}})
        time2=sch_time.strftime(format2)
        title = f'''
🖥️🖥️🖥️🖥️🖥️
Meeting Scheduled
        '''
        embed = discord.Embed(
            title=title,
            colour=discord.Colour.blue()
        )
        name = message.author
        embed.set_author(name=str(name)[:-5])
        embed.add_field(name='Topic', value=str(arg1))
        embed.add_field(name='Time', value=time2)
        embed.add_field(name='Description', value=str(arg2), inline=False)
        embed.set_footer(text="Please attend the meeting")
        emoji1 = '✅'
        emoji2 = '❎'
        mentions = sch[-1]
        men = mentions.split()
        for user in men:
            if str(user) == '@here':
                msg = await message.channel.send(embed=embed)
                await msg.add_reaction(emoji1)
                await msg.add_reaction(emoji2)
        for user in message.mentions:
            msgs = await user.send(embed=embed)
            await msgs.add_reaction(emoji1)
            await msgs.add_reaction(emoji2)
        ment = list()
        for user in men:
            ment.append(user[3:-1])
        msgid = message.channel.id
        dbs.Data.update_one({"ids": str(counter)}, {"$set": {"members": ment}})
        dbs.Data.update_one({"ids": str(counter)}, {"$set": {"MessageChannel": msgid}})
