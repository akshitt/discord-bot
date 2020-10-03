from discord.ext import commands
token = 'sdkfmsdkmskd'


client = commands.Bot(command_prefix='>')

@client.event
async def on_ready():
	print("Heyyaa!")

@client.command()
async def heyy(ctx):
	await ctx.send("heyyy")

client.run(token)