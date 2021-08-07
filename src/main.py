import discord
import os
import requests
import json
from keep_alive import keep_alive
import asyncio
import random
#from replit import db
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv('api_key')
token = os.getenv('token')
print(token)
client = discord.Client()


x = ["what's up","whats up","what's going on in the world","get me some news","news"]

response = requests.get("https://newsapi.org/v2/top-headlines?sources=techcrunch&apiKey="+api_key)
# response = requests.get("https://gnews.io/api/v4/search?q=example&token=d3e4d488715f19959b934cf3ef7029df")
json_data = json.loads(response.text)
#print(json_data)

def get_news():
  randomNumber=random.randint(0,len(json_data["articles"]))
  news = "\n"+"**"+json_data["articles"][randomNumber]["title"]+"**"+"\n"+"```"+json_data["articles"][randomNumber]["description"]+"```"+"\n"+json_data["articles"][randomNumber]["urlToImage"]+"\n"+'*Published At:'+json_data["articles"][randomNumber]["publishedAt"]+"*"
  print(news)
  return (news)


@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))
  await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name='The News'))

@client.event
async def on_guild_join(guild):
    channel = await guild.create_text_channel('breaktech')
    await channel.send("Hello! I am BreakTech, bringing you the latest technology news!")
    channel = await guild.create_text_channel('24hour')
    await channel.send("24x7 news, brought to you by BreakTech.")

    

channels = ['breaktech']
channel = ['24hour']

@client.event
async def on_message(message):
  if str(message.channel) in channels:
    if message.author == client.user:
      return
    if message.content.startswith('!hi'):
      await message.channel.send('Hello!')
    if message.content.startswith('!headline'):
      news = get_news()
      await message.channel.send(news)
    msg = message.content
    if any(word in msg for word in x):
      news = get_news()
      await message.channel.send(news)


  if str(message.channel) in channel:
    if message.content.startswith('24x7'):
      async def report():
        news = get_news()
        await message.channel.send(news)
        await asyncio.sleep(3600)
        await report()
      await report()
    
keep_alive()

#my_secret = os.environ['TOKEN']
client.run(token)
