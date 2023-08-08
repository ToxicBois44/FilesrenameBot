#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) Shrimadhav U K & @No_OnE_Kn0wS_Me
import logging
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

import os
import time

# the secret configuration specific things
if bool(os.environ.get("WEBHOOK", False)):
    from sample_config import Config
else:
    from config import Config

# the Strings used for this "thing"
from translation import Translation

import pyrogram
logging.getLogger("pyrogram").setLevel(logging.WARNING)
from pyrogram import filters 
from pyrogram import Client as Mai_bOTs

#from helper_funcs.chat_base import TRChatBase
from helper_funcs.display_progress import progress_for_pyrogram

from pyrogram.errors import UserNotParticipant, UserBannedInChannel 
from pyrogram.types import ReplyKeyboardMarkup, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
from hachoir.metadata import extractMetadata
from hachoir.parser import createParser
# https://stackoverflow.com/a/37631799/4723940
from PIL import Image
from database.database import *
from database.db import *


@Mai_bOTs.on_message(pyrogram.filters.command(["help"]))
async def help_user(bot, update):
    update_channel = Config.UPDATE_CHANNEL
    if update_channel:
        try:
            user = await bot.get_chat_member(update_channel, update.chat.id)
            if user.status == "kicked":
               await update.reply_text(" Sorry, You're Banned")
               return
        except UserNotParticipant:
            await update.reply_text(
                text="**Due To The Huge Traffic Only Channel Members Can Use This Bot Means You Need To Join The Below Mentioned Channel Before Using Me ❗️ **",
                reply_markup=InlineKeyboardMarkup([
                    [ InlineKeyboardButton(text="⚡️𝓙𝓸𝓲𝓷 𝓜𝔂 𝓤𝓹𝓭𝓪𝓽𝓮𝓼 𝓒𝓱𝓪𝓷𝓷𝓮𝓵⚡️", url=f"https://t.me/{update_channel}")]
              ])
            )
            return
        else:
            await bot.send_message(
        chat_id=update.chat.id,
        text=Translation.HELP_USER,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton('📝ʀᴇɴᴀᴍᴇ', callback_data = "rnme"),
                    InlineKeyboardButton('📂​🇫ɪʟᴇ ᴛᴏ ᴠɪᴅᴇᴏ', callback_data = "f2v")
                ],
                [
                    InlineKeyboardButton('🎞️​🇨​​🇺​​🇸​​🇹​​🇴​​🇲​ ​🇹​​🇭​​🇺​​🇲​​🇧​​🇳​​🇦​​🇮​​🇱​', callback_data = "cthumb"),
                    InlineKeyboardButton('📑ᴄᴜ​​🇸ᴛᴏᴍ ᴄᴀᴘᴛɪᴏɴ', callback_data = "ccaption")
                ],
                [
                    InlineKeyboardButton('💬​🇦​​🇧​​🇴​​🇺​​🇹​', callback_data = "about")
                ]
            ]
        )
    )       

