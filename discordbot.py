# @author Thad Shinno
import discord
from discord.ext import commands

# dont copy this box ########################
# import json                               #
# with open("settings.json", "r") as fp:    #
#    settings = json.load(fp)               #
#    TOKEN = settings["token"]              #
# ###########################################

client = commands.Bot(command_prefix='.') # client is the bot itself

# displays activity on log on
@client.event
async def on_ready():
    print("Bot is online")
    myactivity = discord.Activity(name = "a game", type = discord.ActivityType.playing)
    await client.change_presence(activity=myactivity)

# greets a user every time they say hello
@client.event
async def on_message(message):
	if not (iscommand(message.content) or (message.author == client.user)):		
		if ("hello" in message.content):
			await message.channel.send("hello, " + message.author.mention)
		
	await client.process_commands(message)
	
# hello world	
@client.command()
async def hello(ctx):
    await ctx.send("Hello World!")

# repeat message
@client.command()
async def echo(ctx):
    content = ctx.message.content
    content = content.split(" ", 1)
    await ctx.send(content[1])

# clear past 200 messages
@client.command()
@commands.has_permissions(manage_messages=True)
async def clear(ctx):
	await ctx.channel.purge(limit=200)

# print bubblewrap
@client.command()
async def bubblewrap(ctx):
	bubbles = []
	for i in range(120):
		bubbles.append("||pop!||")
		
	message = "".join(bubbles)
	await ctx.send(message)

# send a rickroll
@client.command()
async def rickroll(ctx):
	rick = discord.Embed(
		title="Not a rickroll I swear",
		url = "https://www.youtube.com/watch?v=dQw4w9WgXcQ",
		color = discord.Color.green(),
	)
	rick.set_image(url="https://i.kym-cdn.com/entries/icons/original/000/026/489/crying.jpg")
	await ctx.send(embed=rick)

# log out the bot
@client.command()
@commands.is_owner()
async def shutdown(ctx):
    await ctx.bot.logout()

# checks if a string begins with a command
def iscommand(message):
	if message.startswith(tuple([".hello", ".echo", ".clear", ".bubblewrap", ".rickroll", ".shutdown"])):
		return True
	return False

client.run(TOKEN) # change this