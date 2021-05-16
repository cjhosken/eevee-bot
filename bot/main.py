import discord
from discord.ext import commands
import os
from dotenv import load_dotenv
from dotenv.main import dotenv_values

client = commands.Bot(command_prefix=".")
config = dotenv_values(".env")
token = config['CYCLES_X_BOT_TOKEN']

@client.event
async def on_ready() :
    await client.change_presence(status = discord.Status.idle, activity = discord.Game("Currently in development."))
    print("I am online")

@client.command()
async def ping(ctx) :
    await ctx.send(f"🏓 Pong with {str(round(client.latency, 2))}")

@client.command(name="whoami")
async def whoami(ctx) :
    await ctx.send(f"You are {ctx.message.author.name}")

@client.command()
async def clear(ctx, amount=3) :
    await ctx.channel.purge(limit=amount)

client.run(token)