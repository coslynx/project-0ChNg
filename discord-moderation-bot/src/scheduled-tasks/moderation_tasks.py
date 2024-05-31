import discord
from discord.ext import commands
import asyncio

class ModerationTasks(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print('Moderation Tasks cog is ready.')

    @commands.command(name='clear_chat', help='Clear chat history in a text channel.')
    async def clear_chat(self, ctx):
        await ctx.channel.purge()

    @commands.command(name='update_rules', help='Update server rules.')
    async def update_rules(self, ctx, new_rules):
        # Update server rules logic here
        await ctx.send(f'Server rules updated to: {new_rules}')

    @commands.Cog.listener()
    async def on_member_join(self, member):
        # Implement member join tasks logic here
        await member.send('Welcome to the server! Please read the rules.')

def setup(bot):
    bot.add_cog(ModerationTasks(bot))