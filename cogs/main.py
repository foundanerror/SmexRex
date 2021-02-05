import discord
from discord.ext import commands
import random
import requests
import asyncpraw
import io
import sqlite3
from datetime import datetime
from time import time

reddit = asyncpraw.Reddit(client_id = "K00Ni5DBXdefSQ", 
                    client_secret = "jpsli9Y2WXZjoybxs5pufLgd0teRWg",
                    user_agent = 'SmartSlayer1')

conn = sqlite3.connect("bot_memes.db")
c = conn.cursor()

c.execute("SELECT * FROM bot_memes")
limit = c.fetchall()
conn.commit()

def to_upper(argument):
    print(argument)
    return argument.upper()

class Main(commands.Cog):
    def __init__(self, client):
        self.client = client
        client.remove_command("help")
        self.launch_time = datetime.utcnow()

    
    @commands.command()
    async def meme(self,ctx):
        #l = len(limit)
        #meme = random.randint(1, l)
        

        #c.execute(f"SELECT * FROM bot_memes WHERE rowid = {meme}")
        #items = c.fetchall()
        #link = items[0][0]
        #name = items[0][1]
       # author = items[0][2]
        #permaLink = items[0][3]
        #upvotes = items[0][4]

        #r = requests.get(link, stream=True)
        
        #image_bytes = io.BytesIO(r.content)

        #create a file object in discordpy library
        #f = discord.File(image_bytes, 'meme.png')

        #send image in the channel

        table = []
        subreddit = await reddit.subreddit("memes")
        async for submission in subreddit.hot(limit=1000):
            table.append(tuple([submission.title,submission.permalink,submission.url,submission.author,submission.score]))


        randoml = random.randint(1,len(table))

        name = table[randoml][0]
        permalink = table[randoml][1]
        url = table[randoml][2]
        author = table[randoml][3]
        score = table[randoml][4]

        print(name,permalink,url,author,score)
        
        #await ctx.send(file=f)

    @commands.command()
    async def help(self, ctx):
        embed = discord.Embed(
            title = 'Help',
            description = 'Commands listed below',
            colour = discord.Colour.from_rgb(47,49,54),
            timestamp = datetime.utcnow()
        )
        embed.set_author(name = 'SmexRex', icon_url='https://media.discordapp.net/attachments/754414804361281598/804127527509295134/image0.png')
        embed.add_field(name = '../ping',value = '`Returns bot latency`',inline = False)
        embed.add_field(name = '../purge',value = '`Purges Specified amount of messages`',inline = False)
        embed.add_field(name = '../uptime',value = '`Returns bot uptime`',inline = False)
        embed.add_field(name = '../meme',value = '`Returns meme from reddit`',inline = False)
        await ctx.send(embed = embed)
    
    @commands.command()
    @commands.bot_has_permissions(manage_messages=True)
    async def purge(self,ctx,Ammount : int):
        await ctx.channel.purge(limit = Ammount)

    @commands.command()
    async def uptime(self,ctx):
        delta_uptime = datetime.utcnow() - self.launch_time
        hours, remainder = divmod(int(delta_uptime.total_seconds()), 3600)
        minutes, seconds = divmod(remainder, 60)
        days, hours = divmod(hours, 24)
        if days == 0 and hours == 0 and minutes == 0:
            await ctx.send(f"{seconds}s")
        elif days == 0 and hours == 0:
            await ctx.send(f'{minutes}m, {seconds}s')
        elif days == 0:
            await ctx.send(f'{hours}h, {minutes}m, {seconds}s')
        else:
            await ctx.send(f'{days}d, {hours}h, {minutes}m, {seconds}s')

    @commands.command()
    @commands.cooldown(1,5,commands.BucketType.category)
    async def ping(self,ctx):
        start = time()
        message = await ctx.send("Pong!")
        end = time()
        await message.edit(content=f"Pong! `{self.client.latency * 1000:,.0f}ms`, Response Time {(end-start)*1000:,.0f}")

    @commands.command(aliases = ['NumberGenerator'])
    async def randomNumber(self,ctx):
        Nums = [1,2,3,4,6,7,8,9,0]
        strl = ''
        
        for i in Nums:
            strl = strl + str(random.choice(Nums))
            
            if i == 3 or i == 7:
                strl = strl + ','
        await ctx.send(strl)

    @commands.command()
    async def guild(self, ctx):
        guilds  = self.client.guilds
        embed = discord.Embed(
            title = 'Guilds',
            colour = discord.Colour.from_rgb(47,49,54),
            timestamp = datetime.utcnow()
        )
        embed.set_author(name = 'SmexRex', icon_url='https://media.discordapp.net/attachments/754414804361281598/804127527509295134/image0.png')
        for i in guilds:
            embed.add_field(name = f'{i}',value = f'`{i.member_count}`',inline = False)

        await ctx.author.send(embed = embed)

    @commands.command()
    async def up(self,ctx, *, content: to_upper):
        embed = discord.Embed(
            title = 'Up',
            description = f'{str(content)}',
            colour = discord.Colour.from_rgb(47,49,54) ,
            timestamp = datetime.utcnow()
        )
        embed.set_author(name = 'SmexRex', icon_url='https://media.discordapp.net/attachments/754414804361281598/804127527509295134/image0.png')
        await ctx.send(embed = embed)

    @commands.command()
    async def delete(self,ctx):
        guild = ctx.message.guild

        for i in guild.channels:
            print('called')
            if str(i) == 'hi':
                    existing_channel = discord.utils.get(guild.channels, name=i)
                    # if the channel exists
                    if existing_channel is not None:
                        await existing_channel.delete()
                    # if the channel does not exist, inform the user
                    else:
                        await ctx.send(f'No channel named, "{i}", was found')
            else:
                print('nah')

def setup(client):
    client.add_cog(Main(client))