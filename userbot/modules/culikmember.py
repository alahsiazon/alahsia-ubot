# Ported By @VckyouuBitch From Geez - Projects
# Copyright © Team Geez - Project

from telethon.tl import functions
from telethon.tl.functions.messages import GetFullChatRequest
from telethon.errors import (
    ChannelInvalidError,
    ChannelPrivateError,
    ChannelPublicGroupNaError)
from telethon.tl.functions.channels import GetFullChannelRequest

from userbot.events import register
from userbot import CMD_HELP


async def get_chatinfo(event):
    chat = event.pattern_match.group(1)
    chat_info = None
    if chat:
        try:
            chat = int(chat)
        except ValueError:
            pass
    if not chat:
        if event.reply_to_msg_id:
            replied_msg = await event.get_reply_message()
            if replied_msg.fwd_from and replied_msg.fwd_from.channel_id is not None:
                chat = replied_msg.fwd_from.channel_id
        else:
            chat = event.chat_id
    try:
        chat_info = await event.client(GetFullChatRequest(chat))
    except BaseException:
        try:
            chat_info = await event.client(GetFullChannelRequest(chat))
        except ChannelInvalidError:
            await event.reply("`Group/Channelnya Invalid`")
            return None
        except ChannelPrivateError:
            await event.reply("`Ini adalah channel/group private atau tidak akan ter ban di sini.`")
            return None
        except ChannelPublicGroupNaError:
            await event.reply("`Channel Dan Group Besar Tidak Ada`")
            return None
        except (TypeError, ValueError):
            await event.reply("` Group/Channelnya Invalid`")
            return None
    return chat_info


@register(outgoing=True, pattern=r"^\.inviteall(?: |$)(.*)")
async def get_users(event):
    sender = await event.get_sender()
    me = await event.client.get_me()
    if not sender.id == me.id:
        geez = await event.reply("`Proses...`")
    else:
        geez = await event.edit("`Loading...`")
    geezteam = await get_chatinfo(event)
    chat = await event.get_chat()
    if event.is_private:
        return await geez.edit("`Mohon Maaf,Tidak Bisa Menculik Orang Disini.`")
    s = 0
    f = 0
    error = 'None'

    await geez.edit("**TerminalStatus**\n\n`Mencari Orang Buat Di culik.......`")
    async for user in event.client.iter_participants(geezteam.full_chat.id):
        try:
            if error.startswith("Too"):
                return await geez.edit(f"**Telethon Siap **\n(`Akun anda sudah limit mohon ulangi besok lagi sensei`)\n**Error** : \n`{error}`\n\n• Menculik `{s}` Orang \n• Gagal Menculik `{f}` Orang")
            await event.client(functions.channels.InviteToChannelRequest(channel=chat, users=[user.id]))
            s = s + 1
            await geez.edit(f"**Menjalankan Telethon...**\n\n• Menculik `{s}` Orang \n• Gagal Menculik `{f}` Orang\n\n**× LastError:** `{error}`")
        except Exception as e:
            error = str(e)
            f = f + 1
    return await geez.edit(f"**Telethon Siap** \n\n• Sukses Menculik `{s}` Orang \n• Gagal Menculik `{f}` Orang")


CMD_HELP.update({
    "culik":
        "Commander: `.inviteall Ussername Group Target Penculikan`\
          \n📌 : __Menculik Pengguna dari group lain ke group anda__."
})
