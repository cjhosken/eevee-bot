import asyncio

import discord
from discord.ext.commands.errors import CommandNotFound, MissingRequiredArgument
import youtube_dl
import os
import urllib
import re

from discord.ext import commands

# Suppress noise about console usage from errors
youtube_dl.utils.bug_reports_message = lambda: ''

ytdl_format_options = {
    'format': 'bestaudio/best',
    'outtmpl': os.path.join('./bot/data/music', '%(title)s.%(ext)s'),
    'restrictfilenames': True,
    'noplaylist': True,
    'nocheckcertificate': True,
    'ignoreerrors': False,
    'logtostderr': False,
    'quiet': True,
    'no_warnings': True,
    'default_search': 'auto',
    'source_address': '0.0.0.0'
}

ffmpeg_options = {
    'options': '-vn'
}

ytdl = youtube_dl.YoutubeDL(ytdl_format_options)

class YTDLSource(discord.PCMVolumeTransformer):
    def __init__(self, source, *, data, volume=0.5):
        super().__init__(source, volume)

        self.data = data

        self.title = data.get('title')
        self.url = data.get('url')

    @classmethod
    async def from_url(cls, url, *, loop=None, stream=False):
        loop = loop or asyncio.get_event_loop()
        data = await loop.run_in_executor(None, lambda: ytdl.extract_info(url, download=not stream))

        if 'entries' in data:
            # take first item from a playlist
            data = data['entries'][0]

        filename = data['url'] if stream else ytdl.prepare_filename(data)
        return cls(discord.FFmpegPCMAudio(filename, **ffmpeg_options), data=data)

