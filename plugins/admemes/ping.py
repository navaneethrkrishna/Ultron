"""Telegram Ping / Pong Speed
Syntax: .ping"""

import time
import random
from pyrogram import Client, filters
from info import COMMAND_HAND_LER
from plugins.helper_functions.cust_p_filters import f_onw_fliter

# -- Constants -- #
ALIVE = "<b>ചത്തിട്ടില്ല മുത്തേ ഇവിടെ തന്നെ ഉണ്ട്.. നിനക്ക് ഇപ്പൊ എന്നോട് ഒരു സ്നേഹവും ഇല്ല. കൊള്ളാം.. നീ പാഴെ പോലെയേ അല്ല മാറിപോയി..😔 ഇടക്ക് എങ്കിലും ചുമ്മാ ഒന്ന് Start ചെയ്തു നോക്ക്..🙂</b>" 
HELP = "<b>Help ഒന്നും ഇല്ല ഓടിക്കോ......</b>"
REPO = "<b>⪼ 𝚁𝙴𝙿𝙾 ›› <a href='https://github.com/Aadhi000/Ajax'>𝙰𝙳𝚅-𝙰𝙹𝙰𝚇</a></b>"
CHANNEL = "<b>⪼ 𝙲𝙻𝙸𝙲𝙺 𝙷𝙴𝚁𝙴 ›› <a href='https://t.me/+veUIdIW2CQ5mOGU5'>𝙼𝚆-𝚄𝙿𝙳𝙰𝚃𝙴𝚂</a></b>"
GROUP = "<b><b>⪼ 𝙲𝙻𝙸𝙲𝙺 𝙷𝙴𝚁𝙴 ›› <a href='https://t.me/+EqhXLhL3T1w4Zjc1'>𝙼𝙾𝚅𝙸𝙴𝚂 𝚆𝙾𝚁𝙻𝙳</a></b></b>"
OWNER = "<b>╭━━━━━━━━━━━━━━━➣</b>\n<b>┣⪼ 𝙼𝚈 𝙽𝙰𝙼𝙴 ›› <a href='https://t.me/Devil0Bot_Bot'>𝙰𝙹𝙰𝚇</a></b>\n<b>┣⪼ 𝙲𝚁𝙴𝙰𝚃𝙾𝚁 ›› <a href='https://t.me/Aadhi011/'>ꪖꪖᦔꫝỉ </a></b>\n<b>┣⪼ 𝚂𝙾𝚄𝚁𝙲𝙴 𝙲𝙾𝙳𝙴 ›› <a href='https://github.com/Aadhi000/Ajax'>𝙰𝙳𝚅-𝙰𝙹𝙰𝚇</a></b>\n<b>┣⪼ 𝙳𝙰𝚃𝙰𝙱𝙰𝚂𝙴 ›› 𝙼𝙾𝙽𝙶𝙾 𝙳𝙱</b>\n<b>┣⪼ 𝙻𝙸𝙱𝚁𝙰𝚁𝚈 ›› 𝙿𝚈𝚁𝙾𝙶𝚁𝙰𝙼</b>\n<b>┣⪼ 𝙻𝙰𝙽𝙶𝚄𝙰𝙶𝙴 ›› 𝙿𝚈𝚃𝙷𝙾𝙽</b>\n<b>╰━━━━━━━━━━━━━━━➣</b>"
AJAX = "<b>╭━━━━━━━━━━━━━━━➣</b>\n<b>┣⪼ 𝙼𝚈 𝙽𝙰𝙼𝙴 ›› <a href='https://t.me/Devil0Bot_Bot'>𝙰𝙹𝙰𝚇</a></b>\n<b>┣⪼ 𝙲𝚁𝙴𝙰𝚃𝙾𝚁 ›› <a href='https://t.me/Aadhi011/'>ꪖꪖᦔꫝỉ </a></b>\n<b>┣⪼ 𝚂𝙾𝚄𝚁𝙲𝙴 𝙲𝙾𝙳𝙴 ›› <a href='https://github.com/Aadhi000/Ajax'>𝙰𝙳𝚅-𝙰𝙹𝙰𝚇</a></b>\n<b>┣⪼ 𝙳𝙰𝚃𝙰𝙱𝙰𝚂𝙴 ›› 𝙼𝙾𝙽𝙶𝙾 𝙳𝙱</b>\n<b>┣⪼ 𝙻𝙸𝙱𝚁𝙰𝚁𝚈 ›› 𝙿𝚈𝚁𝙾𝙶𝚁𝙰𝙼</b>\n<b>┣⪼ 𝙻𝙰𝙽𝙶𝚄𝙰𝙶𝙴 ›› 𝙿𝚈𝚃𝙷𝙾𝙽</b>\n<b>╰━━━━━━━━━━━━━━━➣</b>"
# -- Constants End -- #


@Client.on_message(filters.command("alive", COMMAND_HAND_LER) & f_onw_fliter)
async def check_alive(_, message):
    await message.reply_text(ALIVE)


@Client.on_message(filters.command("help", COMMAND_HAND_LER) & f_onw_fliter)
async def help_me(_, message):
    await message.reply_text(HELP)


@Client.on_message(filters.command("ping", COMMAND_HAND_LER) & f_onw_fliter)
async def ping(_, message):
    start_t = time.time()
    rm = await message.reply_text("...")
    end_t = time.time()
    time_taken_s = (end_t - start_t) * 1000
    await rm.edit(f"Pong!\n{time_taken_s:.3f} ms")


@Client.on_message(filters.command("channel", COMMAND_HAND_LER) & f_onw_fliter)
async def repo(_, message):
    await message.reply_text(REPO)


@Client.on_message(filters.command("help", COMMAND_HAND_LER) & f_onw_fliter)
async def help_me(_, message):
    await message.reply_text(CHANNEL)


@Client.on_message(filters.command("group", COMMAND_HAND_LER) & f_onw_fliter)
async def help_me(_, message):
    await message.reply_text(GROUP)


@Client.on_message(filters.command("owner", COMMAND_HAND_LER) & f_onw_fliter)
async def help_me(_, message):
    await message.reply_text(OWNER)


@Client.on_message(filters.command("ajax", COMMAND_HAND_LER) & f_onw_fliter)
async def help_me(_, message):
    await message.reply_text(ajax)
