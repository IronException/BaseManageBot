import discord
import Config

reactions = {}
reactions["IronException#4092"] = "Send me that \N{THUMBS UP SIGN} reaction, mate"


class MyClient(discord.Client):

    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))

    async def on_message(self, message):
        print('Message from {0.author}: {0.content}'.format(message))
        if message.author.id == self.user.id:
            return

        for r in reactions:
            if str(message.author) == r:
                await message.channel.send(reactions[r])

        if message.content.startswith("!add"):
            print(message.content)


client = MyClient()
client.run(Config.token)
