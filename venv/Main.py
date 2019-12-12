import discord
import Config


class MyClient(discord.Client):

    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))

    async def on_message(self, message):
        global reaction
        print('Message from {0.author}: {0.content}'.format(message))

        reaction = reaction.react_to_discord_message(message)


client = MyClient()
client.run(Config.token)
