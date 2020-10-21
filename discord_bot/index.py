import os
import discord

# import utils 
from utils import default
from utils.data import Bot, HelpFormat

# import config and auth token files
config = default.get("config.json")
auth = default.get("auth.json")

print("Logging in...")


bot = Bot(
    command_prefix=config.prefix, prefix=config.prefix, # sets prefix from config
    owner_ids=config.owners, command_attrs=dict(hidden=True), # sets the bot's owners by ID from config
    help_command=HelpFormat(),
    intents=discord.Intents(  # kwargs found at https://discordpy.readthedocs.io/en/latest/api.html?highlight=intents#discord.Intents
        guilds=True, members=True, messages=True, reactions=True
    )
)

# recursively parse through .py files inside cogs folder and load each as an extension
for file in os.listdir("cogs"):
    if file.endswith(".py"):
        name = file[:-3]
        bot.load_extension(f"cogs.{name}")

# Try and start the bot using the auth token passed in from auth.json. If fails, print error.
try:
    bot.run(auth.token)
except Exception as e:
    print(f'Error when logging in: {e}')
