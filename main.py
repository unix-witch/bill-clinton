#https://discord.com/api/oauth2/authorize?client_id=850485468390752288&permissions=0&scope=bot


import discord
import random
import json
import os

client = discord.Client()
prefix = '!'



messages = []

with open("messages.txt", "r") as usa:
	messages = usa.read().split('\n')

@client.event
async def on_ready():
	print("Server started")

	for guild in client.guilds:
		print(guild.name)

	await client.change_presence(activity=discord.Game(
		name='!help: invading the middle east'
	))



@client.event
async def on_message(message):
	if message.author == client.user:
		return

	
	if message.content == prefix + 'usa':
		print("bad thing got")
		await message.channel.send(random.choice(messages))
		
	
	elif message.content == prefix + 'help':
		print("helping")
		embed = discord.Embed(
			title='help',
			description=f'''
				{prefix}usa: Get a random bad thing
				{prefix}wmd: tells you if Saddam Hussein has nuclear weapons
				{prefix}help: Shows this
			'''
		)
		await message.channel.send(embed = embed)
	

	elif message.content == prefix + 'wmd':
		print("invading the middle east for WMD\'s")
		await message.channel.send('Saddam Hussein has nuclear weapons')


client.run(os.environ['token'])
