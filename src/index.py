import discord

import os
import dotenv

import datetime

from urllib import parse, request
import re

from discord.ext import commands
from dotenv import load_dotenv



bot = commands.Bot(command_prefix='-', description="ver1.0")

@bot.command()
async def Hello(ctx):
    await ctx.send('World')

@bot.command()
async def embed(ctx):
    embed = discord.Embed(title=f"{ctx.guild.name}", description=f"ewe for {ctx.guild.name}", timestamp=datetime.datetime.utcnow(), color=discord.Color.blue())
    embed.set_thumbnail(url=f"https://cdn.discordapp.com/icons/{ctx.guild.id}/{ctx.guild.icon}.webp?size=96")
    await ctx.send(embed=embed)

@bot.command()
async def search(ctx, * ,search):
    busqueda = parse.urlencode({'search_query':search})
    contenido = request.urlopen('http://www.youtube.com/results?' + busqueda)
    resultados = re.findall(r"watch\?v=(\S{11})", contenido.read().decode())
    #print(resultados)
    await ctx.send('https://www.youtube.com/watch?v=' + resultados[0])

@bot.command()
async def play(ctx, url : str):
    vc = discord.utils.get(ctx.guild.voice_channels, name='Sala I')
    voz = discord.utils.get(bot.voice_clients, guild=ctx.guild)
    await vc.connect()










#event
@bot.event
async def on_ready():
    await bot.change_presence(status=discord.Status.online, activity=discord.Streaming(name="Discord", url="https://www.youtube.com/watch?v=dQw4w9WgXcQ", details="Madagascar"))
    print('successfully connected')


load_dotenv()
TOKEN = os.getenv('TOKEN')
bot.run(TOKEN)