import discord
from discord.ext import commands
import json, random, re
class Core(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    @commands.Cog.listener()
    async def on_ready(self):
        print("WORKBENCH: Core loaded")
        print("WORKBENCH: Bot online")
        await self.bot.change_presence(status = discord.Status.online, activity = discord.Game(name="Blender"))

    @commands.command()
    @commands.has_any_role('Host', 'Moderator')
    async def ping(self, ctx):
        print(f"WORKBENCH: Pinged! {round(self.bot.latency * 1000)}ms")
        await ctx.send(f'Pong! {round(self.bot.latency * 1000)}ms')


    @commands.Cog.listener()
    async def on_member_join(self, member):
        channel = await self.bot.fetch_channel("845932856613142568")

        phrases = open('./bot/data/welcomes.txt').readlines()
        msg = random.choice(phrases)
        l = msg.split("%")
        for w in l:
            if w == "*":
                w == f"@{member.name}"

        msg = w.join()

        embed = discord.Embed(color=discord.Color.blue(), description=msg)

        await channel.send(embed=embed)


def setup(bot):
    bot.add_cog(Core(bot))