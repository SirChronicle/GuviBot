import discord
# client = discord.Client()
async def send_after_reminder(Client, TaskSchema):
    role=Client.guilds[0].get_role(TaskSchema['role_id'])
    if role:
        await role.delete()
        for id in TaskSchema['mentions']:
            member = await Client.fetch_user(id)
            msg = f'''
                {member.mention}
                The deadline for {TaskSchema['Task_Title']} Project/task assigned to you is completed
                Please make sure to submit it if you haven't submitted it yet
            '''
            title = f'''
            Task deadline
   🕖🕖🕖🕖🕖
            '''
            embed = discord.Embed(title=title, description= msg, color=discord.Colour.green())
            embed.set_thumbnail(url = member.avatar_url)
            await member.send(embed=embed)
