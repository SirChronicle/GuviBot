import discord
client = discord.Client()
async def send_before_reminder(TaskSchema, message):
    for id in TaskSchema['mentions']:
        member = await message.guild.fetch_member(int(id))
        Role = discord.utils.get(message.guild.roles, name=TaskSchema['Task_Title'])
        await member.add_roles(Role)
        #member = await client.fetch_user(int(id))
        msg = f'''
            {member.mention}
            You have been assigned with {TaskSchema['Task_Title']} Project
            The Deadline for the given task is {TaskSchema['deadline_date'].date()}
            Please submit your Task on or before {TaskSchema['deadline_date'].time().hour}:{TaskSchema['deadline_date'].time().minute}
        '''
        title = f'''
        Task Assignment
💻💻💻💻💻
        '''
        embed = discord.Embed(title=title, description= msg, color=discord.Colour.green())
        embed.add_field(name = 'Title of Project', value = TaskSchema['Task_Title'])
        embed.add_field(name = 'Deadline', value = f"{TaskSchema['deadline_date'].date()}")
        embed.set_thumbnail(url = member.avatar_url)
        await member.send(embed=embed)