import discord
from discord.ext import commands, tasks
from os import getenv
from datetime import datetime
import traceback

# https://discord.com/channels/1008227908617248798/1008227908617248802（この部分）
CHANNEL_ID = 1008227908617248802

client = discord.Client()

channel_sent = None

# 60秒に一回ループ
@tasks.loop(seconds=10)
async def loop():
    # 現在の時刻
    # now = datetime.now().strftime('%H:%M')
    # if now == '07:00':
    await channel_sent.send('10秒経ったよ') 

@client.event
async def on_ready():
    global channel_sent 
    channel_sent = client.get_channel(CHANNEL_ID)
    loop.start() #定期実行するメソッドの後ろに.start()をつける



token = getenv('DISCORD_BOT_TOKEN')
client.run(token)
