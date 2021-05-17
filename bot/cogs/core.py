import discord
from discord.ext import commands
from discord.ext.commands.core import command
class Core(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print("CYCLES-X: Core loaded")
        print("CYCLES-X: Bot online")
        await self.bot.change_presence(status = discord.Status.online, activity = discord.Game(name="Blender"))

    @commands.command()
    async def help(self, ctx):
        activities = """
            `/blenderball` (`question`) to ask the blenderball a question.
            `/inspire` get modelling inspiration!
            `/challenge` challenge another user!
        """
        basic = """
            `/help` list of all avaliable commands.
            `/ping` check bot latency
            `/clear` (`distance`) remove previous messages.
        """

        embed = discord.Embed(title="Help ℹ️", color=discord.Color.blue())
        embed.add_field(name="Activities", value=activities, inline=False)
        embed.add_field(name="Basic", value=basic, inline=False)
        embed.set_author(name=ctx.author.display_name, icon_url=ctx.author.avatar_url)
        await ctx.message.delete()
        await ctx.send(embed=embed)


    @commands.command()
    async def ping(self, ctx):
        await ctx.send(f'Pong! {round(self.bot.latency * 1000)}ms')
        print(f"CYCLES-X: Pinged! {round(self.bot.latency * 1000)}ms")

    @commands.command()
    @commands.has_any_role('Host', 'Moderator')
    async def wipe(self, ctx, amount = 1):
        await ctx.channel.purge(limit = amount + 1)

    # Needs to be implemented
    @commands.command()
    @commands.has_any_role('Host', 'Moderator')
    async def warn(self, ctx, member):
        return
    
    # Needs to be implemented
    @commands.command()
    @commands.has_any_role('Host', 'Moderator')
    async def tempban(self, ctx, member):
        return

    # Needs to be implemented
    @commands.command()
    @commands.has_any_role('Host', 'Moderator')
    async def permban(self, ctx, member):
        return

    # Needs to be implemented
    @commands.command()
    @commands.has_any_role('Host', 'Moderator')
    async def mute(self, ctx, member):
        return
    
    @commands.command()
    @commands.has_any_role('Host', 'Moderator')
    async def slowmode(self, ctx, seconds : int):
        await ctx.channel.edit(slowmode_delay=seconds)

        if (seconds != 0):
            embed = discord.Embed(color=discord.Color.blue(), description=f"Slowmode as been set to a {seconds} second delay.")
        else:
            embed = discord.Embed(color=discord.Color.blue(), description="Slowmode has been disabled.")

        await ctx.message.delete()
        await ctx.send(embed=embed)

    @commands.Cog.listener()
    async def on_member_join(self, member):
        role = discord.utils.get(member.server.roles, id="632745837855899662")
        await self.add_roles(member, role)
        print(f"CYCLES-X: {member} has joined.")

    @commands.Cog.listener()
    async def on_member_remove(member):
        print(f"CYCLES-X: {member} has left.")

def setup(bot):
    bot.add_cog(Core(bot))