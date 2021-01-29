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
        try:
            embed = discord.Embed(
                title = 'Error',
                description = f'{str(error)}',
                colour = discord.Colour.from_rgb(47,49,54) ,
                timestamp = datetime.utcnow())
            await ctx.send(embed = embed)
        except:
            print('error')
    
            
        

    

def setup(client):
    client.add_cog(Errors(client))
