import discord
from discord.ext import commands
import random
import re

class Activities(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print('Activities loaded')

    @commands.command(aliases=['8ball'])
    async def blenderball(self, ctx, *, question):
        responses = [
            'The Blender Gods agree.',
            'Yes.',
            'You will find your answer in the shader editor.',
        ]

        embed = discord.Embed(title="Blender Ball", color=discord.Color.blue())
        embed.add_field(name="Question", value=question, inline=False)
        embed.add_field(name="Answer", value=random.choice(responses), inline=False)

        await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(Activities(bot))