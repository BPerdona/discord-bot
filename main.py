from typing import Any
import discord
import os
import random
from discord.flags import Intents

from dotenv import load_dotenv

class DiscordClient(discord.Client):
    def __init__(self, *, intents: Intents, **options: Any) -> None:
        super().__init__(intents=intents, **options)
        self.gun_bullets = 6

    async def on_ready(self):
        print(f'We have logged in as {client.user}')

    async def on_message(self, message):
        if message.author == client.user:
            return

        match message.content.split(' ')[0]:
            case '/roleta':
                await self.handle_roulette(message)

            case '/muteme':
                await self.handle_muteme(message)

    async def handle_roulette(self, message):
        command_options = message.content.split(' ')
        command_options.pop(0)
        
        match command_options:

            case ['recarregar']:
                self.gun_bullets = 6
                await message.reply("Revolver recarregado!", mention_author=True)

            case ['munição']:
                await message.reply(f'O Revolver esta carregado com {self.gun_bullets} munições!')

            case ['help']:
                await message.reply(f'Comandos disponíveis: \n recarregar -> Reinicia roleta \n munição -> Retorna quantas munições ainda estão no barril \n help -> Retorna lista de comandos')

            case _:
                random_int = random.randint(1, self.gun_bullets)
                if random_int == 1:
                    await message.reply('"Bang"\nTomou na lapa', mention_author=True)
                    self.gun_bullets = 6
                else:
                    self.gun_bullets-=1
                    await message.reply(f'"Click!"\nVocê continua vivo!\nDisparos restantes: {self.gun_bullets}', mention_author=True)

    async def handle_muteme(self, message):
        await message.reply(f'Not Implemented yet', mention_author=True)

load_dotenv()
bot_token = os.getenv('TOKEN')

intents = discord.Intents.default()
intents.message_content = True

client = DiscordClient(intents=intents)

client.run(bot_token)