import discord
from discord.ext import commands
import json, random, re
class Core(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    #@commands.has_any_role('Host', 'Moderator')
    async def ping(self, ctx):
        print(f"WORKBENCH: Pinged! {round(self.bot.latency * 1000)}ms")
        await ctx.reply(f'Pong! {round(self.bot.latency * 1000)}ms')

    @commands.Cog.listener()
    async def on_member_join(self, member):
        print(f"WORKBENCH: {member} has joined.")

        phrases = open('./bot/data/welcomes.txt').readlines()
        msg = random.choice(phrases)
        msg = re.sub("@", f"{member.mention}", msg)

        #await self.bot.get_channel(845932856613142568).send(msg)

def setup(bot):
    bot.add_cog(Core(bot))