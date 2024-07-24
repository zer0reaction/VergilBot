from pyrogram import *
import creds


vergil = Client(
    name=creds.bot_name,
    api_id=creds.api_id,
    api_hash=creds.api_hash,
    bot_token=creds.bot_token
)


@vergil.on_message()
async def on_message(client, message):
    await message.forward(message.from_user.id)


async def main():
    async with vergil:
        # With starts and ends bot
        ...


# vergil.run(main())
vergil.run()
