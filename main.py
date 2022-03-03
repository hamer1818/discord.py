import discord
from discord.ext import commands
from functions import *
from Mycommands import *




TOKEN = "OTQ4ODgzNjM2NDI4NjIzODgy.YiCSwA.VTkzxkX5UaGT0agnA5M2vQvIcIs"
client = commands.Bot(command_prefix='bot ')

@client.event
async def on_ready():
    print('Bot hazır!: {}'.format(client.user.name))
    print('Bot ID: {}'.format(client.user.id))


@client.command()
async def sa(ctx):
    await ctx.send('as')


client.run(TOKEN)