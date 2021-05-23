import discord
from discord.ext import commands
import json, random
class Core(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print("WORKBENCH: Core loaded")
        print("WORKBENCH: Bot online")
        await self.bot.change_presence(status = discord.Status.online, activity = discord.Game(name="Blender"))

    @commands.command()
    async def ping(self, ctx):
        await ctx.send(f'Pong! {round(self.bot.latency * 1000)}ms')
        print(f"WORKBENCH: Pinged! {round(self.bot.latency * 1000)}ms")

    @commands.command()
    async def help(self, ctx, label : str = None):
        if label != "workbench":
            return

    @commands.Cog.listener()
    async def on_member_join(self, member):
        channel = self.bot.get_channel(845932856613142568)
        role = discord.utils.get(member.server.roles, id="632745837855899662")

        f = open('./bot/data/welcome.json')
        data = json.load(f)

        msg = data["welcomes"][random.randrange(0, len(data["welcomes"]))]

        await self.add_roles(member, role)
        await channel.send(msg)
        print(f"WORKBENCH: {member} has joined.")

    @commands.Cog.listener()
    async def on_member_remove(member):
        print(f"WORKBENCH: {member} has left.")

def setup(bot):
    bot.add_cog(Core(bot))