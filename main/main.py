import discord
import json

base = {}
PATH_IMPORT_DB = '.\\base\\db.json'

class ImportBase:
    def imports(self):
        with open(PATH_IMPORT_DB, 'r', encoding='utf8') as file:
            base = json.load(file)
        return base

class MyClient(discord.Client):
    def on_ready(self):
        print(f'Logged on as {self.user}!')

    def on_message(self, message):
        print(f'Message from {message.author}: {message.content}')

imported = ImportBase().imports()
TOKEN = imported['token']
PREFIX = imported['prefix-bot']

intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents=intents)
client.run(TOKEN)
