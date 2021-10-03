import discord
from discord.ext import commands
from config import *
import random
import json

class Activities(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(
        aliases=['blendball','8b','8ball', 'bball', 'bb', 'blenderball']
    )

    async def blenderball(self, ctx, *, question : str = None):
        await ctx.message.delete()

        if question is None:
            return await ctx.send("You need to ask a question!")

        responses = json.load(open("./bot/data/bball.json"))["bball"]

        embed = discord.Embed(
            title="Blender Ball", 
            color=SECONDARY_COLOR
        )

        embed.add_field(name="Question", value=question, inline=False)
        embed.add_field(name="Answer", value=random.choice(responses), inline=False)
        embed.set_thumbnail(url="https://i.imgur.com/AY5mwi2.png")

        await ctx.message.delete()
        await ctx.reply(embed=embed)

    @commands.command()
    async def inspire(self, ctx):
        prompt = self.get_prompt()

        embed = discord.Embed(title="Inspiration! 💡", color=discord.Color.gold(), description=prompt)
        embed.set_author(name=ctx.author.display_name, icon_url=ctx.author.avatar.url)

        await ctx.message.delete()
        await ctx.send(embed=embed)

    def get_prompt(self):
        data = json.load(open("./bot/data/inspires.json"))

        adj = data["adjectives"]
        nouns = data["nouns"]
        verbs = data["verbs"]

        adj1 = random.choice(adj)
        noun1 = random.choice(nouns)
        verb = random.choice(verbs)
        adj2 = random.choice(adj)
        noun2 = random.choice(nouns)

        prompt = f"A {adj1[:-1]} {noun1[:-1]} {verb[:-1]} a {adj2[:-1]} {noun2[:-1]}."

        return prompt

def setup(bot):
    bot.add_cog(Activities(bot))