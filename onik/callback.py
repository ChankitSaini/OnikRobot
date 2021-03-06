from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

from config import Onik

@Client.on_callback_query(filters.regex("cbguide"))
async def cbguide(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""ā HOW TO USE THIS BOT:

1.) First, add me to your group.
2.) Then promote me as admin and give all permissions except anonymous admin.
3.) Add @{Onik.ASSISTANT_USERNAME} to your group.
4.) Turn on the voice chat first before start to stream video.
5.) Type /vstream (reply to video) to start streaming.
6.) Type /vstop to end the video streaming.

š **Note: `/vstream` & `/vstop` command can only be executed by group admin only!**

ā” __Maintained by [Neurotic Association](https://t.me/NeuroticAssociation)__""",
        reply_markup=InlineKeyboardMarkup(
            [[
                InlineKeyboardButton(
                    "š” Go Back", callback_data="cbstart")
            ]]
        ), disable_web_page_preview=True
    )


@Client.on_callback_query(filters.regex("cbstart"))
async def cbstart(_, query: CallbackQuery):
    await query.edit_message_text(
        f"āØ **Hello there, I'm {Onik.BOT_NAME}.**\n\nš­ **I was created to stream videos in group "
        f"video chats easily.**\n\nā **To find out how to use me, please press the help button below** šš»",
        reply_markup=InlineKeyboardMarkup(
            [[
                InlineKeyboardButton(
                    "š All Command List", callback_data="cblist")
            ], [
                InlineKeyboardButton(
                    "ā HOW TO USE THIS BOT", callback_data="cbguide")
            ], [
                InlineKeyboardButton(
                    "š Terms & Condition", callback_data="cbinfo")
            ], [
                InlineKeyboardButton(
                    "š¬ Group", url="https://t.me/NeuroticBotSupport"),
                InlineKeyboardButton(
                    "š£ Channel", url="https://t.me/NeuroticBots")
            ], [
                InlineKeyboardButton(
                    "š©š»āš» Developer", url="https://t.me/NeuroticAssociation")
            ]]
        ))


@Client.on_callback_query(filters.regex("cbinfo"))
async def cbinfo(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""š **Onik's information !**

š¤ __This bot was created to stream video in telegram group video chats using several methods from WebRTC.__

š” __Powered by PyTgcalls the Async client API for the Telegram Group Calls, and Pyrogram the telegram MTProto API 
Client Library and Framework in Pure Python for Users and Bots.__

šØš»āš» __Thanks to the developers who participated in the development of this bot, the list of devs can be seen below:__

š¤µš» Ā» [Chankit Saini](https://github.com/NeuroticCoders) - Owner
š©š»āāļø Ā» [Levina Shavila](https://github.com/levina-lab) - Dev
š¤µš» Ā» [Sammy-XD](https://github.com/Sammy-XD) - Dev

__This bot licensed under MIT License__""",
        reply_markup=InlineKeyboardMarkup(
            [[
                InlineKeyboardButton(
                    "š” Go Back", callback_data="cbstart")
            ]]
        ),
        disable_web_page_preview=True
    )


@Client.on_callback_query(filters.regex("cblist"))
async def cblist(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""š All Command List:

Ā» /vstream (reply to video or yt/live url) - to stream video
Ā» /vend - stop the video streaming
Ā» /song (song name) - download song from YT
Ā» /vsong (video name) - download video from YT
Ā» /lyrics (song name) - lyrics scrapper

š° EXTRA CMD:

Ā» /alive - check bot alive status
Ā» /ping - check bot ping status
Ā» /uptime - check bot uptime status
Ā» /sysinfo - check bot system information

ā” __Maintained by [Neurotic Association](https://t.me/NeuroticAssociation)__""",
        reply_markup=InlineKeyboardMarkup(
            [[
                InlineKeyboardButton(
                    "š” Go Back", callback_data="cbstart")
            ]]
        ), disable_web_page_preview=True
    )


@Client.on_callback_query(filters.regex("cls"))
async def close(_, query: CallbackQuery):
    await query.message.delete()
