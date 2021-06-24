import discord
import asyncio
import datetime
import pymongo
from dbmongo import db
from commands import meet


client = discord.Client()
@client.event
async def on_ready():
    mydb = db.connection()
    print("Connected to Server, Hurahhh!!")

@client.event
async def on_message(message):
    if message.author.bot:
        return
    elif message.content.startswith('&schedule'):
        await meet.scheduleMeet(message)


client.run('ODQ5OTA3OTQ5MjYxNDIyNjAy.YLiAdQ.nJwOlDwPXlH0SQGcHZwcinMQFfM')
