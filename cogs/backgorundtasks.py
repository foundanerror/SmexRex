import discord,random,requests,praw,io,sqlite3
from discord.ext import commands, tasks
from datetime import datetime
from itertools import cycle

status = cycle(['Testing','Still Testing'])

class Events(commands.Cog):
    def __init__(self, client):
        self.client = client
        client.remove_command("help")

    @commands.Cog.listener()
    async def on_ready(self):
        print("Bot is online.")
        self.change_status.start()


    @tasks.loop(seconds=10)
    async def change_status(self):
        game = discord.Game("with the API")
        await self.client.change_presence(status=discord.Status.do_not_disturb,activity=discord.Activity(type= discord.ActivityType.playing,name= f'Over {len(self.client.guilds)} Servers'))
    


def setup(client):
    client.add_cog(Events(client))
