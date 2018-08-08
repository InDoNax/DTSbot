import random
from discord.ext.commands import Bot

TOKEN="NDc2Njg1MjMzMzUwMTE1MzMx.DkylOw.SRCHtg4EnfhYNUXKI4O9Sa6_dH8"

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


client.run(TOKEN)