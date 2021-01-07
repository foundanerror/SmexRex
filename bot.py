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

@client.command()
@commands.has_role('')
async def ban(ctx, member : discord.Member, *, reason = None):
    await member.ban(reason = reason)


@client.command()
@commands.has_permissions(ban_members = True)
async def unban(ctx, *, member):
    banned_users = await ctx.guild.bans()
    member_name, member_discriminator = member.split("#")

    for ban_entry in banned_users:
        user = ban_entry.user

        if (user.name, user.discriminator) == (member_name, member_discriminator):
            await ctx.guild.unban(user)
            await ctx.send(f'Unbanned {user.mention}')
            return


client.run("Nzk2NTExNjE3NzE3NzY0MTQ3.X_Y_QA.UrBZNiRrSNSQ3aL-w2jQZu7r390")