from cogs.activities import Activities
import discord
from discord.ext import commands
import random
import re

class Core(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print('Basic loaded')
        print("Bot Online.")
        await self.bot.change_presence(status = discord.Status.online, activity=discord.Game(name="with feelings..."))

    @commands.command()
    async def ping(self, ctx):
        await ctx.send(f'Pong! {round(self.bot.latency * 1000)}ms')

    @commands.command()
    async def clear(self, ctx, amount=1):
        await ctx.channel.purge(limit=amount)

    @commands.Cog.listener()
    async def on_member_join(member):
        print(f'{member} has joined.')

    @commands.Cog.listener()
    async def on_member_remove(member):
        print(f'{member} has joined.')

def setup(bot):
    bot.add_cog(Core(bot))