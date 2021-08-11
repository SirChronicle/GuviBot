import discord
import asyncio
import datetime
import pymongo
from dbmongo import db
from commands import meet
from commands import tasks
from commands import meetcmd
from commands import member
from remainder import remainder

client = discord.Client()
@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
    await remainder.remainder(client)

@client.event
async def on_message(message):
    if message.author.bot:
        return
    elif message.content.startswith('&schedule'):
        print("meet")
        await meet.scheduleMeet(message)
    elif message.content.startswith('&Task'):
        await tasks.Tasks(message)
    elif message.content.startswith('&meet'):
        await meetcmd.meet(message)
    elif message.content.startswith('&member'):
        await member.membr(message)

client.run('ODQ5OTA3OTQ5MjYxNDIyNjAy.YLiAdQ.nJwOlDwPXlH0SQGcHZwcinMQFfM')
