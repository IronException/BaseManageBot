import discord
import Config
import Reaction

reactions = {}


class MyClient(discord.Client):

    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))

    async def on_message(self, message):
        print('Message from {0.author}: {0.content}'.format(message))
        if message.author.id == self.user.id:
            return
        rV = Reaction.react(message.author, message.content, reactions)
        if rV:
            await message.channel.send(rV)



client = MyClient()
client.run(Config.token)
