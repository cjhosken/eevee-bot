import discord
from discord.ext import commands
from config import *

description = BOT_DESCRIPTION
intents = discord.Intents.all()
intents.members = True
intents.presences = True
bot = commands.Bot(
    owner_ids = [363326394987708417],
    command_prefix=commands.when_mentioned_or(DEFAULT_PREFIX),
    intents=discord.Intents.all(),
    case_insensitive=True,
    strip_after_prefix=False,
    allowed_mentions=discord.AllowedMentions.none())

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
        print(f"| loading {cog}...")
        await bot.load_extension(cog)
    print('+--------------------------------------------------+') 
    print('\n')

bot.run(BOT_TOKEN)