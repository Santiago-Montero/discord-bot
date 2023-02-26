# bot.py
import os

import discord
from discord.ext import commands

import requests

apikey = 'api_key=RGAPI-c19d28c7-653a-4536-a7a5-524ba4e8ef5a'
urlSummoner = 'https://la2.api.riotgames.com/lol/summoner/v4/summoners/by-name'
# THIS QUERY RETURN THIS OBJ
# {
#     "id": "84MSVlR6yKbpU5GpJL0NYOrT9zPMXUzOwnkwubfMT0Yfzg",
#     "accountId": "moH9YIzhM0vsq5znGwRRR-8xWV3UPP9HnuQhVeAOvvaMkyU",
#     "puuid": "Ths4u_x0kxWlJSSCrNTX-5Mu_Rc_lG2OE8G-Gqnj17WTYK5oO8oToK3kcyhHP26XOSwtwbSN6hIWgg",
#     "name": "Monthasi",
#     "profileIconId": 1387,
#     "revisionDate": 1677381350023,
#     "summonerLevel": 434
# }

client = discord.Client(intents=discord.Intents.default())
TOKEN = 'MTA3OTE2MDcwMzI4MzM2MzkwMg.GeanWf.49tFYpTjgDwe_Sl1YdvULlx23uOwX2bgChRbEk'
GUILD = '1008842568831877221'


def summonerLevel(summonerName):
    print(summonerName)
    resp = requests.get(
        urlSummoner + '/' + summonerName + '?' + apikey).json()
    if resp:
        return "Tu nivel es :" + str(resp['summonerLevel'])


@client.event
async def on_ready():
    for guild in client.guilds:
        if guild.name == GUILD:
            break
        print(
            f'{client.user} is connected to the following guild:\n' f'{guild.name}(id: {guild.id})')


@client.event
async def on_message(message):
    print(message)
    await message.channel.send(summonerLevel(message.content))


client.run(TOKEN)
