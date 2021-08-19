import discord
import datetime
from commands import meet
from commands import tasks
from commands import helpcmd
from commands import meetcmd
from commands import member
from remainder import remainder
from datetime import datetime
from discord import client
import os

intents = discord.Intents.default()
intents.members = True
client = discord.Client(intents=intents)


@client.event
async def on_ready():
    print('logged in as')
    print(client.user.name)
    print(client.user.id)
    print('-----')
    await remainder.remainder(client)
    
    
@client.event
async def on_member_join(member):
    guild = member.guild
    channel = discord.utils.get(guild.channels, name = "general")
    embed=discord.Embed(
        title="Welcome "+member.name+"!",
        description="This is the GCC Code Camp discord server!",
        color=0x0000FF,
        timestamp=datetime.utcnow()
    )
    embed.add_field(name="Name", 
                    value=member.mention, 
                    inline=True)
    embed.add_field(name="Who am I ?", 
                    value=f'Hello Adventurer !! I am the GuviBot. I was made for the sole purpose of helping you out in this amazing journey of yours with the GCC. So come along, as your very own adventure awaits!!!! ',
                    inline=False)
    embed.set_thumbnail(url=member.avatar_url)
    embed.set_author(name="GUVI Code Camp",
                     url="https://www.gccatsrm.tech/",
                     icon_url=guild.icon_url)
    embed.set_footer(text="                  ")
    embed.set_image(url="https://media.giphy.com/media/IgGcxqawkRc6y43Z6I/giphy.gif")

    try:
        await channel.send(embed=embed)
    except discord.InvalidArgument:
        print("Channel doesn't exist")

    await member.send(f'Hello {member.mention} !! I am the GuviBot. :robot: ')
    await member.send(f'You have just joined -- {guild.name}. Have Fun !! :partying_face: !!')
    
@client.event
async def on_member_leave(member):
    guild = member.guild
    channel = discord.utils.get(guild.channels, name = "general")

    embed=discord.Embed(
        title="Adios !! "+member.name+"!",
        description="It's sad but we will move on :cry: ",
        color=0x0000FF
    )
    embed.add_field(name="Name", 
                    value=member.mention, 
                    inline=True)
    embed.add_field(name="Message", 
                    value=f'Have a nice life!! ', 
                    inline=True)
    embed.set_thumbnail(url=member.avatar_url)


    try:
        await channel.send(embed=embed)
    except discord.InvalidArgument:
        print("Channel doesn't exist")


@client.event
async def on_message(message):
    if message.author.bot:
        return
    elif message.content.startswith('&schedule'):
        await meet.scheduleMeet(message)
    elif message.content.startswith('&Task'):
        await tasks.Tasks(message)
    elif message.content.startswith('&meet'):
        await meetcmd.meet(message)
    elif message.content.startswith('&member'):
        await member.membr(message)
    elif message.content.startswith('&help'):
        await helpcmd.help(message)

        
client.run(os.environ['DISCORD_TOKEN'])
