import discord
from discord.ext import commands
import random
import time


class GeneralCommands(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print("Generalcommands.py is ready.")

    # random 5 name generator for a match in csgo
    @commands.command(aliases=["csgo", "teamroll", "wheelofnames"])
    async def wheel_of_names(self, ctx, *args):
        players = args
        chosen_players = random.sample(players, 5)
        player1 = chosen_players[0]
        player2 = chosen_players[1]
        player3 = chosen_players[2]
        player4 = chosen_players[3]
        player5 = chosen_players[4]
        await ctx.send("**THE PLAYERS ARE...**  ")
        time.sleep(1)
        await ctx.send(f'\n**`{player1.upper()}`**')
        time.sleep(0.5)
        await ctx.send(f'\n**`{player2.upper()}`**')
        time.sleep(0.5)
        await ctx.send(f'\n**`{player3.upper()}`**')
        time.sleep(0.5)
        await ctx.send(f'\n**`{player4.upper()}`** \nand... Lucky Last!')
        time.sleep(1.5)
        await ctx.send(f'\n**`{player5.upper()}`**')


    # 8ball magic for some fun
    @commands.command(aliases=["8ball", "eightball"])
    async def magic_eightball(self, ctx, *, question):
        with open("responses.txt", "r") as f:
            random_responses = f.readlines()
            response = random.choice(random_responses)

        await ctx.send(response)

    # quote recording
    @commands.command(aliases=["nickquote", "nicksaid"])
    async def nick_quote(self, ctx, *, args):
        with open("quotes.txt", "a") as n:
            quotes = str(args)
            n.write(f"\n{quotes}")
            n.close()
        await ctx.send(f"`{quotes}`, has been added to the quotes.")

    @commands.command(aliases=["whatnicksay", "nicksays"])
    async def nick_says(self, ctx):
        with open("quotes.txt", "r") as f:
            random_quotes = f.readlines()
            quotes = random.choice(random_quotes)
        await ctx.send(quotes)

    # @commands.command(aliases=["test"])
    # async def tested(self, ctx, *args):
    #     players = args
    #     chosen_players = random.sample(players, 5)
    #     player1 = chosen_players[0]
    #     player2 = chosen_players[1]
    #     player3 = chosen_players[2]
    #     player4 = chosen_players[3]
    #     player5 = chosen_players[4]
    #     await ctx.send("**THE PLAYERS ARE...**  ")
    #     time.sleep(1)
    #     await ctx.send(f'\n**`{player1.upper()}`**')
    #     time.sleep(0.5)
    #     await ctx.send(f'\n**`{player2.upper()}`**')
    #     time.sleep(0.5)
    #     await ctx.send(f'\n**`{player3.upper()}`**')
    #     time.sleep(0.5)
    #     await ctx.send(f'\n**`{player4.upper()}`** \nand... Lucky Last!')
    #     time.sleep(1.5)
    #     await ctx.send(f'\n**`{player5.upper()}`**')

        # await ctx.send(f"**The players are...** "
        #                f"\n>>> {player5}\n{player1}\n{player2}\n{player3}\n{player4}")


async def setup(client):
    await client.add_cog(GeneralCommands(client))
