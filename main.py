import os, discord
from better_profanity import profanity
from message_analyzer import Attributes

TOKEN = os.environ["TOKEN"]
C_PATH = os.environ["C_TEXT_PATH"]

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)
attrs = Attributes()
profanity.load_censor_words_from_file(C_PATH)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    attrs.set_attributes(message.content)
    attrs.set_attrs_dictionary()
    toxicity_score = attrs.get_max_score()
    if message.author == client.user:
        return

    if client.user.mentioned_in(message):
        
        attrs.log_message()
        # if profanity.contains_profanity(message.content): 
        #     await message.channel.send(
        #         '''This message contains profanity, it is possible that this was not intentional. Please rewrite your question in order for it to be answered.''')        
        
        # if toxicity_score >= 50: 
        #     await message.channel.send("This message contains toxic langauge and will not be searched, please avoid asking toxic questions.")
        
        await message.channel.send("Logged")
        
        
client.run(TOKEN)