import discord

import datetime

import os

from discord.ext import commands


intent = discord.Intents.all()

client = discord.Client()


@client.event

async def on_ready():
    print(client.user)
    print("봇 준비 완료")
    game = discord.Game("빙산봇 업데이트")
    await client.change_presence(status=discord.Status.online, activity=game)


@client.event 

async def on_message(message):
    if message.content == "!테스트":
        await message.channel.send("빙산봇은 현재 정상 작동중 입니다 : D")


    if message.content == "!내정보":
        embed = discord.Embed(color=discord.Colour.red(), title="개발중 ( 제목 )", description="개발중 ( 설명 )")
        await message.channel.send(embed=embed)


    if message.content.startswith("!청소"):
        number = int(message.content.split(" ")[1])
        await message.delete()
        await message.channel.purge(limit=number)
        await message.channel.send(f"{number}개의 메세지 삭제 완료 : D")




"""@client.command()
async def ban(ctx, member : discord.Member, *, reason=None):
    await member.kick(reason=reason)
"""

"""@client.command()
async def kick(ctx, member : discord.)
"""





access_token = os.environ["BOT_TOKEN"]
client.run(access_token)


