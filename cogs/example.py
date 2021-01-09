import discord
from discord.ext import commands
import random
import requests
import praw
import io
import sqlite3
from datetime import datetime


conn = sqlite3.connect("bot_memes.db")
c = conn.cursor()

c.execute("SELECT * FROM bot_memes")
limit = c.fetchall()
conn.commit()

class Example(commands.Cog):
    def __init__(self, client):
        self.client = client
        client.remove_command("help")

    @commands.command()
    async def ping(self, ctx):
       await ctx.send("Pong")
    
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
        embed.set_thumbnail(url = icon)
        await ctx.send(embed = embed)
        #await ctx.send(file=f)

    @commands.command()
    async def help(self, ctx):
        print("hmmmm")
        


def setup(client):
    client.add_cog(Example(client))
    print("setup")