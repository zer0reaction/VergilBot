from pyrogram import *
from pyrogram.types import (InlineQueryResultArticle, InputTextMessageContent, InlineKeyboardMarkup, InlineKeyboardButton)
import creds


# Specified in creds.py file
vergil = Client(
    name=creds.bot_name,
    api_id=creds.api_id,
    api_hash=creds.api_hash,
    bot_token=creds.bot_token
)


# Handling incoming messages
@vergil.on_message()
async def on_message(client, message):
    ...


# Handling inline queries (e.g. @berrieddelight_bot hi)
@vergil.on_inline_query()
async def on_inline_query(client, inline_query):
    await vergil.answer_inline_query(
        inline_query_id=inline_query.id,
        results=[
            InlineQueryResultArticle("Title", InputTextMessageContent("Message content"))
        ]
    )


async def main():
    async with vergil:
        ...


# vergil.run(main())
vergil.run()
