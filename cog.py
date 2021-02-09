import discord, os
from discord.ext import commands, tasks
import asyncpraw


client = commands.Bot(command_prefix = "!", intents=discord.Intents.all())

@client.command()
async def load(ctx, extension):
    client.load_extension(f'cogs.{extension}')
    print("loaded")

@client.command()
async def unload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')
    print("unloaded")
    
@client.command()
async def reload(ctx, extension):
    if str(extension) == 'all':
        for filename in os.listdir('./cogs'):
            if filename.endswith(".py"):
                client.reload_extension(f'cogs.{filename[:-3]}')
                print(f"Loading: {filename}")
    else:
        try:
            client.reload_extension(f'cogs.{extension}')
            await ctx.send(f"Reloading {extension}.py")
        except:
            await ctx.send('Error occured reloading extension')       

         
    



for filename in os.listdir('./cogs'):
    if filename.endswith(".py"):
        client.load_extension(f'cogs.{filename[:-3]}')
        print(f"Loading: {filename}")

client.run("Token")
