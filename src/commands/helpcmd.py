import discord

async def help(message):
    embed = discord.Embed(
        title="For scheduling meeting:\n",
        description="Commands of Purpose",


        colour=discord.Colour.blue()
    )
    embed.add_field(name='\n\nFor assigning Task:',
                    value='&Task <Title> <@all mentions> <duration[whole number]> <["m", "h", "d"]>', inline=False)
    embed.add_field(name='\n\n\nFor scheduling meetings:',
                    value='&schedule <Topic>  <Info>  <DateTime>  <@all mentions>\n(Double space between each argument from after Topic(for scheduling meet only))')
    embed.add_field(name='\n\n\nFor no. of members(only if sent personally):',
                    value='&member count <meet ID[whole number]>', inline=False)
    embed.add_field(name='\n\n\nFor no. of meet:',
                    value='&meet count', inline=False)
    await message.channel.send(embed=embed)
