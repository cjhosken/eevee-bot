

import discord
from discord.ext import commands
import urllib
import re

class Automation(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print('WORKBENCH: automation loaded')

    @commands.command(aliases=["torga"])
    async def torus(self, ctx):
        embed = discord.Embed(title="TORUS", description="Before you ask a question, use TORUS.", color=discord.Color.orange())
        embed.set_thumbnail(url="https://i.imgur.com/DSjC4x3.png")
        embed.add_field(name="Think", value="Think! Use your brain! Start by figuring out where your problem is, and think of other ways to acheive what you want.", inline=False)

        embed.add_field(name="Observe", value="Observe! Check your files, look for hidden objects, go over to see if you missed anything.", inline=False)

        embed.add_field(name="Restart", value="Restart! Most issues can be solved by restarting or copying everything into a new file.", inline=False)

        embed.add_field(name="Update", value="Update! Your system might be out of date. Make sure to check drivers, versions, and any bit of software that might be causing the issue.", inline=False)

        embed.add_field(name="Search", value="Search! Go online, there's a high chance that someone else has had the same problem as you.", inline=False)

        embed.set_footer(text="If you are still unable to find a solution after following these steps, then you can ask in #help.")

        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(Automation(bot))