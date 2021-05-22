

import discord
from discord.ext import commands
import urllib
import re

class Automation(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print('CYCLES-X: automation loaded')

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

    @commands.command()
    async def youtube(self, ctx, search : str = None):
        if search is None:
            embed = discord.Embed(color=discord.Color.red(), description=f"You need to search something!")
            return await ctx.send(embed=embed)
        else:
            html = urllib.request.urlopen("https://www.youtube.com/results?search_query=" + search)
            vids = re.findall(r"watch\?v=(\S{11})", html.read().decode())
            url = "https://www.youtube.com/watch?v=" + vids[0]
            return await ctx.send(url)
    
    @commands.command()
    @commands.has_any_role('Host')
    async def skillroles(self, ctx):
        advanced = str(discord.utils.get(self.bot.emojis, name="andrew5head"))
        intermediate = str(discord.utils.get(self.bot.emojis, name="andrewnice"))
        beginner = str(discord.utils.get(self.bot.emojis, name="andrewsurprised"))

        embed = discord.Embed(title="Roles: About You", color=discord.Color.blue(), description="React to choose your role.")
        embed.add_field(name="\u200b", value=f"{advanced} : `Advanced`")
        embed.add_field(name="\u200b", value=f"{intermediate} : `Intermediate`")
        embed.add_field(name="\u200b", value=f"{beginner} : `Beginner`")
        await ctx.message.delete()
        await ctx.send(embed=embed)

    @commands.command()
    @commands.has_any_role('Host')
    async def talentroles(self, ctx):
        default = str(discord.utils.get(self.bot.emojis, name="default"))
        bcom = str(discord.utils.get(self.bot.emojis, name="blendercommunity"))

        embed = discord.Embed(title="Roles: About You", color=discord.Color.blue(), description="React to choose your role.")
        embed.add_field(name="\u200b", value=f"{bcom} : `Blenderer`")
        embed.add_field(name="\u200b", value=":art: : `Concept Artist`")
        embed.add_field(name="\u200b", value=":computer: : `Programmer`")
        embed.add_field(name="\u200b", value=":paintbrush: : `2D Artist`")
        embed.add_field(name="\u200b", value=f"{default} : `3D Generalist`")
        embed.add_field(name="\u200b", value=":video_game: : `Game Artist`")
        embed.add_field(name="\u200b", value=":boom: : `VFX Artist`")
        embed.add_field(name="\u200b", value=":man_mage: : `Texture Artist`")
        embed.add_field(name="\u200b", value=":hammer_pick: : `Sculptor`")
        embed.add_field(name="\u200b", value=":doughnut: : `Modeller`")
        embed.add_field(name="\u200b", value=":bone: : `Rigger`")
        embed.add_field(name="\u200b", value=":person_standing: : `Animator`")
        embed.add_field(name="\u200b", value=":clapper: : `Filmmaker`")
        embed.add_field(name="\u200b", value=":musical_keyboard: : `Musician`")
        embed.add_field(name="\u200b", value=":pencil: : `Student`")
        await ctx.message.delete()
        await ctx.send(embed=embed)

    @commands.command()
    @commands.has_any_role('Host')
    async def abilityroles(self, ctx):
        embed = discord.Embed(title="Roles: Server Abilities", color=discord.Color.blue(), description="React to choose your role.")
        embed.add_field(name="\u200b", value=f":innocent: : `Helper`")
        embed.add_field(name="\u200b", value=f":person_fencing: : `Challenger`")
        embed.add_field(name="\u200b", value=f":raised_hand: : `Recieves @everyone`")
        await ctx.message.delete()
        await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(Automation(bot))