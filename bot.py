import discord
import os
from random import randint
import time
from discord.ext import commands
import asyncio
import praw

reddit = praw.Reddit(client_id=os.environ['REDDIT_ID'],
                     client_secret=os.environ['REDDIT_SECRET'],
                     user_agent="aesthbot-discordbot[python] v1.0.2 (by /u/thehellbell)")

if reddit.read_only:
    print("The Reddit instance is in READ ONLY mode.")
else:
    print("The Reddit instance is in AUTHORIZED mode.")

bot = discord.Client()
owners = [264195450859552779, 403557634998796288]

@bot.event
async def on_ready():
    print('Logged in as {0.user}'.format(bot))
    print("Created by HBell_CL.py#5144 and Alexei Стуков#1672")
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
    
@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    if message.content.startswith('~botinfo'):
        e = discord.Embed(title="**BOT INFO**",
description="""**Owners:** HBell_CL.py#5144 and Alexei Стуков#1672 =^.^=
[<:furryfren2:463616355900588062>][<:lopez:456587657837936642>]
**The bot was created** at """+str(bot.user.created_at)+"""~
**The bot is present** in """+str(len(bot.guilds))+" server(s)~")
        
        e.set_thumbnail(url=bot.user.avatar_url)
        e.set_footer(text="La weá weón fsdfdslkñsfls.")
        await message.channel.send(embed=e)

    if message.content.startswith('~servinfo'):
        if len(message.content) > 10 and message.author.id in owners:
            msg = message.content.split(' ')
            msg.pop(0)
            if len(msg) > 1:
                msg = msg[0]
            msg = " ".join(msg)
            try:
                msg = int(msg)
            except ValueError:
                await message.channel.send("Please input a valid ID")
                return
            g = bot.get_guild(msg)
            if g == None:
                await message.channel.send("This server either doesn't exist, or I'm not present in it.")
                return
        else:
            g = message.guild
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
    
    if message.content.startswith('~ping'):
        i = randint(1,5)
        if i == 1:
            await message.channel.send("It's time to chew gum and kick ass... | "+str(round(bot.latency, 5))+"s")
        if i == 2:
            await message.channel.send("Pong~ | "+str(round(bot.latency, 5))+"s")
        if i == 3:
            await message.channel.send("A ping is a ping, you can't say it's only a half. | "+str(round(bot.latency, 5))+"s")
        if i == 4:
            await message.channel.send("Beep boop~ | "+str(round(bot.latency, 5))+"s")
        if i == 5:
            await message.channel.send("In case of doubt, shout Bell out! | "+str(round(bot.latency, 5))+"s")

    if message.content.startswith('~night'):
        if message.author.id in owners:
            print("SHUTDOWN STARTING...")
            t = await message.channel.send('Restarting... ')
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
            await message.channel.send("ERROR: Owner-only command.")

    if message.content.startswith('~aesth'):
        sample = """El veloz murciélago hindú comía feliz cardillo y kiwi. La cigüeña tocaba el saxofón detrás del palenque de paja.
The quick brown fox jumps over the lazy dog."""
        msg = message.content.split(' ')
        msg.pop(0)
        msg = " ".join(msg)
        tab =  "　ＡＢＣＤＥＦＧＨＩＪＫＬＭＮＯＰＱＲＳＴＵＶＷＸＹＺａｂｃｄｅｆｇｈｉｊｋｌｍｎｏｐｑｒｓｔｕｖｗｘｙｚ１２３４５６７８９０！＂＃＄％＆／（）＝＇＼？＋＊［｛＾］｝｀，；．：－＿＜＞"
        tab2 = " ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890!"+'"'+"#$%&/()='"+'\\'+'?+*[{^]}`,;.:-_<>'
        tran = str.maketrans(tab2, tab)
        if len(message.content) > 7:
            await message.channel.send(msg.translate(tran))
        else:
            await message.channel.send(sample.translate(tran))

    if message.content.startswith('~echo'):
        msg = message.content.split(' ')
        msg.pop(0)
        msg = " ".join(msg)
        if len(message.content) > 6:
            await message.channel.send(msg)
            await message.delete()
        else:
            await message.channel.send("Please, input the message to echo.")

    if message.content.startswith('~aesnick'):
        tab =  "　ＡＢＣＤＥＦＧＨＩＪＫＬＭＮＯＰＱＲＳＴＵＶＷＸＹＺａｂｃｄｅｆｇｈｉｊｋｌｍｎｏｐｑｒｓｔｕｖｗｘｙｚ１２３４５６７８９０！＂＃＄％＆／（）＝＇＼？＋＊［｛＾］｝｀，；．：－＿＜＞"
        tab2 = " ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890!"+'"'+"#$%&/()='"+'\\'+'?+*[{^]}`,;.:-_<>'
        tran = str.maketrans(tab2, tab)
        t = message.author.nick
        if t is None:
            t = message.author.name
        try:
            await message.author.edit(nick = t.translate(tran))
            print("ACTION: Changed nickname of user {0}: '{1}' to '{2}'.".format(message.author, t, t.translate(tran)))
        except discord.errors.Forbidden:
            await message.channel.send("ERROR: My privilege is too low...")

    if message.content.startswith('~gameset'):
        if message.author.id in owners:
            msg = message.content.split(' ')
            msg.pop(0)
            msg = " ".join(msg)
            if len(message.content) > 9:
                await bot.change_presence(activity=discord.Game(msg))
                print("ACTION: Status set to: 'Playing "+msg+"'")
                await message.channel.send("*Playing status* set to: '"+msg+"'")
            else:
                await message.channel.send("Please give an input.")
        else:
            await message.channel.send("ERROR: Owner-only command.")

    if message.content.startswith('~usern'):    
        if message.author.id in owners:
            msg = message.content.split(' ')
            msg.pop(0)
            msg = " ".join(msg)
            if len(message.content) > 7:
                await bot.user.edit(username=msg)
                print("ACTION: Changed username to '{}'.".format(msg))
                await message.channel.send("Changed username to '{}'.".format(msg))
            else:
                await message.channel.send("Please input an username.")
        else:
            await message.channel.send("ERROR: Owner-only command.")
            
    if message.content.startswith('~massping'):
        a = message.author
        perms = message.author.permissions_in(message.channel)
        if perms.administrator or m == "<@!"+a.id+">":
            for i in range(5):
                for user in message.mentions:
                    message = await message.channel.send(str(user.mention))
                if i < 4:
                    await message.delete()
    
    if message.content.startswith('~userinfo'):
        error1 = "Please input a valid ID/mention."
        if len(message.mentions) < 2:
            if len(message.mentions) == 1:
                author = message.mentions[0]
                j = True
            else:
                if len(message.content) > 10:
                    msg = message.content.split(' ')
                    msg.pop(0)
                    if len(msg) > 1:
                        msg = msg[0]
                    msg = "".join(msg)
                    try:
                        msg = int(msg)
                    except ValueError:
                        await message.channel.send(error1)
                        return
                    author = message.guild.get_member(msg)
                    j = True
                    if author == None:
                        author = await bot.get_user_info(msg)
                        j = False
                else:
                    author = message.author
                    j = True
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
                embed.set_footer(text="Command requested by "+str(message.author)+".")
                await message.channel.send("#############################")
                await message.channel.send(embed=embed)
                await message.channel.send("#############################")
                print(author)
            except AttributeError:
                message.channel.send("The inputted user is invalid.")
        else:
            await message.channel.send("Ping less than 2 people only!")
                        
    if "<@455225304991137792>" in message.content:
        await message.channel.send("I'm ready!")

    if message.content.startswith("~servers"):
        if message.author.id in owners:
            c = 1
            for server in bot.guilds:
                await message.channel.send(str(c)+".-) "+str(server.name)+"; ID = "+str(server.id)+"~")
                c += 1
    
    if message.content.startswith("~reddit"):
        sr = ['vaporwaveart','vaporwaveaesthetics']
        y = randint(0,1)
        a = []
        for submission in reddit.subreddit(sr[y]).hot(limit=50):
            a.append(submission)
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
                print(yt)
                yt.pop(0)
                print(yt)
                yt = yt[0]
                print(yt)
                yt = yt.split("/")
                print(yt)
                yt.pop(0)
                print(yt)
                yt = yt[0]
                print(yt)
                e.set_image(url = "http://img.youtube.com/vi/"+yt+"/maxresdefault.jpg")
            z = "\nContent URL: "+a.url
        e.description="**Score:** "+str(a.score)+"\n**Uploaded by** /u/"+str(a.author)+"\n______________________\n"+str(a.selftext)+z
        print(a.url)
        e.set_footer(text="/r/"+sr[y])
        await message.channel.send(embed = e)
    
    if message.content.startswith("~help"):
        e = discord.Embed(title="HELP WITH COMMANDS",description="""**<> encompasses obligatory arguments. () encompasses optional arguments.**
**~botinfo** => Sends information about this bot.
**~userinfo** *(id or mention)* => Sends information about a certain user; the author of the message if not specified.
**~servinfo** *(id)* => Sends information about the server where the command was sent.
**~ping** => For testing bot latency.
**~aesth** *(text)* => Turns given text (from the english alphabet, that is) into a simple aesthetic font. If no text is present, it shows two sample pangrams.
**~echo** *<text>* => Repeats text given by the user.
**~aesnick** => Turns any normal font part (from the english alphabet, that is) from your name to a simple aesthetic font and turns it into your nickname. The bot must have a higher role than you for it to work, and manage nicknames permissions too!
**~reddit** => Takes a random post from the hot section of either /r/vaporwaveart or /r/vaporwaveaesthetics.
**=======BOT OWNER ONLY COMMANDS=======**
**~night** => Shuts down the bot.
**~gameset** *<text>* => Sets the playing status of the bot.
**~usern** *<text>* => Sets the username of the bot.
**~servers** => Lists all the servers the bot is present in.""",
                          color=discord.Colour(0xff0204))
        await message.channel.send(embed=e)








        
bot.run(os.environ['BOT_TOKEN'])
