import discord
from discord.ext import commands

class Moderation(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=["clear"])
    @commands.has_any_role('Host', 'Moderator')
    async def wipe(self, ctx, amount = 1):
        await ctx.channel.purge(limit = amount + 1)

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

    @commands.command()
    @commands.has_any_role('Host')   
    async def prune(self, ctx):
        print("Pruning...")

        i = 0

        for member in ctx.guild.members:
            if (len(member.roles) < 2):
                i+=1
                await ctx.guild.kick(member)

        print (i, " Members Pruned.")

        await ctx.message.delete()



async def setup(bot):
    await bot.add_cog(Moderation(bot))