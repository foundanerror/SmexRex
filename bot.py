import discord 
from discord.ext import commands

client = commands.Bot(command_prefix = "^", intents=discord.Intents.all())

@client.event
async def on_ready():
    print("bot is online")


@client.command()
async def ping(ctx):
    print(ctx)
    await ctx.send(f'My Ping : {round(client.latency * 1000)}ms')




client.run("Nzk2NTExNjE3NzE3NzY0MTQ3.X_Y_QA.UrBZNiRrSNSQ3aL-w2jQZu7r390")