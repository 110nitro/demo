import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='-', description="ver1.0")

@bot.command()
async def ping(ctx):
    await ctx.send('pong')

#event
@bot.event
async def on_ready():
    await bot.change_presence(status=discord.Status.online, activity=discord.Streaming(name="Discord", url="https://www.youtube.com/watch?v=dQw4w9WgXcQ", details="Madagascar"))
    print('successfully connected')

bot.run('TOKEN')