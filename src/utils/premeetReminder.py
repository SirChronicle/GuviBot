import discord

async def send_before_reminder(Client, MeetSchema):
    top = MeetSchema["Topic"]
    for id in MeetSchema['members']:
        if str(id) == 'r':
            embed = discord.Embed(
                title='Meeting in about 30 min🕓', description='Topic: ' + top, color=discord.Colour.green())
            embed.set_footer(text='Please join meeting!!')
            channel_id = MeetSchema["MessageChannel"]
            channel = Client.get_channel(channel_id)
            await channel.send(embed=embed)
        else:
            member = await Client.fetch_user(id)
            embed = discord.Embed(title='Meeting in about 30 min🕓',description='Topic: ' + top, color=discord.Colour.green())
            embed.set_footer(text='Please join meeting!!')
            await member.send(embed=embed)