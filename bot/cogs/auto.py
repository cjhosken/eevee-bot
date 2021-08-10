from config import *
import discord
from discord.ext import commands

class Automation(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(
        aliases=["torga"]
        )
    
    async def torus(self, ctx):
        embed = discord.Embed(
            title="TORUS", 
            description="Before you ask a question, use TORUS.", 
            color=MAIN_COLOR
            )
        
        embed.set_thumbnail(url="https://i.imgur.com/DSjC4x3.png")
        
        embed.add_field(name= "Think"  , value= "**T**hink! Use your brain! Start by figuring out where your problem is, and think of other ways to acheive what you want."                   , inline=False)
        embed.add_field(name= "Observe", value= "**O**bserve! Check your files, look for hidden objects, go over to see if you missed anything."                                              , inline=False)
        embed.add_field(name= "Restart", value= "**R**estart! Most issues can be solved by restarting or copying everything into a new file."                                                 , inline=False)
        embed.add_field(name= "Update" , value= "**U**pdate! Your system might be out of date. Make sure to check drivers, versions, and any bit of software that might be causing the issue.", inline=False)
        embed.add_field(name= "Search" , value= "**S**earch! Go online, there's a high chance that someone else has had the same problem as you."                                             , inline=False)

        embed.set_footer(text="If you are still unable to find a solution after following these steps, then you should ask in #help.")

        await ctx.reply(embed=embed)

def setup(bot):
    bot.add_cog(Automation(bot))