import discord
from discord.ext import commands
from discord import utils

class Emoji(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message: discord.Message):
        if message.author.bot:
            return
        if not message.guild:
            return
        pain = message.content.split(" ")
        final_msg = ""
        for e in pain:
            hmm = e.split(":")
            if len(hmm) < 3:
                final_msg += e + " "
            else:
                i = 1
                interseting = ""
                for h in range(0, len(hmm)):
                    ee = hmm[h]
                    if i % 2 == 0:
                        emoji = discord.utils.get(self.bot.emojis, name=ee)
                        if emoji is not None and (hmm[h + 1][18: 19] != ">"):
                            interseting += str(emoji)
                        else:
                            interseting += ":" + ee + (":" if len(hmm) != i else "")
                    else:
                        interseting += ee
                    i += 1
                final_msg += interseting + " "
        if final_msg not in [message.content, message.content[:-1], message.content + " "]:
            msg_attachments = []
            for attachment in message.attachments:
                uwu = await attachment.to_file()
                msg_attachments.append(uwu)
            await message.delete()
            webhooks = await message.channel.webhooks()
            webhook = discord.utils.get(webhooks, name="WorkBench NQN", user=self.bot.user)
            if webhook is None:
                webhook = await message.channel.create_webhook(name="WorkBench NQN")

            await webhook.send(
                final_msg,
                files=msg_attachments,
                username=message.author.name,
                avatar_url=message.author.avatar.url,
                allowed_mentions=discord.AllowedMentions.none()
            )

def setup(bot):
    bot.add_cog(Emoji(bot))