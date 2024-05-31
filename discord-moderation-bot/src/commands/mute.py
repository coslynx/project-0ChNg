import discord

from discord.ext import commands

class Mute(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def mute(self, ctx, member: discord.Member, duration: int):
        role = discord.utils.get(ctx.guild.roles, name="Muted")
        
        if not role:
            role = await ctx.guild.create_role(name="Muted")
            for channel in ctx.guild.channels:
                await channel.set_permissions(role, send_messages=False)

        await member.add_roles(role)
        await ctx.send(f"{member.mention} has been muted for {duration} minutes.")

        await asyncio.sleep(duration * 60)
        await member.remove_roles(role)
        await ctx.send(f"{member.mention} has been unmuted after {duration} minutes.")

def setup(client):
    client.add_cog(Mute(client))