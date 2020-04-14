import discord
from discord.ext import commands

client = commands.Bot(command_prefix = '!')

@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.idle, activity=discord.Game('Dipped in Cheese!'))
    print('klar!')

@client.event
async def on_member_join(member):
    print(f'{member} connected to da server')

@client.event
async def on_member_remove(member):
    print(f'{member} ran away:(')

@client.command()
async def clear(ctx, amount=5):
    await ctx.channel.purge(limit=amount)
    
@client.command()
async def join(ctx):
    channel = ctx.author.voice.channel
    await channel.connect()
    
@client.command()
async def leave(ctx):
    await ctx.voice_client.disconnect()

@client.command()
async def sig(ctx, arg):
    await ctx.send(arg)

client.run('Njc5NjY4NjMxODMwNzkwMTYw.Xk0s-w.UH2fANKB4_M0f_TqFltNUGmcb7o')

