from dbmongo import db
import asyncio
from datetime import datetime
import pymongo
import discord
global times_used

dbs = db.connection()

client = discord.Client()

#&schedule Discord Bot @Pradipta Nandi 1d 2h 3m

async def scheduleMeet(message):
    keywords = ['m', 'h', 'd']
    command = message.content.split()
    title = command[1]
    keyword = command[-3:]
    dbs = db.connection()
    
    
    present_timestamp = datetime.now().timestamp()
    deadline_duration = present_timestamp
    for eachTime in keyword:
        duration = int(eachTime[:-1])
        seconds = {
            "m": duration * 60,
            "h": duration * 60 * 60,
            "d": duration * 24 * 60 * 60
        }

        k = eachTime[-1]

        deadline_duration = deadline_duration + seconds[k]


    schedule_date = datetime.fromtimestamp(deadline_duration)
    countmeet = dbs.Count_Meet.find()
    for item in countmeet:
        counter = item["count"]
        dbs.Data.insert_one({"ids": str(counter), "Topic": title,
                            "DateTime": schedule_date, "TimeStamp": deadline_duration, "Reminder": 2})
        print("Scheduled successfully!")
        await message.channel.send(f"Scheduled successfully! ID: {counter}")
        dbs.Count_Meet.update_one({"ids": "4"}, {"$inc": {"count": 1}})
        embed = discord.Embed(
            title="Meeting Scheduled💻",
            description="Topic: " +
            title,
            colour=discord.Colour.blue()
        )
        name = message.author
        embed.set_author(name=str(name)[:-5])
        embed.set_footer(text="Please attend the meeting")
        emoji1 = '✅'
        emoji2 = '❎'
        mentions = command[2:-3]
        men = mentions
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
        dbs.Data.update_one({"ids": str(counter)}, {
                            "$set": {"MessageChannel": msgid}})
