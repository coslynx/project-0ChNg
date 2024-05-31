import discord
from discord.ext import commands

class RemoveRoles(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='remove_roles', help='Remove roles from users after a certain period of inactivity')
    async def remove_roles(self, ctx, role_name: str, inactivity_period: int):
        role = discord.utils.get(ctx.guild.roles, name=role_name)
        if role is None:
            await ctx.send('Role not found')
            return

        for member in ctx.guild.members:
            last_message = max(member.activity, default=None, key=lambda x: x.created_at)
            if last_message is not None:
                time_difference = (ctx.message.created_at - last_message.created_at).days
                if time_difference >= inactivity_period:
                    await member.remove_roles(role)

        await ctx.send(f'{role_name} role removed from inactive users after {inactivity_period} days')

def setup(bot):
    bot.add_cog(RemoveRoles(bot))