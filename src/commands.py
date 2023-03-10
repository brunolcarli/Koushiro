from io import BytesIO
import discord
from discord.ext import commands
import matplotlib.pyplot as plt

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

    plt.bar(height=data.values(), x=data.keys())
    plt.title('Messages average sentiment polarities')
    fig = plt.gcf()
    imgdata = BytesIO()
    fig.savefig(imgdata, format='png')
    imgdata.seek(0)
    plt.close()

    await ctx.send(
        'Average sentiment polarities from messages',
        embed=embed,
        file=discord.File(imgdata, filename='file.png')
    )


@client.command(aliases=['msg_rank', 'mrank'])
async def message_rank(ctx):
    """
    Return the rank ladder for messages sent by users in Twitch live chat
    """
    try:
        data = Query.query_top_ten()['data']['topTen']
    except:
        return await ctx.send('Sorry, something went wrong. Try again later!')

    embed = discord.Embed(color=0x1E1E1E, type="rich")
    for i, record in enumerate(data):
        embed.add_field(
            name=f'{i+1}) {record["username"]}',
            value=f'Messages: {record["messagesCount"]}',
            inline=False
        )

    await ctx.send(
        'Message sending ranking',
        embed=embed
    )


@client.command(aliases=['msent', 'mpols', 'mps', 'sent_rate', 'sr'])
async def messages_sentiment_rate(ctx):
    """
    Plots the sentiment and offensive level of each message.
    """
    try:
        data = Query.query_chat_messages()['data']['chatMessages']
    except:
        return await ctx.send('Sorry, something went wrong. Try again later!')

    sents = [i['messageSentiment'] for i in data]
    off_lvs = [i['messageOffenseLevel'] for i in data]

    plt.plot(sents, label='Sentiment polarity')
    plt.plot(off_lvs, label='Offensive level')
    plt.legend()
    plt.title('Sentiment and offensive rate')
    fig = plt.gcf()
    imgdata = BytesIO()
    fig.savefig(imgdata, format='png')
    imgdata.seek(0)
    plt.close()

    await ctx.send(
        'Message sentiment and offesive rate',
        file=discord.File(imgdata, filename='file.png')        
    )
