import discord
import Config


class MyClient(discord.Client):

    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))

    async def on_message(self, message):
        print('Message from {0.author}: {0.content}'.format(message))
        if message.author.id == "IronException#4092":
            print("but yea..")
            await message.channel.send('Send me that \N{THUMBS UP SIGN} reaction, mate')


client = MyClient()
client.run(Config.token)
