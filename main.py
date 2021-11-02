from discord.ext import commands
from discord_together import DiscordTogether
import discord

client = commands.Bot(command_prefix="!")

@client.event
async def on_ready():
    client.togetherControl = await DiscordTogether("ㅌㅋㅌㅋ")
    print('Bot is online!')

@client.command()
async def youtube(ctx):
    link = await client.togetherControl.create_link(ctx.author.voice.channel.id, 'youtube')
    await ctx.send(f"파란색 링크를 눌러주세요 !\n{link}")

@client.command()
async def poker(ctx):
    link = await client.togetherControl.create_link(ctx.author.voice.channel.id, 'poker')
    await ctx.send(f"파란색 링크를 눌러주세요 !\n{link}")

@client.command()
async def chess(ctx):
    link = await client.togetherControl.create_link(ctx.author.voice.channel.id, 'chess')
    await ctx.send(f"파란색 링크를 눌러주세요 !\n{link}")

@client.command()
async def betrayal(ctx):
    link = await client.togetherControl.create_link(ctx.author.voice.channel.id, 'betrayal')
    await ctx.send(f"파란색 링크를 눌러주세요 !\n{link}")

@client.command()
async def fishing(ctx):
    link = await client.togetherControl.create_link(ctx.author.voice.channel.id, 'fishing')
    await ctx.send(f"파란색 링크를 눌러주세요 !\n{link}")

@client.command()
async def lettertile(ctx):
    link = await client.togetherControl.create_link(ctx.author.voice.channel.id, 'letter-tile')
    await ctx.send(f"파란색 링크를 눌러주세요 !\n{link}")

@client.command()
async def wordsnack(ctx):
    link = await client.togetherControl.create_link(ctx.author.voice.channel.id, 'word-snack')
    await ctx.send(f"파란색 링크를 눌러주세요 !\n{link}")

@client.command()
async def doodlecrew(ctx):
    link = await client.togetherControl.create_link(ctx.author.voice.channel.id, 'doodle-crew')
    await ctx.send(f"파란색 링크를 눌러주세요 !\n{link}")

@client.command()
async def 명령어(ctx):
    embed=discord.Embed(title="DISGAME 명령어", description="게임명령어는 음성방에 참가하고 있어야지 작동된답니다!")
    embed.add_field(name="!명령어", value="지금 이 명령어!", inline=True)
    embed.add_field(name="!youtube", value="유튜브 투게더", inline=False)
    embed.add_field(name="!poker", value="포커게임", inline=False)
    embed.add_field(name="!chess", value="체스게임", inline=False)
    embed.add_field(name="!betrayal", value="betrayal.io", inline=True)
    embed.add_field(name="!fishing", value="fishington.io", inline=True)
    embed.add_field(name="!lettertile", value="글자조각 맞추기", inline=True)
    embed.add_field(name="!wordsnack", value="글자 잇기", inline=True)
    embed.add_field(name="!doodlecrew", value="캐치마인드 비슷한게임", inline=True)
    embed.set_footer(text="제작자 ! ! 이미지#6625") #지우지말것
    await ctx.send(embed=embed)
    await ctx.send("https://discord.gg/c4GWM8RQWe | 공식서버에 참여해주세요!")
    
client.run("ㅌㅋㅌㅋ")
