import asyncio
import sys
sys.path.append('..')
from pyrogram import Client, idle
from config import API_ID, API_HASH, BOT_TOKEN
from onik.videoplayer import app
from onik.videoplayer import call_py

PLUGINS = dict(
    root="onik",
    include=[
        "callback"  ,
        "inline",
        "sysinfo",
        "song",
        "start",
        "ytsearch",
        "videoplayer"
    ]
)

bot = Client(
    ":memory:",
    API_ID,
    API_HASH,
    bot_token=BOT_TOKEN,
    plugins=PLUGINS),
)

bot.start()
print("[STATUS]:✅ »» BOT CLIENT STARTED ««")
app.start()
print("[STATUS]:✅ »» USERBOT CLIENT STARTED ««")
call_py.start()
print("[STATUS]:✅ »» PYTGCALLS CLIENT STARTED ««")
idle()
print("[STATUS]:❌ »» BOT STOPPED ««")
