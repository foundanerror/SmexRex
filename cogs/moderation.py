import discord,random,requests,io,sqlite3
from discord.ext import commands, tasks
from datetime import datetime
from itertools import cycle


class Moderation(commands.Cog):
    def __init__(self, client):
        self.client = client
        client.remove_command("help")

    @commands.command()
    async def joined(self,ctx, member: discord.Member):
        await ctx.send('{0} joined on {0.joined_at}'.format(member))


def setup(client):
    client.add_cog(Moderation(client))