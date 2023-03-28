import discord
from discord.ext import commands, tasks
import random

TOKEN = "MTA5MDA1NTEzNTU4MzAzMTQ1OA.GYW3p9.PZb90oA0StxRw3gCCm4Ne3I4ykkj_EJ8T_dWUs"

client = commands.Bot(command_prefix="//", intents=discord.Intents.all())


@client.event
async def on_ready():
    print("Bot is connected to discord.")


@client.command()
async def ping(ctx):
    bot_latency = round(client.latency * 1000)

    await ctx.send(f"{bot_latency} ms")


# random 5 name generator for a match in csgo
@client.command(aliases=["csgo", "teamroll"])
async def team_Select(ctx, *args):
    players = args
    chosen_players = random.sample(players, 5)
    await ctx.send(f"**The players are...**  \n> `{', '.join(chosen_players)}`")


# 8ball magic for some fun
@client.command(aliases=["8ball", "eightball"])
async def magic_eightball(ctx, *, question):
    with open("responses.txt", "r") as f:
        random_responses = f.readlines()
        response = random.choice(random_responses)

    await ctx.send(response)


# quote recording
@client.command(aliases=["bdnquote", "nickrecord", "nick_quote"])
async def nick_quote(ctx, *, args):
    with open("quotes.txt", "a") as n:
        quotes = str(args)
        n.write(f"\n{quotes}")
        n.close()
    await ctx.send(f"`{quotes}`, has been added to the quotes.")


client.run(TOKEN)
