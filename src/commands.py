import discord
from discord.ext import commands

from koushiro.settings import __version__


client = commands.Bot(
    intents=discord.Intents.all(),
    command_prefix='/'
)


@client.event
async def on_ready():
    """
    Prints a "log message" on the shell informing the bot (system)  was
    initialized and running.
    """
    print(f'Koushiro running version: {__version__}')


@client.command()
async def version(ctx):
    """
    Pings the bot to return its current version.
    """
    await ctx.send(f'Running version: {__version__}')
