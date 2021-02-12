# bot.py
import os
import random
from dotenv import load_dotenv

from discord.ext import commands


load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
bot = commands.Bot(command_prefix='healbot ')


@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')


def clw():
    # 1d8+1 since wand is cast at minimum level
    # randint is inclusive on both ends in python
    return random.randint(2, 9)


def format_response(charges_used, health_cured):
    return f"You used {charges_used} Cure Light Wounds wand charges to cure {health_cured} hit points"


@bot.command(name='heal', help='healbot heal X will tell you how many charges of a cure light wounds wand it takes to heal at least X points of damage')
async def heal(ctx, health):
    health_cured = 0
    charges_used = 0
    while health_cured < int(health):
        health_cured += clw()
        charges_used += 1
    await ctx.send(format_response(charges_used, health_cured))


@bot.command(name='use', help='healbot use X will tell you how much healing you get from using X charges of a cure light wounds wand')
async def use(ctx, charges):
    health_cured = 0
    for charge in range(int(charges)):
        health_cured += clw()
    await ctx.send(format_response(charges, health_cured))


bot.run(TOKEN)