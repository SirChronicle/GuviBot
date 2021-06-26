import discord
from commands import meet
from commands import tasks
from remainder import remainder
from commands import meetcmd
from commands import member
from commands import helpcmd

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
        await meet.scheduleMeet(message,client)
    elif message.content.startswith('&Task'):
        await tasks.Tasks(message)
    elif message.content.startswith('&meet'):
            await meetcmd.meet(message)
    elif message.content.startswith('&member'):
        await member.membr(message)
    elif message.content.startswith('&help'):
        await helpcmd.help(message)


client.run('ODQ5OTA3OTQ5MjYxNDIyNjAy.YLiAdQ.nJwOlDwPXlH0SQGcHZwcinMQFfM')
