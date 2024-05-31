import discord
from discord.ext import commands

class Kick(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='kick', help='Kick a user from the server')
    @commands.has_permissions(kick_members=True)
    async def kick_user(self, ctx, member: discord.Member, *, reason=None):
        try:
            await member.kick(reason=reason)
            await ctx.send(f'{member.mention} has been kicked from the server.')
        except discord.Forbidden:
            await ctx.send('I do not have permission to kick this user.')
        except discord.HTTPException:
            await ctx.send('Failed to kick the user. Please try again.')

def setup(bot):
    bot.add_cog(Kick(bot))