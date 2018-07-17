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

rapi = praw.Reddit(client_id=os.environ['REDDIT_ID'],
                     client_secret=os.environ['REDDIT_SECRET'],
                     user_agent="aesthbot-discordbot[python] v1.4.5 (by /u/thehellbell)")

if rapi.read_only:
    print("The Reddit instance is in READ ONLY mode.")
else:
    print("The Reddit instance is in AUTHORIZED mode.")

owners = [264195450859552779, 403557634998796288]

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
        
@bot.command(pass_context=True)
async def night(ctx):
    if ctx.author.id in owners:
        print("SHUTDOWN STARTING...")
        t = await ctx.send('Restarting... ')
        for i in range(3):
            await asyncio.sleep(0.75)
            m = '.'*(i+1)
            await t.edit(content=m)
        await asyncio.sleep(1)
        await t.edit(content='Ｇｏｏｄｂｙｅ．')
        await asyncio.sleep(1)
        await t.edit(content='ＺＺＺ．．．')
        await bot.logout()
    else:
        await ctx.send("ERROR: Owner-only command.")
    
@bot.command(pass_context = True)
async def aesth(ctx, msg = None):
    if msg == None:
        msg = """El veloz murciélago hindú comía feliz cardillo y kiwi. La cigüeña tocaba el saxofón detrás del palenque de paja.
The quick brown fox jumps over the lazy dog."""
    tab =  "　ＡＢＣＤＥＦＧＨＩＪＫＬＭＮＯＰＱＲＳＴＵＶＷＸＹＺａｂｃｄｅｆｇｈｉｊｋｌｍｎｏｐｑｒｓｔｕｖｗｘｙｚ１２３４５６７８９０！＂＃＄％＆／（）＝＇＼？＋＊［｛＾］｝｀，；．：－＿＜＞"
    tab2 = " ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890!"+'"'+"#$%&/()='"+'\\'+'?+*[{^]}`,;.:-_<>'
    tran = str.maketrans(tab2, tab)
    await ctx.send(msg.translate(tran))
    
@bot.command(pass_context=True)    
async def echo(ctx, msg = None):
    if msg == None:
        await ctx.send("Please, input the message to echo.")
        return
    await ctx.send(msg)
    await ctx.message.delete()
    
@bot.command(pass_context=True)
async def aesnick(ctx):
    tab =  "　ＡＢＣＤＥＦＧＨＩＪＫＬＭＮＯＰＱＲＳＴＵＶＷＸＹＺａｂｃｄｅｆｇｈｉｊｋｌｍｎｏｐｑｒｓｔｕｖｗｘｙｚ１２３４５６７８９０！＂＃＄％＆／（）＝＇＼？＋＊［｛＾］｝｀，；．：－＿＜＞"
    tab2 = " ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890!"+'"'+"#$%&/()='"+'\\'+'?+*[{^]}`,;.:-_<>'
    tran = str.maketrans(tab2, tab)
    t = ctx.author.nick
    if t is None:
        t = ctx.author.name
    try:
        await ctx.author.edit(nick = t.translate(tran))
        print("ACTION: Changed nickname of user {0}: '{1}' to '{2}'.".format(ctx.author, t, t.translate(tran)))
    except discord.errors.Forbidden:
        await ctx.send("ERROR: My privilege is too low...")
        
@bot.command(pass_context = True)
async def gameset(ctx, msg = None):
    if ctx.author.id in owners:
        if msg == None:
            await ctx.send("Please give an input.")
            return
        await bot.change_presence(activity=discord.Game(msg))
        print("ACTION: Status set to: 'Playing "+msg+"'")
        await ctx.send("*Playing status* set to: '"+msg+"'")
    else:
        await ctx.send("ERROR: Owner-only command.")
        
@bot.command(pass_context = True)
async def usern(ctx, *, msg = None):
    if ctx.author.id in owners:
        if msg == None:
            await ctx.send("Please give an input.")
            return
        await bot.user.edit(username=msg)
        print("ACTION: Username set to: '"+msg+"'")
        await ctx.send("Username set to: '"+msg+"'")
    else:
        await ctx.send("ERROR: Owner-only command.")
        
