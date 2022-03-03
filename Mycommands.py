from discord.ext import commands
client = commands.Bot(command_prefix='!')

@client.command()
async def sa(ctx):
    await ctx.send('as')