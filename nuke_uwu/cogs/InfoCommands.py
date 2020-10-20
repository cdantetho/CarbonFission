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


## -- Sets Global Variables -- ##
consoleDivider = "\n" + "\n" + \
    "|======--------------------------------------------------------------------------------======|" + "\n"
consoleDividerSmall = "\n" + "|==---------------------------==|" + "\n"
# When you reference this in a print function, it will generate one empty line.
consoleNewLine = " "
# When you reference this in a print function, it will generate two empty lines.
consoleSpace = "\n"


class InfoCommands(commands.Cog):
	def __init__(self, bot):
		self.bot = bot


	@commands.Cog.listener()


	## -- HELP -- ##
	# Command: $help #
	@commands.command()
	async def help(self, ctx):
			commandRan = "$help"
			await ctx.send('☫ ———————⫷General Info⫸——————— ☫\nHello, This is the command that gives you info!\n "$" is the default prefix for this bot\n\n ˜”*°• :------------Commands-------------: •°*”˜  \n╔ $kick [@user] - Kicks the user pinged from the server\n╠ $kickAll - Kicks all users from the server\n╠ $ban [@user] - Bans the user pinged from the server\n╠ $banAll - Bans all members from the server\n╠ $rename [@user] - Renames the user pinged from the server\n╠ $renameAll - Renames all users in the server\n╠ $dm [@user] - DMs the user pinged\n╠ $dmAll - DMs all members in the server\n╠ $spam [Amount] [Message] - Spams that message in the channel the command is run in\n╠ $rolespam [Amount] [Role Name] - Spam creates roles with the name that is provided\n╠ $channelspam [Amount] [Channel Name] - Spam creates channels with the name that is provided\n╠ $listAll [Condition] - Lists all of the thing that is asked for\n╠ Conditions for list all: Roles, Channels, Emojis, All\n╠ $deleteAll [Condition] - Deletes all of the thing that is asked for\n╠ Conditions for delete all: Roles, Channels, Emojis\n╚ $destroy - Deletes Everything in the server, Literally everything lmaooo\n')
			# Command Info #
			print (consoleDivider)
			print (f"Details:")
			print (f" Executed command  -  {commandRan}")
			print (f" Server command was executed in  -  {ctx.guild.name}")
			print (consoleDivider)


def setup(bot):
	bot.add_cog(InfoCommands(bot))
	print('InfoCommands Have Been Loaded!')