@bot.command(pass_context = True)
async def userinfo(ctx, *, msg = None):
    if len(ctx.message.mentions) < 2:
        if len(ctx.message.mentions) == 1:
            author = ctx.message.mentions[0]
            j = True
        else:
            if msg == None:
                msg = ctx.author.id
                j = True
            try:
                msg = int(msg)
            except ValueError:
                await ctx.send("Please input a valid ID.")
                return
            author = ctx.guild.get_member(msg)
            j = True
            if author == None:
                author = await bot.get_user_info(msg)
                j = False
        try:
            name = author.name
            uid = author.id
            disc = author.discriminator
            avatar = author.avatar_url
            if avatar == None:
                avatar = author.default_avatar_url
            if j:
                nick = author.display_name
            else:
                nick = "**-**"
            time = author.created_at
            if j:
                join = author.joined_at
            else:
                join = "**-**"
            if j:
                r = "Yes :white_check_mark:"
            else:
                r = "No :x:"
            embed = discord.Embed(title="USER INFO",
                                  color=discord.Colour(0xff0bb7),
                                  description="**Username#ID:** "+name+"#"+disc+"\n\n**User ID:** "+str(uid)+"\n\n**Guild Nickname:** "+nick+"\n\n**UTC Creation Time:** "+str(time)+"\n\n**UTC Guild joined at:** "+str(join)+"\n\n**Is the user in this server?** "+r)
            embed.set_thumbnail(url=avatar)
            embed.set_author(name="^_^")
            embed.set_footer(text="Command requested by "+str(ctx.author)+".")
            await ctx.send("#############################")
            await ctx.send(embed=embed)
            await ctx.send("#############################")
            print(author)
        except AttributeError:
            await ctx.send("The inputted user is invalid.")
    else:
        await ctx.send("Ping less than 2 people only!")
        
@bot.command(pass_context=True)        
async def servers(ctx):
    if ctx.author.id in owners:
        c = 1
        for server in bot.guilds:
            await ctx.send(str(c)+".-) "+str(server.name)+"; ID = "+str(server.id)+"~")
            c += 1        
        
@bot.command(pass_context=True)
async def reddit(ctx, msg=None):
    if msg == None:
        await ctx.send("Please give a subreddit!")
        return
    sr = msg
    a = []
    try:
        for submission in rapi.subreddit(sr).hot(limit=50):
            a.append(submission)
    except prawcore.exceptions.BadRequest:
        await ctx.send("ERROR: An exception has occured. Please make sure you've given a correct subreddit id (use the name given in the link; /r/<subreddit>).")
        return
    x = randint(0,49)
    a = a[x]
    e = discord.Embed(title=str(a.title),
                      url=str(a.shortlink),
                      color=discord.Colour.purple())
    if a.url.endswith((".gif",".png",".jpg",".jpeg",".gifv")):
        e.set_image(url=a.url)
        z = ""
    else:
        if a.url.startswith("https://youtu.be"):
            yt = a.url.split(".")
            yt.pop(0)
            yt = yt[0]
            yt = yt.split("/")
            yt.pop(0)
            yt = yt[0]
            e.set_image(url = "http://img.youtube.com/vi/"+yt+"/maxresdefault.jpg")
        if a.url.startswith("https://www.youtube.com"):
            yt = a.url.split("=")
            yt.pop(0)
            yt = yt[0]
            e.set_image(url = "http://img.youtube.com/vi/"+yt+"/maxresdefault.jpg")
        z = "\nContent URL: "+a.url
    e.description="**Score:** "+str(a.score)+"\n**Uploaded by** /u/"+str(a.author)+"\n______________________\n"+str(a.selftext)+z
    print(a.url)
    e.set_footer(text="/r/"+sr)
    await ctx.send(embed = e)
        
        
        
    
bot.run(os.environ['BOT_TOKEN'])