@Mai_bOTs.on_message(pyrogram.filters.command(["start"]))
async def start_me(bot, update):
    if update.from_user.id in Config.BANNED_USERS:
        await update.reply_text("You are Banned")
        return
    update_channel = Config.UPDATE_CHANNEL
    if update_channel:
        try:
            user = await bot.get_chat_member(update_channel, update.chat.id)
            if user.status == "kicked":
               await update.reply_text("​🇸​​🇴​​🇷​​🇷​​🇾​,​🇾​​🇴​​🇺​❜​🇻​​🇪​ ​🇧​​🇪​​🇪​​🇳​ ​🇫​​🇱​​🇴​​🇴​​🇩​​🇮​​🇳​​🇬​ ​🇲​​🇪​ ​🇸​​🇴​ ​🇲​​🇾​ ​🇴​​🇼​​🇳​​🇪​​🇷​ ​🇷​​🇪​​🇲​​🇴​​🇻​​🇪​​🇩​ ​🇾​​🇴​​🇺​ ​🇫​​🇷​​🇴​​🇲​ ​🇺​​🇸​​🇮​​🇳​​🇬​ ​🇲​​🇪​ ​🇮​​🇫​ ​🇾​​🇴​​🇺​ ​🇹​​🇭​​🇮​​🇳​​🇰​ ​🇮​​🇹​❜​🇸​ ​🇦​​🇳​ ​🇪​​🇷​​🇷​​🇴​​🇷​ ​🇨​​🇴​​🇳​​🇹​​🇦​​🇨​​🇹​ : @Jonathanlk")
               return
        except UserNotParticipant:
            await update.reply_text(
                text="**​🇩​​🇺​​🇪​ ​🇹​​🇴​ ​🇹​​🇭​​🇪​ ​🇭​​🇺​​🇬​​🇪​ ​🇹​​🇷​​🇦​​🇫​​🇫​​🇮​​🇨​ ​🇴​​🇳​​🇱​​🇾​ ​🇨​​🇭​​🇦​​🇳​​🇳​​🇪​​🇱​ ​🇲​​🇪​​🇲​​🇧​​🇪​​🇷​​🇸​ ​🇨​​🇦​​🇳​ ​🇺​​🇸​​🇪​ ​🇹​​🇭​​🇮​​🇸​ ​🇧​​🇴​​🇹​ ​🇲​​🇪​​🇦​​🇳​​🇸​ ​🇾​​🇴​​🇺​ ​🇳​​🇪​​🇪​​🇩​ ​🇹​​🇴​ ​🇯​​🇴​​🇮​​🇳​ ​🇹​​🇭​​🇪​ ​🇧​​🇪​​🇱​​🇴​​🇼​ ​🇲​​🇪​​🇳​​🇹​​🇮​​🇴​​🇳​​🇪​​🇩​ ​🇨​​🇭​​🇦​​🇳​​🇳​​🇪​​🇱​ ​🇧​​🇪​​🇫​​🇴​​🇷​​🇪​ ​🇺​​🇸​​🇮​​🇳​​🇬​ ​🇲​​🇪​ ❗️ **",
                reply_markup=InlineKeyboardMarkup([
                    [ InlineKeyboardButton(text="⚡️𝓙𝓸𝓲𝓷 𝓜𝔂 𝓤𝓹𝓭𝓪𝓽𝓮𝓼 𝓒𝓱𝓪𝓷𝓷𝓮𝓵⚡️", url=f"https://t.me/{update_channel}")]
              ])
            )
            return
        else:
            await update.reply_text(Translation.START_TEXT.format(update.from_user.first_name),
        reply_markup=InlineKeyboardMarkup(
            [
                [
                        InlineKeyboardButton("Help", callback_data = "ghelp")
                ],
                [
                    InlineKeyboardButton('⚡️𝓢𝓾𝓹𝓹𝓸𝓻𝓽 𝓒𝓱𝓪𝓷𝓷𝓮𝓵⚡️', url='https://t.me/cryptoupdatezx'),
                    InlineKeyboardButton('𝘾𝙞𝙣𝙚 𝙁𝙡𝙞𝙭 🇱🇰', url='https://t.me/Cineflixlk')
                ],
                [
                    InlineKeyboardButton('📊 𝘾𝙧𝙮𝙥𝙩𝙤 𝙐𝙥𝙙𝙖𝙩𝙚 📊', url='https://t.me/cryptoupdatezx'),
                    InlineKeyboardButton('🔰 𝗖𝗼𝗻𝘁𝗮𝗰𝘁 🔰', url='https://t.me/Jonathanlk')
                ]
            ]
        ),
        reply_to_message_id=update.message_id
    )
            return 

