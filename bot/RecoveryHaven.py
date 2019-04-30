import configparser
import os
import shutil
import subprocess
import sys
import asyncio
import discord
from discord import Member
import datetime
import time
from discord.ext import commands
from discord.ext.commands import has_permissions
from discord.ext.commands import Bot

bot = commands.Bot(command_prefix = ';', description = 'Created by Datsun280zx')
client = bot
botId = None


@bot.event
async def on_ready():
    print('Logged in as\n{}\nhttps://discordapp.com/oauth2/authorize?&client_id={}&scope=bot&permissions=8\n------\nMain loading proccess 25%\n Mute script loaded\n Main bot loading process 60%\n Welcome script loaded!\nMain bot loading process is now complete!\n----------'.format(bot.user.name, bot.user.id))

@bot.event
async def on_member_join(member):
    channel = member.server.get_channel("Welcome")
    role = discord.utils.get(member.server.roles,name="Members")
    fmt = 'Welcome to the {1.name} offical Discord, {0.mention}, please read the rules and enjoy your stay.'
    await bot.send_message(channel, fmt.format(member, member.server))
    await bot.add_roles(member, role)

@bot.event
async def on_member_remove(member):
    channel = member.server.get_channel("Welcome")
    fmt = '{} has left/been kicked from the server.'
    await bot.send_message(channel, fmt.format(member, member.server))

@bot.command(pass_context=True)
async def agree(ctx):
    await bot.delete_message(ctx.message)
    role = discord.utils.get(ctx.message.server.roles, name='Verified Members')
    await bot.add_roles(ctx.message.author, role)
    await bot.send_message(ctx.message.author, "You are are now verfied.\nThis means you have agreed to our terms of service.\nPlease follow respect our terms of service or you will be unverfied!\nJust make this easy on the both of us. \n If you forget our Terms of Service here they are: ```Copyright Disclaimer Under Section 107 of the Copyright Act 1976, allowance is made for fair use for purposes such as criticism, comment, news reporting, teaching, scholarship, and research. Fair use is a use permitted by copyright statute that might otherwise be infringing. Non-profit, EDUCATIONAL or personal use tips the balance in favor of fair use.```\n\n```DO NOT GO ON A SPENDING SPREE\n\nDO NOT SPEND LARGE CASH AMOUNTS IN A SINGLE SESSION\n\nDO NOT TRANSFER MONEY TO OTHER LOCATIONS```\n\n```Any thing with in 24 hours is my fault Anything outside of 24 hours is your fault if for some reason you played legit with in 24 you get banned then I will agree to give a temporary account for you to play on as well redo the recovery at a later time```")
   



    
                        ##############
                        # Moderation #
                        ##############
                        
@bot.command(name="kick", pass_context=True)
async def kick(ctx, member: Member):
    if ctx.message.author.server_permissions.administrator:
        await bot.kick(member)
        embed=discord.Embed(title="User kicked!", description="**{0}** was kicked by **{1}**!".format(member, ctx.message.author), color=0xff00f6)
        await bot.delete_message(ctx.message)
        await bot.say(embed=embed)
    else:
        embed=discord.Embed(title="Permission Denied.", description="You don't have permission to use this command.", color=0xff00f6)
        await bot.say(embed=embed)


@bot.command(pass_context = True)
async def mute(ctx, member: discord.Member):
     if ctx.message.author.server_permissions.administrator or ctx.message.author.id == '194151340090327041':
        role = discord.utils.get(member.server.roles, name='Muted')
        await bot.add_roles(member, role)
        embed=discord.Embed(title="User Muted!", description="**{0}** was muted by **{1}**!".format(member, ctx.message.author), color=0xff00f6)
        await bot.say(embed=embed)
     else:
        embed=discord.Embed(title="Permission Denied.", description="You don't have permission to use this command.", color=0xff00f6)
        await bot.say(embed=embed)

@bot.command(pass_context = True)
async def unmute(ctx, member: discord.Member):
     if ctx.message.author.server_permissions.administrator or ctx.message.author.id == '194151340090327041':
        role = discord.utils.get(member.server.roles, name='Muted')
        await bot.remove_roles(member, role)
        embed=discord.Embed(title="User unmuted!", description="**{0}** was unmuted by **{1}**!".format(member, ctx.message.author), color=0xff00f6)
        await bot.say(embed=embed)
     else:
        embed=discord.Embed(title="Permission Denied.", description="You don't have permission to use this command.", color=0xff00f6)
        await bot.say(embed=embed)


