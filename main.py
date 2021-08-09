import os
from discord.ext import commands
import discord

from config import *

# Defining the Bot
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
#On_ready Info
@bot.event
async def on_ready():
    print('+--------------------------------------------------+')
    print('|                 Bot has Started                  |')
    print('+--------------------------------------------------+')
    print('| logged in as: {}               |'.format(bot.user))
    print('+--------------------------------------------------+')
    print('| No. of Servers: {}                               |'.format(len(bot.guilds)))
    print('| No. of Users: {}                              |'.format(len(bot.users)))
    print('| Bot Prefix: "{}"                                  |'.format(DEFAULT_PREFIX))
    print('+--------------------------------------------------+')
    print('\n')
    print('+--------------------------------------------------+')
    print('|                     Cogs:                        |')
    print('+--------------------------------------------------+')

    # Loads in the Cogs
    for cog in COGS:
        try:
            bot.load_extension(cog)
            print(f"| {cog} has loaded")
        except Exception as e:
            print(f"| {cog} has not been loaded")
            print(e)
    print('+--------------------------------------------------+') 
    print('\n')    
    print('+--------------------------------------------------+')
    print('|                     servers:                     |')
    print('+--------------------------------------------------+')

    #Gets the Server Names   
    for guild in bot.guilds:
        print(f'| name:{guild.name}\n| guild id:{guild.id}\n| no. of members:{len(guild.members)}\n| Humans: {len(list(filter(lambda m: not m.bot, guild.members)))}\n| Bots: {len(list(filter(lambda m: m.bot, guild.members)))}\n| GuildOwner:{str(guild.owner)}')
        print('+--------------------------------------------------+')   

    print('\n')
# TODO bot.remove_command('help') #Removing the Default Help
# TODO Make a help cmd by subclassing
bot.run(BOT_TOKEN)

#if os.path.exists("./.env"):
#    config = dotenv_values("./.env")
#    token = config['WORKBENCH_BOT_TOKEN']
#else:
#    token = os.getenv('WORKBENCH_BOT_TOKEN')
#
#for file in os.listdir('bot/cogs'):
#    if file.endswith('.py'):
#        bot.load_extension(f'cogs.{file[:-3]}')
#
#bot.run(token)
#
# This is a template for when writing a 'section' of commands. (Eg. Activies, RoleChanging)

#   import discord
#   from discord.ext import commands
#
#   class Template(commands.Cog):
#       def __init__(self, bot):
#           self.bot = bot
#
#       @commands.Cog.listener()
#       async def on_ready(self):
#           print('CYCLES-X: template loaded')
#
#       @commands.command()
#       async def test(self, ctx):
#           await ctx.send("This is a template!")
#
#   def setup(bot):
#       bot.add_cog(Template(bot))
