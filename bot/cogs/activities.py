import discord
from config import *
from discord.ext import commands
import random

class Activities(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(
        aliases=['blendball','8b','8ball']
        )
    async def blenderball(self, ctx, *, question : str = None):
        if question is None:
            return await ctx.reply("You need to ask a question!")

        responses = open("./bot/data/blenderball.txt").readlines()

        embed = discord.Embed(
            title="Blender Ball", 
            #color=discord.Color.dark_purple()
            color=SECONDARY_COLOR
            )
        embed.add_field(name="Question", value=question, inline=False)
        embed.add_field(name="Answer", value=random.choice(responses), inline=False)
        embed.set_thumbnail(url="https://i.imgur.com/AY5mwi2.png")

        await ctx.reply(embed=embed)

    @commands.command()
    async def inspire(self, ctx):
        prompt = self.get_prompt()

        embed = discord.Embed(title="Inspiration! 💡", color=discord.Color.gold(), description=prompt)
        embed.set_author(name=ctx.author.display_name, icon_url=ctx.author.avatar.url)
        #await ctx.message.delete()
        await ctx.reply(embed=embed)

    def get_prompt(self):
        prompt = ""
        adj = open("./bot/data/prompts/adjectives.txt").readlines()
        nouns = open("./bot/data/prompts/nouns.txt").readlines()
        verbs = open("./bot/data/prompts/verbs.txt").readlines()

        a1 = random.choice(adj)
        n1 = random.choice(nouns)
        v = random.choice(verbs)
        a2 = random.choice(adj)
        n2 = random.choice(nouns)

        prompt = f"A {a1[:-1]} {n1[:-1]} {v[:-1]} a {a2[:-1]} {n2[:-1]}."

        return prompt


def setup(bot):
    bot.add_cog(Activities(bot))