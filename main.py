# bot.py
import os

import discord
from discord.ext import commands

client = discord.Client(intents=discord.Intents.default())
TOKEN = 'MTA3OTE2MDcwMzI4MzM2MzkwMg.GgI1qc.nWweg7V9N8ZIwpeSyZkm3Jfj02fFE8yf6nOP_k'
GUILD = '1008842568831877221'


bot = commands.Bot(command_prefix='_', description="this is a testing bot")


# Ping-pong
@bot.command()
async def ping(ctx):
    await ctx.send('pong')


@client.event
async def on_ready():
    for guild in client.guilds:
        if guild.name == GUILD:
            break
        print(
            f'{client.user} is connected to the following guild:\n' f'{guild.name}(id: {guild.id})')


@client.event
async def on_message(message):
    if 'hola' in message.content.lower():
        print(message)
        await message.channel.send('hola ' + message.author.name)


@client.command
async def on_message(message):
    if 'hola' in message.content.lower():
        print(message)
        await message.channel.send('hola ' + message.author.name)


client.run(TOKEN)
