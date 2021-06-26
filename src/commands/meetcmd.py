from dbmongo import db
import discord
global times_used

dbs = db.connection()


client = discord.Client()

async def meet(message):
    index = message.content.index(' ')
    index = index + 1
    main_message = message.content[index:]
    sch = main_message.split()
    arg1 = sch[0]
    if arg1 == 'count':
        meet = dbs.Data.find()
        count = 0
        for item in meet:
            count += 1
        await message.channel.send(f"No. of pending meets: {count}")
