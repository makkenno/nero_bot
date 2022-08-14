import discord
from discord.ext import commands, tasks
from os import getenv
from datetime import datetime
import traceback

# https://discord.com/channels/1008227908617248798/1008227908617248802（この部分）
CHANNEL_ID = 1008227908617248802

bot = commands.Bot(command_prefix='/')
client = discord.Client()


@bot.event
async def on_command_error(ctx, error):
    orig_error = getattr(error, "original", error)
    error_msg = ''.join(traceback.TracebackException.from_exception(orig_error).format())
    await ctx.send(error_msg)


@bot.command()
async def ping(ctx):
    await ctx.send('更新したよ')
    
# 60秒に一回ループ
@tasks.loop(seconds=10)
async def loop():
    # 現在の時刻
    now = datetime.now().strftime('%H:%M')
    # if now == '07:00':
    channel = client.get_channel(CHANNEL_ID)
    await channel.send('10秒経ったよ')  

#ループ処理実行
loop.start()


token = getenv('DISCORD_BOT_TOKEN')
bot.run(token)
client.run(token)