@bot.command(pass_context = True, description="This command clears messages for an X amount of messages")
async def clear(ctx, amount = 10000):
    if ctx.message.author.server_permissions.administrator:
        channel = ctx.message.channel
        messages = []
        async for message in bot.logs_from(channel, limit=int(amount) + 1):
            messages.append(message)
        await bot.delete_messages(messages)
    else:
        embed=discord.Embed(title="Permission Denied.", description="You don't have permission to use this command.", color=0xff00f6)
        await bot.say(embed=embed)  

                        ##############
                        ## About Us ##
                        ##############
        
@bot.command(pass_context = True)
async def aboutus(ctx):
    embed = discord.Embed(color = 0xC300FF, title = "About Recovery Haven, Who are we?")
    embed.description = "\n Hi! We're Recovery Haven. Recovery Haven is a __**Grand Theft Auto V**__ modding company but this is just now. Recovery Haven strives to be the very best in customer service and quality with the services we have to make your overall stay a fantastic experience."
    await bot.say(embed = embed)
    await bot.delete_message(ctx.message)
    return
                        ##############
                        ## Services ##
                        ##############

@bot.command(pass_context = True)
async def drop(ctx):
    embed = discord.Embed(color = 0xC300FF, title = "Money Drops")
    embed.description = "Money Drops are free I will ping this channel if I am doing a drop"
    await bot.say(embed = embed)
    await bot.delete_message(ctx.message)
    return

@bot.command(pass_context = True)
async def bad(ctx):
    embed = discord.Embed(color = 0xC300FF, title = "Bad sport")
    embed.description = "Found your self in a bad sport lobby? \n\n For 3$ we can remove that for you!"
    await bot.say(embed = embed)
    await bot.delete_message(ctx.message)
    return


@bot.command(pass_context = True)
async def service(ctx):
    embed = discord.Embed(color = 0x2AFF00, title = "Pay for a service", description = "So you want me to mod your account but dont know how it works \n\n **Heres how it works** \n\n ► First add me on Discord! \n ✦ Datsun280zx#9766 \n ►  Then send me a message regarding you wanting a modded account, then the paypal will be sent to you\n\t► Service starts after we've received the money\n\t► Only PayPal Payments are accepted!\n\t► When we've received the money we need your account login for Steam or Social Club if you bought it on Social Club!\n\n **Our prices**\n\n**Power**\n►$5 USD\n\t\t✦ 500 Million \n\t\t✦ Lvl +0\n\n**Starter**\n►$6 USD\n\t\t✦ 150 Million \n\t\t✦ LvL + 80\n\n**Basic**\n►$7 USD\n\t\t✦ 400 Million \n\t\t✦ LvL + 120\n\n**Regular**\n►$8 USD\n\t\t✦ 600 Million \n\t\t✦ LvL + 140\n\n**Classic**\n►$9 USD\n\t\t✦ 800 Million \n\t\t✦ LvL + 160\n\n**Premium**\n►$10 USD\n\t\t✦ 800 Million\n\t\t✦ Lvl + 180\n\t\t✦ UNLOCKED\n\n**Elite**\n$20 USD\n\t\t✦ 1 Billion\n\t\t✦ Lvl + 200\n\t\t✦ UNLOCKED\n\t\t✦ BAN PROTECTION\n\n\n **About Ban protection**\n So you got banned from my recovery? Well fear not! I will give you a donor account to use while you are banned and when you get unabnned you will get the same recovery for free! There chances of you getting banned are very low but it could happen! Although I shutdown the store if something happens like a banwave something could sneak up on me that I dont realize, which is why I'm now offering a ban protection!")
    await bot.say(embed = embed)
    await bot.delete_message(ctx.message)
    return



                        ##############
                        ####  FAQ  ###
                        ##############
@bot.command(pass_context = True)
async def faq(ctx):
    embed = discord.Embed(color = 0x2AFF00, title = "Frequently asked questions", description = "Will I get banned?\nNo, Our menus are paid for, and undetected\n\nIs it legit?\nYes It is! Ask people with yellow names, or check  <#547157681513824276>.\n\nWhy Revoery Haven?\nWe're very active, so much cheaper than the competition!\n\nHow do I buy?\nIt's easy! Simply message <@233046326898720769> and I will get back to you as soon as I can!")
    await bot.say(embed = embed)
    await bot.delete_message(ctx.message)
    return


bot.run("NTM1MTk1NzM2NzkxNTgwNjgz.XMFBBQ.H2AE8Pp8AL1GYtNcLNg2T5MQ2Pc")
