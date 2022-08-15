import discord
from discord.ext import commands, tasks
from os import getenv
from datetime import datetime
import traceback

# https://discord.com/channels/1008227908617248798/1008227908617248802（この部分）
CHANNEL_ID = 988398446287405066

client = discord.Client()

channel_sent = None

target_members = [905072543919116308, 689663907257909248]


# 60秒に一回ループ
@tasks.loop(seconds=60)
async def loop():
    # 現在の時刻
    now = datetime.now().strftime('%H:%M')
    # 指定したい時刻から9時間引いた時刻
    #if now != '15:30':
        #return
    for ch in channel_sent.guild.voice_channels:
        for member in ch.members:
            if member.id not in target_members:
                continue
            await member.move_to(None)
            await channel_sent.send(f'{member.mention} おやすみ')

@client.event
async def on_ready():
    global channel_sent 
    channel_sent = client.get_channel(CHANNEL_ID)
    loop.start() #定期実行するメソッドの後ろに.start()をつける



token = getenv('DISCORD_BOT_TOKEN')
client.run(token)
