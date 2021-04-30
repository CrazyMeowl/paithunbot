import discord
from discord.ext import commands
from discord.utils import get
import os
import random
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
	await ctx.send(f'{random.choice(responses)} {ctx.author.mention}')


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
		await ctx.send(f'{random.choice(responses)} {ctx.author.mention}')
	else:
		responses = [
		'Không hun thường dân nha',
		'Chỉ hun công chúa thui nha',
		'#NO HOMO'
		]	
		await ctx.send(f'{random.choice(responses)} {ctx.author.mention}')

@client.command()
async def test(ctx):
	for role in ctx.author.roles:
		print(type(role.id))

client.run(os.environ['DISCORD_TOKEN'])