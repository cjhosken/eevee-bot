import discord
from discord.ext import commands
from discord.ext.commands.core import command
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

    @commands.Cog.listener()
    async def on_member_join(self, member):
        role = discord.utils.get(member.server.roles, id="632745837855899662")
        await self.add_roles(member, role)
        print(f"WORKBENCH: {member} has joined.")

    @commands.Cog.listener()
    async def on_member_remove(member):
        print(f"WORKBENCH: {member} has left.")

def setup(bot):
    bot.add_cog(Core(bot))