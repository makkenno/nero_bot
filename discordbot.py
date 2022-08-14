from discord.ext import commands, tasks
from os import getenv
from datetime import datetime
import traceback

bot = commands.Bot(command_prefix='/')


@bot.event
async def on_command_error(ctx, error):
    orig_error = getattr(error, "original", error)
    error_msg = ''.join(traceback.TracebackException.from_exception(orig_error).format())
    await ctx.send(error_msg)


@bot.command()
async def ping(ctx):
    await ctx.send('やぴまる')
    
# 60秒に一回ループ
@tasks.loop(seconds=60)
async def loop():
    # 現在の時刻
    now = datetime.now().strftime('%H:%M')
    # if now == '07:00':
    channel = client.get_channel(CHANNEL_ID)
    await channel.send('おはよう')  

#ループ処理実行
loop.start()


token = getenv('DISCORD_BOT_TOKEN')
bot.run(token)
