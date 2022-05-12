import discord
import os
import dotenv

from discord.ext import commands
from dotenv import load_dotenv



bot = commands.Bot(command_prefix='-', description="ver1.0")

@bot.command()
async def uwu(ctx):
    await ctx.send('uwu')

#event
@bot.event
async def on_ready():
    await bot.change_presence(status=discord.Status.online, activity=discord.Streaming(name="Discord", url="https://www.youtube.com/watch?v=dQw4w9WgXcQ", details="Madagascar"))
    print('successfully connected')


load_dotenv()
TOKEN = os.getenv('TOKEN')
bot.run(TOKEN)