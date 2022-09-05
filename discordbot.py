import discord
import random
from discord.ext import commands, tasks
from os import getenv
from datetime import datetime
import traceback

# https://discord.com/channels/1008227908617248798/1008227908617248802（この部分）
CHANNEL_ID = 988398446287405066

client = discord.Client()

channel_sent = None

target_members = [905072543919116308, 642474473802694687, 802487731786874880, 947106212674175027]
# 指定したい時刻から9時間引いた時刻
target_time =  ['13:30','14:00','14:30','15:00','15:30','16:00','16:30','17:00','17:30','18:00','18:30','19:00','19:30','20:00','20:30']



# 60秒に一回ループ
@tasks.loop(seconds=30)
async def loop():
    # 現在の時刻
    target_member = random.choice(target_members)
    now = datetime.now().strftime('%H:%M')
    #if not (now in target_time):
    #   return
    for ch in channel_sent.guild.voice_channels:
        for member in ch.members:
            if member.id == target_member:
                await member.move_to(None)
                await channel_sent.send(f'{member.mention} バイバイ')
                break

            

@client.event
async def on_ready():
    global channel_sent 
    channel_sent = client.get_channel(CHANNEL_ID)
    loop.start() #定期実行するメソッドの後ろに.start()をつける



token = getenv('DISCORD_BOT_TOKEN')
client.run(token)
