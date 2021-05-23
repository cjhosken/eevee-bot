import discord
from discord.ext import commands
import random
import datetime
import json

class Activities(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print("WORKBENCH: Activities loaded")

    @commands.command(aliases=['8ball'])
    async def blenderball(self, ctx, *, question):
        responses = [
            # Yes
            'Yes.',
            'As I see it, yes.',
            'Outlook good.',
            'Signs point to yes.',
            'Most likely.',
            'It is certain.',
            'It is decidedly so.',
            'Without a doubt.',
            'You may rely on it.',
            'Yes definitely.',
            
            # No
            'No.',
            "Don't count on it.",
            "My reply is no.",
            "My sources say no.",
            "Outlook not so good.",
            "Very doubtful.",

            # Non-Comittal
            "Reply hazy, try again.",
            "Ask again later.",
            "Better not tell you now.",
            "Cannot predict now.",
            "Concentrate and ask again."
        ]

        embed = discord.Embed(title="Blender Ball", color=discord.Color.blue())
        embed.add_field(name="Question", value=question, inline=False)
        embed.add_field(name="Answer", value=random.choice(responses), inline=False)
        embed.set_thumbnail(url="https://cdn4.iconfinder.com/data/icons/sports-flat-2/48/Billiard-512.png")

        await ctx.send(embed=embed)

    @commands.command()
    async def inspire(self, ctx):
        prompt = self.get_prompt()

        embed = discord.Embed(title="Inspiration! 💡", color=discord.Color.gold(), description=prompt)
        embed.set_author(name=ctx.author.display_name, icon_url=ctx.author.avatar_url)
        await ctx.message.delete()
        await ctx.send(embed=embed)
        
    def get_prompt(self):
        prompt = ""
        f = open('./bot/data/prompts.json')
        data = json.load(f)

        for p in data['prompts']:
            i = random.randrange(0, len(p['choices']))
            prompt += " " + p['choices'][i]

        return prompt


def setup(bot):
    bot.add_cog(Activities(bot))