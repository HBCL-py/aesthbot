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
    
@bot.event
async def on_member_remove(member):
    try:
        await member.guild.system_channel.send(':cry: {} has left this server :['.format(member))
    except AttributeError:
        return
    
@bot.event
async def on_member_join(member):
    try:  
        await member.guild.system_channel.send(':wave: <@{}> just joined this server :]'.format(member.id))
    except AttributeError:
        return
    
@bot.event
async def on_member_ban(server,member):
    try:
        await server.system_channel.send(':no_entry_sign: {} just got banned. >:[ :hammer:'.format(member))
    except AttributeError:
        return
    
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

@bot.command(pass_context = True)
async def servinfo(ctx, id = None):
    if id == None:
        id = ctx.guild.id
    else:
        try:
            id = int(id)
        except ValueError:
            await ctx.send("Please input a valid ID.")
            return
        g = bot.get_guild(id)
        if g == None:
            await ctx.send("That server either doesn't exist, or I'm not present on it.")
            return
    if g.mfa_level == 1:
        a = "The server requires 2FA for administration."
    else:
        a = "The server doesn't require 2FA for administration."
    e = discord.Embed(title = "SERVER INFO",
                      color = discord.Colour(0x00ff00),
                      description = "**Server name is** "+str(g.name)+".\n\n**Created at:** "+str(g.created_at)+" UTC.\n\n**Server ID is** "+str(g.id)+"~\n\n**Server owner is** "+str(g.owner)+"~\n\n"+a+"\n\nThere are "+str(g.member_count)+" members.")
    e.set_thumbnail(url=g.icon_url)
    e.set_author(name="^_^")
    e.set_footer(text="Command requested by "+str(ctx.author)+".")
    await ctx.send("===============================================")
    await ctx.send(embed=e)
    await ctx.send("===============================================")

@bot.command(pass_context=True)
async def ping(ctx):
    i = randint(1,5)
        if i == 1:
            await ctx.send("It's time to chew gum and kick ass... | "+str(round(bot.latency, 5))+"s")
        if i == 2:
            await ctx.send("Pong~ | "+str(round(bot.latency, 5))+"s")
        if i == 3:
            await ctx.send("A ping is a ping, you can't say it's only a half. | "+str(round(bot.latency, 5))+"s")
        if i == 4:
            await ctx.send("Beep boop~ | "+str(round(bot.latency, 5))+"s")
        if i == 5:
            await ctx.send("In case of doubt, shout Bell out! | "+str(round(bot.latency, 5))+"s")
    
bot.run(os.environ['BOT_TOKEN'])
