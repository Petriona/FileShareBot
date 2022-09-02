from os import environ
from pyrogram import Client
from pyrogram import filters
from helper import new_file_id
from pyrogram.types import InlineKeyboardButton
from pyrogram.types import InlineKeyboardMarkup

BOT_TOKEN = environ.get("BOT_TOKEN")
API_ID = int(environ.get("API_ID"))
API_HASH = environ.get("API_HASH")
BOT_USERNAME = environ.get("BOT_USERNAME")

print("----------Starting Bot----------")

Bot = Client(
    "File Store Bot",
    bot_token=BOT_TOKEN,
    api_id=API_ID,
    api_hash=API_HASH
)

@Bot.on_message(filters.command('start'))
async def start(bot, message):
    if len(message.command) == 1:
        await message.reply(
            text=f"Hello {message.from_user.mention}, I am a Powerful File Store Bot devoloped by @Hagadmansa.\n\nJust send me any photo, video, voice, audio, document, sticker, animation or videonote, i'll share you you it's permanent link.",
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton('Updates', url='https://t.me/hagadmansa'),
                        InlineKeyboardButton('Support', url='https://t.me/hagadmansachat')
                    ],
                    [
                        InlineKeyboardButton('Website', url='https://hagadmansa.com'),
                        InlineKeyboardButton('Source', url='https://github.com/hagadmansa/FileStoreBot')
                    ]
                ]
            )
        )
    elif len(message.command) == 2:
        try:
            link = f"https://t.me/{BOT_USERNAME}?start={message.command[1]}"
            share = f"https://t.me/share/url?url={link}&text=Click%20on%20link%20to%20get%20the%20file%20now,%20Join%20@Hagadmansa"
            send = await message.reply_cached_media(
                file_id=message.command[1],
                reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton('Share now', url=share)
                        ]
                    ]
                )
            )
            media = replied.photo or replied.video or replied.voice or replied.document or replied.animation or replied.audio or replied.sticker 
            await send.edit(media.file_name)
        except:
            await message.reply('The media you are trying to get is invalid.')
            
@Bot.on_message(filters.private)
async def hagadmansa(bot, message):
    
    hagadmansa = await message.reply("`Processing...`")
    
    if message.text:
      return await hagadmansa.edit('Send me any photo, video, voice, audio, document, sticker, animation or videonote to get a permanent link.')
    
    media = message.photo or message.video or message.voice or message.document or message.animation or message.audio or message.sticker 
    link = f"https://t.me/{BOT_USERNAME}?start={new_file_id(media.file_id)}"
    share = f"https://t.me/share/url?url={link}&text=Click%20on%20link%20to%20get%20the%20file%20now,%20Join%20@Hagadmansa"
    await hagadmansa.edit(
        text=f"Here is your link: {link}",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton('Share now', url=share)
                ]
            ]
        )
    )

Bot.run()

print("----------Bot Started----------")
