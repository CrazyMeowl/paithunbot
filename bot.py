import discord
from discord.ext import commands, tasks
from discord.voice_client import VoiceClient
from discord.utils import get
import os
from random import choice



client = commands.Bot(command_prefix = 'p.')

@client.event
async def on_ready():
	print("CrazyBot is ready")


@client.event
async def on_member_join(member):
	print(f'{member} has joined a server')


@client.event
async def on_member_remove(member):
	print(f'{member} has left a server')


@client.command()
async def ping(ctx):
	await ctx.send(f'Pong! {round(client.latency *1000)}ms')


@client.command(aliases = ['hi','Hai','Hi','hai','hello','Hello','Hellu','hellu'])
async def _hai(ctx):
	responses = [
	'Haii',
	'Helluu',
	'Hello',
	'Quen biết không mà hi'
	]	
	await ctx.send(f'{choice(responses)} {ctx.author.mention}')


@client.command(name = 'clear',aliases=['clearchat'])
@commands.has_permissions(administrator=True)
async def clear(ctx,amount):
	await ctx.channel.purge(limit = int(amount))

@client.command(name = 'huncongchua', aliases = ['hun','Hun','moah','muah'])
#@commands.has_any_role(735473153765277777,735898025121153108)
async def _hunCongChua(ctx):
	authorrole = []
	for _ in ctx.author.roles:
		authorrole.append(_.id)

	if 735473153765277777 in authorrole or 735898025121153108 in authorrole:
		responses = [
		'Hun lại nè',
		'Ngại quá',
		'Muahh'
		]	
		await ctx.send(f'{choice(responses)} {ctx.author.mention}')
	else:
		responses = [
		'Không hun thường dân nha',
		'Chỉ hun công chúa thui nha',
		'#NO HOMO'
		]	
		await ctx.send(f'{choice(responses)} {ctx.author.mention}')

@client.command()
async def test(ctx):
	for role in ctx.author.roles:
		print(type(role.id))





status = ['test1', 'test2', 'test3']


@client.command(name='play', help='This command plays music')
async def play(ctx, url):
    if not ctx.message.author.voice:
        await ctx.send("You are not connected to a voice channel")
        return

    else:
        channel = ctx.message.author.voice.channel

    await channel.connect()

    server = ctx.message.guild
    voice_channel = server.voice_client

    async with ctx.typing():
        player = await YTDLSource.from_url(url, loop=client.loop)
        voice_channel.play(player, after=lambda e: print('Player error: %s' % e) if e else None)

    await ctx.send('**Now playing:** {}'.format(player.title))

@client.command(name='stop', help='This command stops the music and makes the bot leave the voice channel')
async def stop(ctx):
    voice_client = ctx.message.guild.voice_client
    await voice_client.disconnect()

@tasks.loop(seconds=10)
async def change_status():
    await client.change_presence(activity=discord.Game(choice(status)))


client.run(os.environ['DISCORD_TOKEN'])