@Mai_bOTs.on_callback_query()
async def cb_handler(client: Mai_bOTs , query: CallbackQuery):
    data = query.data
    if data == "rnme":
        await query.message.edit_text(
            text=Translation.RENAME_HELP,
            disable_web_page_preview = True,
            reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton('Back', callback_data = "ghelp"),
                    InlineKeyboardButton("🔒 Close", callback_data = "close")
                ]
            ]
        )
     )
    elif data == "f2v":
        await query.message.edit_text(
            text=Translation.C2V_HELP,
            disable_web_page_preview = True,
            reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton('Back', callback_data = "ghelp"),
                    InlineKeyboardButton("🔒 Close", callback_data = "close")
                ]
            ]
        )
     )
    elif data == "ccaption":
        await query.message.edit_text(
            text=Translation.CCAPTION_HELP,
            disable_web_page_preview = True,
            reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton('Show Current Caption', callback_data = "shw_caption"),
                    InlineKeyboardButton("Delete Caption", callback_data = "d_caption")
                ],
                [
                    InlineKeyboardButton('Back', callback_data = "ghelp"),
                    InlineKeyboardButton('🔒 Close', callback_data = "close")
                ]
            ]
        )
     )
    elif data == "cthumb":
        await query.message.edit_text(
            text=Translation.THUMBNAIL_HELP,
            disable_web_page_preview = True,
            reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton('Back', callback_data = "ghelp"),
                    InlineKeyboardButton("🔒 Close", callback_data = "close")
                ]
            ]
        )
     )
    elif data == "closeme":
        await query.message.delete()
        try:
            await query.message.reply_text(
                text = "<b>Process Cancelled</b>"
     )
        except:
            pass 
    elif data == "ghelp":
        await query.message.edit_text(
            text=Translation.HELP_USER,
            disable_web_page_preview = True,
            reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton('📝ʀᴇɴᴀᴍᴇ', callback_data = "rnme"),
                    InlineKeyboardButton('📂​🇫ɪʟᴇ ᴛᴏ ᴠɪᴅᴇᴏ', callback_data = "f2v")
                ],
                [
                    InlineKeyboardButton('🎞️​🇨​​🇺​​🇸​​🇹​​🇴​​🇲​ ​🇹​​🇭​​🇺​​🇲​​🇧​​🇳​​🇦​​🇮​​🇱', callback_data = "cthumb"),
                    InlineKeyboardButton('📑ᴄᴜ​​🇸ᴛᴏᴍ ᴄᴀᴘᴛɪᴏɴ', callback_data = "ccaption")
                ],
                [
                    InlineKeyboardButton('💬ᴀʙᴏᴜᴛ', callback_data = "about")
                ]
            ]
        )
    )       

    elif data =="shw_caption":
             try:
                caption = await get_caption(query.from_user.id)
                c_text = caption.caption
             except:
                c_text = "​🇸​​🇴​​🇷​​🇷​​🇾​ ​🇧​​🇺​​🇹​ ​🇾​​🇴​​🇺​ ​🇭​​🇦​​🇻​​🇪​​🇳​❜​🇹​ ​🇦​​🇩​​🇩​​🇪​​🇩​ ​🇦​​🇳​​🇾​ ​🇨​​🇦​​🇵​​🇹​​🇮​​🇴​​🇳​ ​🇾​​🇪​​🇹​ ​🇵​​🇱​​🇪​​🇦​​🇸​​🇪​ ​🇸​​🇪​​🇹​ ​🇾​​🇴​​🇺​​🇷​ ​🇨​​🇦​​🇵​​🇹​​🇮​​🇴​​🇳​ ​🇹​​🇭​​🇷​​🇴​​🇺​​🇬​​🇭​ /scaption command" 
             await query.message.edit(
                  text=f"<b>🇾​​🇴​​🇺​​🇷​ ​🇨​​🇺​​🇸​​🇹​​🇴​​🇲​ ​🇨​​🇦​​🇵​​🇹​​🇮​​🇴​​🇳​ :</b> \n\n{c_text} ",
                  parse_mode="html", 
                  disable_web_page_preview=True, 
                  reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton('Back', callback_data = "ccaption"),
                    InlineKeyboardButton("🔒 Close", callback_data = "close")
                ]
            ]
        )
     )
    elif data == "about":
        await query.message.edit_text(
            text=Translation.ABOUT_ME,
            disable_web_page_preview = True,
            reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton('Back', callback_data = "ghelp"),
                    InlineKeyboardButton("🔒 Close", callback_data = "close")
                ]
            ]
        )
     )
    elif data == "d_caption":
        try:
           await del_caption(query.from_user.id)   
        except:
            pass
        await query.message.edit_text(
            text="<b>caption deleted successfully</b>",
            disable_web_page_preview = True,
            reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton('Back', callback_data = "ccaption"),
                    InlineKeyboardButton("🔒 Close", callback_data = "close")
                ]
            ]
        )
     )
    elif data == "close":
        await query.message.delete()
        try:
            await query.message.reply_to_message.delete()
        except:
            pass
