import os
import discord
from discord.ext import commands
import keep_alive

keep_alive.keep_alive()

intents = discord.Intents.default()
intents.messages = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'Bot is online as {bot.user}!')

@bot.command()
async def ping(ctx):
    await ctx.send('Pong!')

# Start the bot with your token
bot.run(os.getenv('DISCORD_TOKEN'))