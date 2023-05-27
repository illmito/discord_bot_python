import os
import discord
from discord.ext import commands
import asyncio
import random


TOKEN = ""

client = commands.Bot(command_prefix="//", intents=discord.Intents.all())


@client.event
async def on_ready():
    print("Bot is connected to discord.")


async def load():
    for filename in os.listdir("./cogs"):
        if filename.endswith('.py'):
            await client.load_extension(f"cogs.{filename[:-3]}")


async def main():
    async with client:
        await load()
        await client.start(TOKEN)

asyncio.run(main())


# # random 5 name generator for a match in csgo
# @client.command(aliases=["csgo", "teamroll", "wheelofnames"])
# async def wheel_of_names(ctx, *args):
#     players = args
#     chosen_players = random.sample(players, 5)
#     await ctx.send(f"**The players are...**  \n> `{', '.join(chosen_players)}`")
## test