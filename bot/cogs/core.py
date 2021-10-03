import discord
from discord.ext import commands
import json
import random
import re
class Core(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_member_join(self, member):
        print(f"EEVEE: {member} has joined.")

        phrases = json.load(open('./bot/data/welcomes.json'))["welcomes"]
        msg = random.choice(phrases)
        msg = re.sub("@", f"{member.mention}", msg)

        #await self.bot.get_channel(845932856613142568).send(msg)

def setup(bot):
    bot.add_cog(Core(bot))