class Music(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.queue = {}
        self.queueSize = 0
        self.queueUser = {}
        self.qID = 0
        self.loopQ = 0

    @commands.command()
    async def _join(self, ctx, channel : discord.VoiceChannel = None):
        await ctx.message.add_reaction('👋')
        self.queue = {}

        if ctx.author.voice is None:
            embed = discord.Embed(color=discord.Color.red(), description=f"Please join a voice channel to use that command!")
            return await ctx.send(embed=embed)  
        
        if channel is None:
            channel = discord.utils.get(ctx.guild.voice_channels, name=str(ctx.author.voice.channel))

        return await channel.connect()

    
    @commands.command()
    async def _play(self, ctx, *, url=None, search=None):
        if ctx.author.voice is None:
            embed = discord.Embed(color=discord.Color.red(), description=f"Please join a voice channel to use that command!")
            return await ctx.send(embed=embed)
        
        if discord.utils.get(self.bot.voice_clients, guild=ctx.guild) is None:
            channel = discord.utils.get(ctx.guild.voice_channels, name=str(ctx.author.voice.channel))
            await channel.connect()

        if url is None:
            if search is None:
                embed = discord.Embed(color=discord.Color.red(), description=f"You need to specify a song!")
                return await ctx.send(embed=embed)
            else:
                html = urllib.request.urlopen("https://www.youtube.com/results?search_query=" + search)
                vids = re.findall(r"watch\?v=(\S{11})", html.read().decode())
                url = "https://www.youtube.com/watch?v=" + vids[0]

        player = await YTDLSource.from_url(url, loop=self.bot.loop)

        if len(self.queue) == 0:
            self.queue[0] = player
            self.queueUser[0] = ctx.message.author
            self.queueSize += 1
            await self.playQueue(ctx)
        else:
            self.queueUser[len(self.queue)] = ctx.message.author
            self.queue[len(self.queue)] = player
            self.queueSize += 1

    
    @commands.command()
    async def _pause(self, ctx):
        await ctx.message.add_reaction('⏸')
        voice = discord.utils.get(self.bot.voice_clients, guild=ctx.guild)
        if voice.is_playing():
            voice.pause()
        else:
            embed = discord.Embed(color=discord.Color.red(), description=f"No audio is playing!")
            await ctx.send(embed=embed)
    
    @commands.command()
    async def _resume(self, ctx): 
        await ctx.message.add_reaction('▶')
        voice = discord.utils.get(self.bot.voice_clients, guild=ctx.guild)
        if voice.is_paused():
            voice.resume()
        else:
            embed = discord.Embed(color=discord.Color.red(), description=f"The audio is not paused!")
            await ctx.send(embed=embed)

    @commands.command()
    async def _stop(self, ctx):
        await ctx.message.add_reaction("🚫")

        if ctx.author.voice is None:
            embed = discord.Embed(color=discord.Color.red(), description=f"Please join a voice channel to use that command!")
            return await ctx.send(embed=embed)  

        voice = discord.utils.get(self.bot.voice_clients, guild=ctx.guild)
        await voice.stop()

    @commands.command()
    async def _leave(self, ctx):
        await ctx.message.add_reaction('👌')

        if ctx.author.voice is None:
            embed = discord.Embed(color=discord.Color.red(), description=f"Please join a voice channel to use that command!")
            return await ctx.send(embed=embed)  

        voice = discord.utils.get(self.bot.voice_clients, guild=ctx.guild)

        if voice is None or not voice.is_connected():
            embed = discord.Embed(color=discord.Color.red(), description=f"I'm not connected to your voice channel!")
            await ctx.send(embed=embed)

        else:
            await ctx.voice_client.disconnect()
        
        self.cache()

    @commands.command()
    async def _sound(self, ctx, *, query):
        await ctx.message.add_reaction('🎶')
        
        if ctx.author.voice is None:
            embed = discord.Embed(color=discord.Color.red(), description=f"Please join a voice channel to use that command!")
            return await ctx.send(embed=embed)  

        source = discord.PCMVolumeTransformer(discord.FFmpegPCMAudio(query))
        ctx.voice_client.play(source, after=lambda e: print(f'Player error: {e}') if e else None)
        await ctx.send(f'Now playing: {query}')

    @commands.command()
    async def _volume(self, ctx, volume: int):
        await ctx.message.add_reaction('🔈')

        if ctx.author.voice is None:
            embed = discord.Embed(color=discord.Color.red(), description=f"Please join a voice channel to use that command!")
            return await ctx.send(embed=embed)  

        if ctx.voice_client is None:
            embed = discord.Embed(color=discord.Color.red(), description=f"I'm not connected to your voice channel!")
            return await ctx.send(embed=embed)

        ctx.voice_client.source.volume = volume / 100
        await ctx.send(f"Changed volume to {volume}%")
    
    @commands.command()
    async def _loop(self, ctx):
        self.loopQ += 1

        if self.loopQ == 3:
            self.loopQ = 0

        if (self.loopQ == 0):
            await ctx.send(embed=discord.Embed(color=discord.Color.blue(), description=f"Looping is now **disabled**."))

        elif (self.loopQ == 1):
            await ctx.send(embed=discord.Embed(color=discord.Color.blue(), description=f"Now looping the **queue**."))

        elif (self.loopQ == 2):
            await ctx.send(embed=discord.Embed(color=discord.Color.blue(), description=f"Now looping the **current track**."))

    @commands.command()
    async def _next(self, ctx):
        if (self.qID < self.queueSize):
            self.qID += 1
            ctx.voice_client.stop()
            await self.playQueue(ctx)
        
        else:
            await ctx.send("cannot skip to next track!")

    @commands.command()
    async def _last(self, ctx):
        if (self.qID > 0):
            self.qID -= 1
            ctx.voice_client.stop()
            await self.playQueue(ctx)
        else:
            await ctx.send("cannot go back to previous track!")

    @commands.command()
    async def _shuffle(self, ctx):
        pass

    @commands.command
    async def _list(self, ctx):
        pass


    @commands.command()
    async def _clear(self, ctx):
        self.queue = {}
        self.qID = 0

    def cache(self):
        self.qID = 0
        self.queue = {}
        path = "./bot/data/music"
        ext = [
            '.webm',
            '.mp3',
            '.wav'
        ]
        for f in os.listdir(path):
            for e in ext:
                if f.endswith(e):
                    os.remove(os.path.join(path, f))

    async def playQueue(self, ctx):
        while self.qID < len(self.queue):
            try:
                ctx.voice_client.play(self.queue[self.qID], after=lambda e: print(f'Player error: {e}') if e else None)
                embed = discord.Embed(color=discord.Color.blue())
                embed.add_field(name="Now Playing", value=f"[{self.queue[self.qID].title}]({self.queue[self.qID].url}) [{self.queueUser[self.qID].mention}]")
                await ctx.send(embed=embed)
            except Exception as e:
                embed = discord.Embed(color=discord.Color.blue())
                embed.add_field(name="Queued", value=f"[{self.queue[self.qID].title}]({self.queue[self.qID].url}) [{self.queueUser[self.qID].mention}]")
                await ctx.send(embed=embed)

            if (self.loopQ != 2):
                self.qID += 1
            
        
        if (self.loopQ == 1):
            self.qID = 0
        else:
            self.queue = {}
            self.qID = 0



def setup(bot):
    bot.add_cog(Music(bot))