import discord
from discord.ext import commands
from discord import utils

class Emoji(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print("CYCLES-X: Emojis loaded")
    
    async def getEmote(self, arg):
        emoji = utils.get(self.bot.emojis, name = arg.strip(":"))

        if emoji is not None:
            if emoji.animated:
                add = "a"
            else:
                add = ""
            return f"<{add}:{emoji.name}:{emoji.id}>"
        else:
            return None

    async def getInstr(self, content):
        ret = []
        spc = content.split(" ")
        cnt = content.split(":")

        if len(cnt) > 1:
            for item in spc:
                if item.count(":") > 1:
                    wr = ""
                    if item.startswith("<") and item.endswith(">"):
                        ret.append(item)
                    else:
                        cnt = 0
                        for i in item:
                            if cnt == 2:
                                aaa = wr.replace(" ", "")
                                ret.append(aaa)
                                wr = ""
                                cnt = 0
                            if i != ":":
                                wr += i
                            else:
                                if wr == "" or cnt == 1:
                                    wr += " : "
                                    cnt += 1
                                else:
                                    aaa = wr.replace(" ", "")
                                    ret.append(aaa)
                                    wr = ":"
                                    cnt = 1
                        aaa = wr.replace(" ", "")
                        ret.append(aaa)
                else:
                    ret.append(item)
        else: 
            return content

        return ret

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author.bot:
            return

        if ":" in message.content:
            msg = await self.getInstr(message.content)
            ret = " "
            em = False
            smth = message.content.split(":")
            if len(smth) > 1:
                for word in msg:
                    if word.startswith(":") and word.endswith(":") and len(word) > 1:
                        emoji = await self.getEmote(word)
                        if emoji is not None:
                            em = True
                            ret += f" {emoji}"
                        else:
                            ret += f" {word}"
                    else:
                        ret += f" {word}"
            else:
                ret += msg
            
            if em:
                webhooks = await message.channel.webhooks()
                webhook = utils.get(webhooks, name = "CYCLES-X")
                if webhook is None:
                    webhook = await message.channel.create_webhook(name = "CYCLES-X")

                await webhook.send(ret, username= message.author.display_name, avatar_url = message.author.avatar_url)
                await message.delete()

def setup(bot):
    bot.add_cog(Emoji(bot))
