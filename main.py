import os, discord
from better_profanity import profanity

TOKEN = os.environ["TOKEN"]
CHANNEL_ID = os.environ["CHANNEL_ID"]

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if client.user.mentioned_in(message):
        print(message.content)
        if profanity.contains_profanity(message.content): 
            await message.channel.send("\"No more saying cusswords guys\"")
        else:
            await message.channel.send('Hello!')

client.run(TOKEN)