import discord
import os
from random import randint
import time
from discord.ext import commands
import asyncio
import praw
import prawcore
from scripts.yt import *

bot = commands.Bot(command_prefix='~')

@bot.event
async def on_ready():
    print('Logged in as {0}'.format(bot.user.name))
    print("Created by HBell_CL.py#5144 and Alexei Стуков#1672~")
    print("Using discord.py v"+discord.__version__)
    print("__________________________________________________________________________")
    
@bot.command(pass_context = True)
async def botinfo(ctx):
    e = discord.Embed(title="**BOT INFO**",
                      description="""**Owners:** HBell_CL.py#5144 and Alexei Стуков#1672 =^.^=
[<:furryfren2:463616355900588062>][<:lopez:456587657837936642>]
**The bot was created** at """+str(bot.user.created_at)+"""~
**The bot is present** in """+str(len(bot.guilds))+" server(s)~")
    e.set_thumbnail(url=bot.user.avatar_url)
    e.set_footer(text="La weá weón fsdfdslkñsfls.")        
    await ctx.send(embed=e)
    
bot.run(os.environ['BOT_TOKEN'])
