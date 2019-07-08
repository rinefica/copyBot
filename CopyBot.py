import discord


class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as', self.user)

    async def on_message(self, message):
        # don't respond to ourselves
        if message.author == self.user:
            return

        for channel in message.channel_mentions:
            await channel.send(message.content)


client = MyClient()
client.run('token')
