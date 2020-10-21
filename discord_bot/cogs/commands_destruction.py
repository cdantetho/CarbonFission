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


class Commands_destruction(commands.Cog):
	def __init__ (self, bot):
		self.bot = bot

		@commands.Cog.listener()




def setup(bot):
	bot.add_cog(Commands_destruction(bot))
	print('Commands_destruction Have Been Loaded!')

