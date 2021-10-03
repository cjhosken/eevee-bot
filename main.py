import os
import discord
from discord.ext import commands
from config import *

description = BOT_DESCRIPTION
intents = discord.Intents.all()
intents.members = True
intents.presences = True
bot = commands.Bot(
    owner_ids = [363326394987708417,530395525179244557],
    command_prefix=commands.when_mentioned_or(DEFAULT_PREFIX),
    intents=discord.Intents.all(),
    case_insensitive=True,
    strip_after_prefix=False,
    allowed_mentions=discord.AllowedMentions.none())

os.environ.setdefault("JISHAKU_HIDE", "1")
bot.load_extension('jishaku') # pip install -U jishaku

@bot.event
async def on_ready():
    print('+--------------------------------------------------+')
    print('|                 Bot has Started                  |')
    print('+--------------------------------------------------+')
    print('| logged in as: {}               |'.format(bot.user))
    print('+--------------------------------------------------+')
    print('| No. of Users: {}                              |'.format(len(bot.users)))
    print('| Bot Prefix: "{}"                                  |'.format(DEFAULT_PREFIX))
    print('+--------------------------------------------------+')
    print('|                     Cogs:                        |')
    print('+--------------------------------------------------+')

    for cog in COGS:
        try:
            bot.load_extension(cog)
            print(f"| {cog} was loaded")
        except Exception as e:
            print(f"| {cog} was not loaded")
            print(e)
    print('+--------------------------------------------------+') 
    print('\n')

# TODO bot.remove_command('help') #Removing the Default Help
# TODO Make a help cmd by subclassing

bot.run(BOT_TOKEN)