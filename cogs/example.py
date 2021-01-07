import discord
from discord.ext import commands
import random
import requests
import praw
import io
reddit = praw.Reddit(client_id = 'SoZ-V_ZEXQdCKw', 
                    client_secret = 'AqpnUH2WJ0iMBXa1Sl8A53zEyjDTYg', 
                    user_agent = 'SmartSlayewer1')


subreddit = reddit.subreddit("Animemes")
table = []
for submission in subreddit.hot(limit=1000):
    print(submission.url)
    table.append(submission.url)



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
        meme = random.randint(1,len(table))
        print(len(table))
        link = table[meme]
        r = requests.get(link, stream=True)
        
        image_bytes = io.BytesIO(r.content)

        #create a file object in discordpy library
        f = discord.File(image_bytes, 'meme.jpg')

        # send image in the channel
        await ctx.send(file=f)

def setup(client):
    client.add_cog(Example(client))