import os
import discord
from discord.ext import commands
import asyncio
import random


TOKEN = "MTA5MDA1NTEzNTU4MzAzMTQ1OA.GYW3p9.PZb90oA0StxRw3gCCm4Ne3I4ykkj_EJ8T_dWUs"

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

# @client.command()
# async def ping(ctx):
#     bot_latency = round(client.latency * 1000)
#
#     await ctx.send(f"{bot_latency} ms")
#
#
# # random 5 name generator for a match in csgo
# @client.command(aliases=["csgo", "teamroll", "wheelofnames"])
# async def wheel_of_names(ctx, *args):
#     players = args
#     chosen_players = random.sample(players, 5)
#     await ctx.send(f"**The players are...**  \n> `{', '.join(chosen_players)}`")
#
#
# # 8ball magic for some fun
# @client.command(aliases=["8ball", "eightball"])
# async def magic_eightball(ctx, *, question):
#     with open("responses.txt", "r") as f:
#         random_responses = f.readlines()
#         response = random.choice(random_responses)
#
#     await ctx.send(response)
#
#
# # quote recording
# @client.command(aliases=["nickquote", "nicksaid"])
# async def nick_quote(ctx, *, args):
#     with open("quotes.txt", "a") as n:
#         quotes = str(args)
#         n.write(f"\n{quotes}")
#         n.close()
#     await ctx.send(f"`{quotes}`, has been added to the quotes.")
#
#
# @client.command(aliases=["whatnicksay", "nicksays"])
# async def nick_says(ctx):
#     with open("quotes.txt", "r") as f:
#         random_quotes = f.readlines()
#         quotes = random.choice(random_quotes)
#     await ctx.send(quotes)
#
#
# # async def load():
# #     for filename in os.listdir("./cogs"):
#
# client.run(TOKEN)
