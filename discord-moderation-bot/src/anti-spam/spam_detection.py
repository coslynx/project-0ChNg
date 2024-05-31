import discord
from discord.ext import commands
from collections import deque

class SpamDetection(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.spam_threshold = 5
        self.spam_detection_window = 30
        self.user_message_history = {}

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author == self.bot.user:
            return

        if message.author.id not in self.user_message_history:
            self.user_message_history[message.author.id] = deque(maxlen=self.spam_detection_window)

        user_history = self.user_message_history[message.author.id]
        user_history.append(message.created_at)

        if len(user_history) >= self.spam_threshold:
            time_difference = user_history[-1] - user_history[0]

            if time_difference.total_seconds() <= self.spam_detection_window:
                await message.channel.send(f"{message.author.mention}, you are sending messages too quickly. Please slow down.")
                # Implement action to take against spam (e.g., mute, kick, ban)

def setup(bot):
    bot.add_cog(SpamDetection(bot))