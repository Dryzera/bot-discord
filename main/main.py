import discord
import json

base = {}
PATH_IMPORT_DB = '.\\base\\db.json'

class ImportBase:
    def __init__(self, json):
        self.import_json = json

    def imports(self):
        with open(PATH_IMPORT_DB, 'r', encoding='utf8') as file:
            base = json.load(file)
        return base

class MyClient(discord.Client):
    async def on_ready(self):
        print(f'Logged on as {self.user}!')

    async def on_message(self, message):
        print(f'Message from {message.author}: {message.content}')

intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents=intents)
client.run('my token goes here')
