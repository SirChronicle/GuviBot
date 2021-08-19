import datetime
import discord
from utils import preReminder
from dbmongo import db

client = discord.Client()
async def Tasks(message):
    syntax = '<&Task> <Title> <@all mentions> <duration[whole number]> <["m", "h", "d"]>'
    if message.author.bot:
        return
    elif message.content.startswith('&Task'):
        keywords = ['m','h','d']
        command = message.content.split()
        error=True
        if len(command)<5 or command[-1] not in keywords:
            await message.channel.send(syntax)
            error=False
        elif len(command)>=5:
            try:
                if not command[2].startswith('<@!'):
                    raise
            except:
                await message.channel.send('Name of the task should be a single word!')
                error=False

            try:
                duration = int(command[-2])
            except:
                await message.channel.send('duration should be a number')
                error=False

            if error: 
                title = command[1]
                keyword = command[-1]
                Task_details = db.connection()
                seconds = {
                    "m":duration * 60 ,
                    "h":duration * 60 * 60 ,
                    "d": duration * 24 * 60 * 60
                }
                present_timestamp = datetime.datetime.now().timestamp()
                deadline_duration = present_timestamp + seconds[keyword]
                deadline_date = datetime.datetime.fromtimestamp(deadline_duration)
                taggedusers = command[2:-2]
                mention = list()
                for user in taggedusers:
                    if user.startswith('<@!'):
                        mention.append(user[3:-1])


                Role = await message.guild.create_role(name=title, hoist = True)
                data = {
                    "Task_Title": title,
                    "deadline": deadline_duration,
                    "deadline_date": deadline_date,
                    "mentions": mention,
                    "role_id": Role.id
                }   
                Task_details.discord.insert_one(data)
                await preReminder.send_before_reminder(data, message)
