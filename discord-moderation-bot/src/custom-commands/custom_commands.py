import discord
from discord.ext import commands

intents = discord.Intents.default()
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')

@bot.command()
async def kick(ctx, member: discord.Member, *, reason=None):
    if ctx.author.guild_permissions.kick_members:
        await member.kick(reason=reason)
        await ctx.send(f'{member} has been kicked.')
    else:
        await ctx.send('You do not have permission to kick members.')

@bot.command()
async def ban(ctx, member: discord.Member, *, reason=None):
    if ctx.author.guild_permissions.ban_members:
        await member.ban(reason=reason)
        await ctx.send(f'{member} has been banned.')
    else:
        await ctx.send('You do not have permission to ban members.')

@bot.command()
async def mute(ctx, member: discord.Member, duration: int, *, reason=None):
    if ctx.author.guild_permissions.manage_roles:
        role = discord.utils.get(ctx.guild.roles, name='Muted')
        if not role:
            role = await ctx.guild.create_role(name='Muted')
            for channel in ctx.guild.channels:
                await channel.set_permissions(role, send_messages=False)
        await member.add_roles(role, reason=reason)
        await ctx.send(f'{member} has been muted for {duration} minutes.')
        await asyncio.sleep(duration * 60)
        await member.remove_roles(role)
        await ctx.send(f'{member} has been unmuted.')
    else:
        await ctx.send('You do not have permission to mute members.')

bot.run('YOUR_BOT_TOKEN')