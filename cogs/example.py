import discord
from discord.ext import commands
import random
import requests
import praw
import io
import sqlite3
from datetime import datetime
import time


conn = sqlite3.connect("bot_memes.db")
c = conn.cursor()

c.execute("SELECT * FROM bot_memes")
limit = c.fetchall()
conn.commit()

class Example(commands.Cog):
    def __init__(self, client):
        self.client = client
        client.remove_command("help")
        self.launch_time = datetime.utcnow()

    
    @commands.command()
    async def meme(self,ctx):
        l = len(limit)
        meme = random.randint(1, l)
        

        c.execute(f"SELECT * FROM bot_memes WHERE rowid = {meme}")
        items = c.fetchall()
        icon = ctx.guild.icon_url
        link = items[0][0]
        name = items[0][1]
        author = items[0][2]
        permaLink = items[0][3]
        upvotes = items[0][4]

        #r = requests.get(link, stream=True)
        
        #image_bytes = io.BytesIO(r.content)

        #create a file object in discordpy library
        #f = discord.File(image_bytes, 'meme.png')

        #send image in the channel
        embed = discord.Embed(
            title = name,
            description = f"[{author}](https://www.reddit.com{permaLink})",
            colour = discord.Colour.green(),
            timestamp = datetime.utcnow()
        )
        embed.set_footer(text=f'Memes From Reddit, UpVote: 👍{upvotes}')
        embed.set_author(name = 'Gay Haven', icon_url=icon)
        embed.set_image(url = str(link))
        await ctx.send(embed = embed)
        #await ctx.send(file=f)

    @commands.command()
    async def help(self, ctx):
        embed = discord.Embed(
            title = 'Help',
            description = 'Commands listed below',
            colour = discord.Colour.green(),
            timestamp = datetime.utcnow()
        )
        embed.add_field(name = '../ping',value = '`Returns bot latency`',inline = False)
        embed.add_field(name = '../purge',value = '`Purges Specified amount of messages`',inline = False)
        embed.add_field(name = '../uptime',value = '`Returns bot uptime`',inline = False)
        embed.add_field(name = '../meme',value = '`Returns meme from reddit`',inline = False)
        await ctx.send(embed = embed)
    
    @commands.command()
    @commands.bot_has_permissions(manage_messages=True)
    async def purge(self,ctx,Ammount : int):
        await ctx.channel.purge(limit = Ammount)

    @commands.command()
    async def uptime(self,ctx):
        delta_uptime = datetime.utcnow() - self.launch_time
        hours, remainder = divmod(int(delta_uptime.total_seconds()), 3600)
        minutes, seconds = divmod(remainder, 60)
        days, hours = divmod(hours, 24)
        if days == 0 and hours == 0 and minutes == 0:
            await ctx.send(f"{seconds}s")
        elif days == 0 and hours == 0:
            await ctx.send(f'{minutes}m, {seconds}s')
        elif days == 0:
            await ctx.send(f'{hours}h, {minutes}m, {seconds}s')
        else:
            await ctx.send(f'{days}d, {hours}h, {minutes}m, {seconds}s')

    @commands.command()
    async def ping(self,ctx):
        message = await ctx.send("Pong!")
        ping = self.client.latency
        await message.edit(content=f"Pong!  `{int(ping)}ms`")
        print(f'Ping {int(ping)}ms')

def setup(client):
    client.add_cog(Example(client))