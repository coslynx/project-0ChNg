import discord

class AutoResponses:
    def __init__(self, client):
        self.client = client

    async def check_auto_responses(self, message):
        if message.author == self.client.user:
            return

        if "hello" in message.content.lower():
            await message.channel.send("Hello! How can I assist you today?")

        if "goodbye" in message.content.lower():
            await message.channel.send("Goodbye! Have a great day.")

        # Add more auto responses based on specific keywords

def setup(client):
    client.add_cog(AutoResponses(client))