import discord
from discord.ext import commands
import os
import re
from dotenv.main import dotenv_values

prefix = "."
emojis = []
client = commands.Bot(command_prefix=prefix)

try:
    config = dotenv_values(".env")
    token = config['CYCLES_X_BOT_TOKEN']
except:
    token = os.getenv("CYCLES_X_BOT_TOKEN")

@client.event
async def on_ready() :
    client.change_presence(status = discord.Status.online, activity=discord.Game(name="with feelings..."))
    print("Bot Online.")
    for e in client.emojis:
        emojis.append(str(e))

@client.command()
async def ping(ctx) :
    await ctx.send(f"🏓 Pong with {str(round(client.latency, 2))}")

@client.event
async def on_message(message):
    f = ""
    e = None
    if message.content.startswith(".") and message.content.endswith("."):
        msg = str(message.content)[1:][:-1]
        pat = ":(.*?):"
        for e in client.emojis:
            f = re.search(pat, str(e)).group(1)
            if (f == msg):
                print(f"Found '{f}': {e}")
                break
        else:
            e = None

        await message.delete()
        if e is not None:
            await message.channel.send(e)

@client.command(name="whoami")
async def whoami(ctx) :
    await ctx.send(f"You are {ctx.message.author.name}")

@client.command()
async def clear(ctx, amount=3) :
    await ctx.channel.purge(limit=amount)

client.run(token)

"""
Here are some ideas I have.
1. We should be able to move all our other bot commands (from mee6, dyno), into this app.

2. .challenge command. This allows you to challenge someone to a modelling duel

3. maybe something about XP? Idk

4. automating alot of tasks, (Events, etc) perhaps better social media control.

5. Better roles
"""