import discord,random,requests,praw,io,sqlite3
from discord.ext import commands, tasks
from datetime import datetime
from itertools import cycle


class Errors(commands.Cog):
    def __init__(self, client):
        self.client = client
        client.remove_command("help")
        
    @commands.Cog.listener()
    async def on_command_error(self,ctx,error):
        await ctx.send(error)
        

    

def setup(client):
    client.add_cog(Errors(client))
