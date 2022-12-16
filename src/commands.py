import discord
from discord.ext import commands

from src.query import Query
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


@client.command(aliases=['avgp', 'avg_sent', 'avg_pol'])
async def average_polarity(ctx):
    """
    Return the messages average polarities percentage.
    """
    try:
        data = Query.query_message_avg_polarity()['data']['messageAveragePolarity']
    except:
        return await ctx.send('Sorry, something went wrong. Try again later!')

    embed = discord.Embed(color=0x1E1E1E, type="rich")
    embed.add_field(name='Positive :green_circle:', value=f"{data['positive']}%", inline=False)
    embed.add_field(name='Negative :red_circle:', value=f"{data['negative']}%", inline=False)
    embed.add_field(name='Neutral :white_circle: ', value=f"{data['neutral']}%", inline=False)

    await ctx.send('Average sentiment polarities from messages', embed=embed)
