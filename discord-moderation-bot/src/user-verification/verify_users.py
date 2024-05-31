import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.typing = False
intents.presences = False

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')

@bot.command()
async def verify(ctx):
    # Logic for user verification process
    await ctx.send('Verification process initiated. Please follow the instructions.')

bot.run('YOUR_DISCORD_BOT_TOKEN')