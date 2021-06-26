import discord
import asyncio
import datetime
import pymongo
from dbmongo import db
from commands import meet
from commands import tasks
from remainder import remainder

client = discord.Client()
@client.event
async def on_ready():
    print("Connected to Server, Hurahhh!!")
    await remainder.remainder(client)

@client.event
async def on_message(message):
    if message.author.bot:
        return
    elif message.content.startswith('&schedule'):
        print("meet")
        await meet.scheduleMeet(message,client)
    elif message.content.startswith('&Task'):
        await tasks.Tasks(message)


client.run('ODQ5NjMyNjYwODkyNTQ5MTIx.YLeAEw.yqzSq3huUrmspRon0AGkAIwkpyk')
