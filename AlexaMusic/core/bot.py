#
# Copyright (C) 2021-2022 by Alexa_Help@Github, < https://github.com/Jankarikiduniya >.
# A Powerful Music Bot Property Of Rocks Indian Largest Chatting Group

# Kanged By © @Dr_Asad_Ali
# Rocks © @Shayri_Music_Lovers
# Owner Asad Ali
# Harshit Sharma
# All rights reserved. © Alexa © Yukki


import sys

from pyrogram import Client

import config

from ..logging import LOGGER


class AlexaBot(Client):
    def __init__(self):
        LOGGER(__name__).info(f"Starting Bot...")
        super().__init__(
            "MusicBot",
            api_id=config.API_ID,
            api_hash=config.API_HASH,
            bot_token=config.BOT_TOKEN,
        )

    async def start(self):
        await super().start()
        get_me = await self.get_me()
        self.username = get_me.username
        self.id = get_me.id
        try:
            await self.send_message(
                config.LOG_GROUP_ID, "» ᴍᴜsɪᴄ ʙᴏᴛ sᴛᴀʀᴛᴇᴅ, ᴡᴀɪᴛɪɴɢ ғᴏʀ ᴀssɪsᴛᴀɴᴛ..."
            )
        except:
            LOGGER(__name__).error(
                "Bot has failed to access the log Group. Make sure that you have added your bot to your log channel and promoted as admin!"
            )
            sys.exit()
        a = await self.get_chat_member(config.LOG_GROUP_ID, self.id)
        if a.status != "administrator":
            LOGGER(__name__).error("Please promote Bot as Admin in Logger Group")
            sys.exit()
        if get_me.last_name:
            self.name = get_me.first_name + " " + get_me.last_name
        else:
            self.name = get_me.first_name
        LOGGER(__name__).info(f"MusicBot Started as {self.name}")

        from pyrogram import Client
from pyrogram.errors import UserNotParticipant

class YourBot(Client):
    async def on_start(self, _):
        try:
            chat_member = await self.get_chat_member(config.LOG_GROUP_ID, self.id)
            if chat_member.status == "administrator":
                print("Bot is an administrator in the group. Proceed with your logic.")
                # Add your main bot logic here
            else:
                print("Bot is not an administrator in the group. Please promote it.")
        except UserNotParticipant:
            print("Bot is not a participant in the group. Add the bot to the group.")

# Initialize your bot
bot = YourBot("my_bot", bot_token="YOUR_BOT_TOKEN")

# Start the bot
bot.run()
