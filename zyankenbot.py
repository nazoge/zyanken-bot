import discord
import random
import time
TOKEN = 'your token here'
client = discord.Client()
@client.event
async def on_ready():
    print('ログインしました')
@client.event
async def on_message(message):
    if message.author.bot:
        return
    if message.content == '?zg':
        cpu=random.randint(1,3)
        if cpu==1:
            await message.channel.send("あなたはグーを選択しました\nコンピュータはグーを出しました\nあいこです")
        elif cpu==2:
            await message.channel.send("あなたはグーを選択しました\nコンピュータはチョキを出しました\nあなたの勝ちです")
        else:
            await message.channel.send("あなたはグーを選択しました\nコンピュータはパーを出しました\nあなたの負けです")
    elif message.content == '?zt':
        cpu=random.randint(1,3)
        if cpu==1:
            await message.channel.send("あなたはチョキを選択しました\nコンピュータはグーを出しました\nあなたの負けです")
        elif cpu==2:
            await message.channel.send("あなたはチョキを選択しました\nコンピュータはチョキを出しました\nあいこです")
        else:
            await message.channel.send("あなたはチョキを選択しました\nコンピュータはパーを出しました\nあなたの勝ちです")
    elif message.content == '?zp':
        cpu=random.randint(1,3)
        if cpu==1:
            await message.channel.send("あなたはパーを選択しました\nコンピュータはグーを出しました\nあなたの勝ちです")
        elif cpu==2:
            await message.channel.send("あなたはパーを選択しました\nコンピュータはチョキを出しました\nあなたの負けです")
        else:
            await message.channel.send("あなたはパーを選択しました\nコンピュータはパーを出しました\nあいこです")
client.run(TOKEN)