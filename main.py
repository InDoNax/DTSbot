import random
#import discord
#import os
from discord.ext.commands import Bot
from config import maintoken


client = Bot(command_prefix="!")


@client.command(name='CoinFlip',
                description="randomly lands on heads or tails",
                brief="flips a coin",
                aliases=['coin', 'flip'])
async def coin_flip():
    possible_responses = [
        'Heads',
        'Tails',
    ]
    await client.say(random.choice(possible_responses))

@client.command(name='WheelDecide', 
                description="takes a list of anime and decideds which anime you should watch", 
                breif="helps decide next anime episode",
                aliases=['anime','spin','wheel','decide'])
async def WheelDecide():
    
    choices = ['Sumo','sao','mob','shield','neverland','dorororororo','kaguya','home girl']
    #choices = choices.split()

    await client.say(random.choice(choices))


client.run(maintoken)