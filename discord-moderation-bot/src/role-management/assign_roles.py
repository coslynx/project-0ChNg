import discord
from discord.ext import commands

class RoleManagement(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='assignrole')
    async def assign_role(self, ctx, member: discord.Member, role: discord.Role):
        await member.add_roles(role)
        await ctx.send(f'{member.mention} has been assigned the role {role.name}')

def setup(bot):
    bot.add_cog(RoleManagement(bot))