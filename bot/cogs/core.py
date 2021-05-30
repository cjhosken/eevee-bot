import discord
from discord.ext import commands
import json, random, re
class Core(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print("WORKBENCH: Core loaded")
        await self.bot.change_presence(status = discord.Status.online, activity = discord.Game(name="Blender"))
        print("Logged in as")
        print(self.bot.user.name)
        print(self.bot.user.id)
        print("< - - - - - >")

    @commands.command()
    @commands.has_any_role('Host', 'Moderator')
    async def ping(self, ctx):
        print(f"WORKBENCH: Pinged! {round(self.bot.latency * 1000)}ms")
        await ctx.send(f'Pong! {round(self.bot.latency * 1000)}ms')


    @commands.Cog.listener()
    async def on_member_join(self, member):
        print("Member: " + member.name + " has joined.")

        channel = await self.bot.fetch_channel(845932856613142568)

        phrases = open('./bot/data/welcomes.txt').readlines()
        msg = random.choice(phrases)
        msg = re.sub("@", f"{member.mention}", msg)

        await channel.send(msg)


def setup(bot):
    bot.add_cog(Core(bot))