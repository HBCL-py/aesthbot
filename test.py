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
    print('Logged in as {0}'.format(bot.user))
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
    await bot.say(embed=e)
    
@bot.command()
async def servinfo(id: int):
    g = get_guild(id)
    if g.mfa_level == 1:
        a = "The server requires 2FA for administration."
    else:
        a = "The server doesn't require 2FA for administration."
    e = discord.Embed(title = "SERVER INFO",
                      color = discord.Colour(0x00ff00),
                      description = "**Server name is** "+str(g.name)+".\n\n**Created at:** "+str(g.created_at)+" UTC.\n\n**Server ID is** "+str(g.id)+"~\n\n**Server owner is** "+str(g.owner)+"~\n\n"+a+"\n\nThere are "+str(g.member_count)+" members.")
    e.set_thumbnail(url=g.icon_url)
    e.set_author(name="^_^")
    e.set_footer(text="Command requested by "+str(message.author)+".")
    await message.channel.send("==============================================")
    await message.channel.send(embed=e)
    await message.channel.send("==============================================")

bot.run(os.environ['BOT_TOKEN'])
