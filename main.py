import discord
from discord.ext import commands
import random

TOKEN = "MTA5MDA1NTEzNTU4MzAzMTQ1OA.GYW3p9.PZb90oA0StxRw3gCCm4Ne3I4ykkj_EJ8T_dWUs"

client = commands.Bot(command_prefix="//", intents=discord.Intents.all())


@client.event
async def on_ready():
    print("Bot is connected to discord.")


@client.command()
async def ping(ctx):
    bot_latency = round(client.latency * 1000)

    await ctx.send(f"Pong, {bot_latency} ms")


@client.command()
async def mosh(ctx):
    await ctx.send("pit")


@client.command()
async def add(ctx, a: int, b: int):
    await ctx.send(a + b)


@client.command(aliases=["8ball", "eightball"])
async def magic_eightball(ctx, *, question):
    with open("responses.txt", "r") as f:
        random_responses = f.readlines()
        response = random.choice(random_responses)

    await ctx.send(response)

client.run(TOKEN)
