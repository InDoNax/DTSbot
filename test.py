import random
import discord
import asyncio
from config import testtoken

client = discord.Client()


@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')



@client.event
async def on_message(message):
    print(message.channel)
    print(message.channel.id)
    print(message.author.name)
    print(message.content)
    if message.content.startswith('!play'):
        if int(message.channel.id) != 550271068066283520:
            await client.send_message(message.channel, message.author.name + ' PLEASE!!!! Use the music-bot channel for the music bots. It\'s there for a reason!')


    if message.content.startswith('!coin'):
        possible_responses = [
        'Heads',
        'Tails',
        ]
        await client.send_message(message.channel, random.choice(possible_responses))

    if message.content.startswith('!spin'):
        #choices = ['Sumo','sao','mob','shield','neverland','dorororororo','kaguya','home girl']
        sent = message.content
        sent = sent.split(' ', 1)[1]
        sent = sent.split(' ')
        #choices = .split()

        await client.send_message(message.channel, random.choice(sent))

        







client.run(testtoken)