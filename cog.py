import discord, os
from discord.ext import commands, tasks
import praw


client = commands.Bot(command_prefix = "../", intents=discord.Intents.all())

@client.command()
async def load(ctx, extension):
    client.load_extension(f'cogs.{extension}')
    print("loaded")

@client.command()
async def unload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')
    print("unloaded")
    

#f

for filename in os.listdir('./cogs'):
    if filename.endswith(".py"):
        client.load_extension(f'cogs.{filename[:-3]}')
        print(f"Loading: {filename}")

client.run("Nzk2NTExNjE3NzE3NzY0MTQ3.X_Y_QA.UrBZNiRrSNSQ3aL-w2jQZu7r390")