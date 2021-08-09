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
#        guild_config = await self.bot.get_guild_config(message.guild.id)
#        if not guild_config['nqn']:
#            return
#        for e in self.bot.blacklisted_cache:
#            if message.author.id == e['_id']:
#                return
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
            webhook = discord.utils.get(webhooks, name="EpicBot NQN", user=self.bot.user)
            if webhook is None:
                webhook = await message.channel.create_webhook(name="EpicBot NQN")

            await webhook.send(
                final_msg,
                files=msg_attachments,
                username=message.author.name,
                avatar_url=message.author.avatar.url,
                allowed_mentions=discord.AllowedMentions.none()
            )
#    @commands.Cog.listener()
#    async def on_ready(self):
#        print("WORKBENCH: Emojis loaded")
#    
#    async def getEmote(self, arg):
#        emoji = utils.get(self.bot.emojis, name = arg.strip(":"))
#
#        if emoji is not None:
#            if emoji.animated:
#                add = "a"
#            else:
#                add = ""
#            return f"<{add}:{emoji.name}:{emoji.id}>"
#        else:
#            return None
#
#    async def getInstr(self, content):
#        ret = []
#        spc = content.split(" ")
#        cnt = content.split(":")
#
#        if len(cnt) > 1:
#            for item in spc:
#                if item.count(":") > 1:
#                    wr = ""
#                    if item.startswith("<") and item.endswith(">"):
#                        ret.append(item)
#                    else:
#                        cnt = 0
#                        for i in item:
#                            if cnt == 2:
#                                aaa = wr.replace(" ", "")
#                                ret.append(aaa)
#                                wr = ""
#                                cnt = 0
#                            if i != ":":
#                                wr += i
#                            else:
#                                if wr == "" or cnt == 1:
#                                    wr += " : "
#                                    cnt += 1
#                                else:
#                                    aaa = wr.replace(" ", "")
#                                    ret.append(aaa)
#                                    wr = ":"
#                                    cnt = 1
#                        aaa = wr.replace(" ", "")
#                        ret.append(aaa)
#                else:
#                    ret.append(item)
#        else: 
#            return content
#
#        return ret
#
#    @commands.Cog.listener()
#    async def on_message(self, message):
#        if message.author.bot:
#            return
#
#        if ":" in message.content:
#            msg = await self.getInstr(message.content)
#            ret = " "
#            em = False
#            smth = message.content.split(":")
#            if len(smth) > 1:
#                for word in msg:
#                    if word.startswith(":") and word.endswith(":") and len(word) > 1:
#                        emoji = await self.getEmote(word)
#                        if emoji is not None:
#                            em = True
#                            ret += f" {emoji}"
#                        else:
#                            ret += f" {word}"
#                    else:
#                        ret += f" {word}"
#            else:
#                ret += msg
#            
#            if em:
#                webhooks = await message.channel.webhooks()
#                webhook = utils.get(webhooks, name = "WORKBENCH")
#                if webhook is None:
#                    webhook = await message.channel.create_webhook(name = "WORKBENCH")
#
#                await webhook.send(ret, username= message.author.display_name, avatar_url = message.author.avatar_url)
#                await message.delete()

def setup(bot):
    bot.add_cog(Emoji(bot))