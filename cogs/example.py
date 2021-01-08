import discord
from discord.ext import commands
import random
import requests
import praw
import io
import sqlite3


conn = sqlite3.connect("bot_memes.db")
c = conn.cursor()

c.execute("SELECT * FROM bot_memes")
limit = c.fetchall()
conn.commit()

class Example(commands.Cog):
    def __init__(self, client):
        self.client = client
    
    @commands.Cog.listener()
    async def on_ready(self):
        print("Bot is online.")
    
    @commands.command()
    async def ping(self, ctx):
       await ctx.send("pong")
    
    @commands.command()
    async def meme(self,ctx):
        l = len(limit)
        meme = random.randint(1, l)
        

        c.execute(f"SELECT * FROM bot_memes WHERE rowid = {meme}")
        items = c.fetchall()
        #print(meme)
        link = items[0][0]
        r = requests.get(link, stream=True)
        
        image_bytes = io.BytesIO(r.content)

        #create a file object in discordpy library
        f = discord.File(image_bytes, 'meme.jpg')

        #send image in the channel
        await ctx.send(file=f)

def setup(client):
    client.add_cog(Example(client))