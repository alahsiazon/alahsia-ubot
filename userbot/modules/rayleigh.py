# Lord-Userbot
from time import sleep
from userbot import CMD_HELP, bot
from userbot.events import register
from telethon import events
import asyncio


@bot.on(events.NewMessage(pattern=r"\.(.*)", outgoing=True))
async def _(event):

    if event.fwd_from:

        return

    animation_interval = 0.1

    animation_ttl = range(117)

    input_str = event.pattern_match.group(1)

    if input_str == "bulan":

        await event.edit(input_str)

        animation_chars = [
            "🌗",
            "🌘",
            "🌑",
            "🌒",
            "🌓",
            "🌔",
            "🌕",
            "🌖",
            "🌗",
            "🌘",
            "🌑",
            "🌒",
            "🌓",
            "🌔",
            "🌕",
            "🌖",
            "🌗",
            "🌘",
            "🌑",
            "🌒",
            "🌓",
            "🌔",
            "🌕",
            "🌖",
            "🌗",
            "🌘",
            "🌑",
            "🌒",
            "🌓",
            "🌔",
            "🌕",
            f"🌖"]

        for i in animation_ttl:

            await asyncio.sleep(animation_interval)

            await event.edit(animation_chars[i % 32])


@register(outgoing=True, pattern='^.helikopter(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("▬▬▬.◙.▬▬▬ \n"
                     "═▂▄▄▓▄▄▂ \n"
                     "◢◤ █▀▀████▄▄▄▄◢◤ \n"
                     "█▄ █ █▄ ███▀▀▀▀▀▀▀╬ \n"
                     "◥█████◤ \n"
                     "══╩══╩══ \n"
                     "╬═╬ \n"
                     "╬═╬ \n"
                     "╬═╬ \n"
                     "╬═╬ \n"
                     "╬═╬ \n"
                     "╬═╬ \n"
                     "╬═╬ Hallo Semuanya :) \n"
                     "╬═╬☻/ \n"
                     "╬═╬/▌ \n"
                     "╬═╬/ \\ \n")


@register(outgoing=True, pattern='^.tembak(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("_/﹋\\_\n"
                     "(҂`_´)\n"
                     "<,︻╦╤─ ҉\n"
                     r"_/﹋\_"
                     "\n**Mau Jadi Pacarku Gak?!**")


@register(outgoing=True, pattern='^.bundir(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("`Dadah Semuanya...`          \n　　　　　|"
                     "\n　　　　　| \n"
                     "　　　　　| \n"
                     "　　　　　| \n"
                     "　　　　　| \n"
                     "　　　　　| \n"
                     "　　　　　| \n"
                     "　　　　　| \n"
                     "　／￣￣＼| \n"
                     "＜ ´･ 　　 |＼ \n"
                     "　|　３　 | 丶＼ \n"
                     "＜ 、･　　|　　＼ \n"
                     "　＼＿＿／∪ _ ∪) \n"
                     "　　　　　 Ｕ Ｕ\n")


@register(outgoing=True, pattern='^.awkwok(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("────██──────▀▀▀██\n"
                     "──▄▀█▄▄▄─────▄▀█▄▄▄\n"
                     "▄▀──█▄▄──────█─█▄▄\n"
                     "─▄▄▄▀──▀▄───▄▄▄▀──▀▄\n"
                     "─▀───────▀▀─▀───────▀▀\n`Awkwokwokwok..`")


@register(outgoing=True, pattern='^.ular(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("░░░░▓\n"
                     "░░░▓▓\n"
                     "░░█▓▓█\n"
                     "░██▓▓██\n"
                     "░░██▓▓██\n"
                     "░░░██▓▓██\n"
                     "░░░░██▓▓██\n"
                     "░░░░░██▓▓██\n"
                     "░░░░██▓▓██\n"
                     "░░░██▓▓██\n"
                     "░░██▓▓██\n"
                     "░██▓▓██\n"
                     "░░██▓▓██\n"
                     "░░░██▓▓██\n"
                     "░░░░██▓▓██\n"
                     "░░░░░██▓▓██\n"
                     "░░░░██▓▓██\n"
                     "░░░██▓▓██\n"
                     "░░██▓▓██\n"
                     "░██▓▓██\n"
                     "░░██▓▓██\n"
                     "░░░██▓▓██\n"
                     "░░░░██▓▓██\n"
                     "░░░░░██▓▓██\n"
                     "░░░░██▓▓██\n"
                     "░░░██▓▓██\n"
                     "░░██▓▓██\n"
                     "░██▓▓██\n"
                     "░░██▓▓██\n"
                     "░░░██▓▓██\n"
                     "░░░░██▓▓██\n"
                     "░░░░░██▓▓██\n"
                     "░░░░██▓▓██\n"
                     "░░░██▓▓██\n"
                     "░░██▓▓██\n"
                     "░██▓▓██\n"
                     "░░██▓▓██\n"
                     "░░░██▓▓██\n"
                     "░░░░██▓▓██\n"
                     "░░░░░██▓▓██\n"
                     "░░░░██▓▓██\n"
                     "░░░██▓▓██\n"
                     "░░██▓▓██\n"
                     "░██▓▓██\n"
                     "░░██▓▓██\n"
                     "░░░██▓▓██\n"
                     "░░░░██▓▓██\n"
                     "░░░░░██▓▓██\n"
                     "░░░░██▓▓██\n"
                     "░░░██▓▓██\n"
                     "░░██▓▓██\n"
                     "░██▓▓██\n"
                     "░░██▓▓██\n"
                     "░░░██▓▓██\n"
                     "░░░░██▓▓██\n"
                     "░░░░░██▓▓██\n"
                     "░░░░██▓▓██\n"
                     "░░░██▓▓██\n"
                     "░░██▓▓██\n"
                     "░██▓▓██\n"
                     "░░██▓▓██\n"
                     "░░░██▓▓██\n"
                     "░░░░██▓▓██\n"
                     "░░░░░██▓▓██\n"
                     "░░░░██▓▓██\n"
                     "░░░██▓▓██\n"
                     "░░██▓▓██\n"
                     "░░██▓▓██\n"
                     "░░██▓▓██\n"
                     "░░██▓▓██\n"
                     "░░██▓▓██\n"
                     "░░██▓▓██\n"
                     "░░░██▓▓███\n"
                     "░░░░██▓▓████\n"
                     "░░░░░██▓▓█████\n"
                     "░░░░░░██▓▓██████\n"
                     "░░░░░░███▓▓███████\n"
                     "░░░░░████▓▓████████\n"
                     "░░░░█████▓▓█████████\n"
                     "░░░█████░░░█████●███\n"
                     "░░████░░░░░░░███████\n"
                     "░░███░░░░░░░░░██████\n"
                     "░░██░░░░░░░░░░░████\n"
                     "░░░░░░░░░░░░░░░░███\n"
                     "░░░░░░░░░░░░░░░░░░░\n")


@register(outgoing=True, pattern='^.y(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("‡‡‡‡‡‡‡‡‡‡‡‡▄▄▄▄\n"
                     "‡‡‡‡‡‡‡‡‡‡‡█‡‡‡‡█\n"
                     "‡‡‡‡‡‡‡‡‡‡‡█‡‡‡‡█\n"
                     "‡‡‡‡‡‡‡‡‡‡█‡‡‡‡‡█\n"
                     "‡‡‡‡‡‡‡‡‡█‡‡‡‡‡‡█\n"
                     "██████▄▄█‡‡‡‡‡‡████████▄\n"
                     "▓▓▓▓▓▓█‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡█\n"
                     "▓▓▓▓▓▓█‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡█\n"
                     "▓▓▓▓▓▓█‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡█\n"
                     "▓▓▓▓▓▓█‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡█\n"
                     "▓▓▓▓▓▓█‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡█\n"
                     "▓▓▓▓▓▓█████‡‡‡‡‡‡‡‡‡‡‡‡██\n"
                     "█████‡‡‡‡‡‡‡██████████\n")


@register(outgoing=True, pattern='^.tank(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("█۞███████]▄▄▄▄▄▄▄▄▄▄▃ \n"
                     "▂▄▅█████████▅▄▃▂…\n"
                     "[███████████████████]\n"
                     "◥⊙▲⊙▲⊙▲⊙▲⊙▲⊙▲⊙◤\n")


@register(outgoing=True, pattern='^.babi(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("┈┈┏━╮╭━┓┈╭━━━━╮\n"
                     "┈┈┃┏┗┛┓┃╭┫Ngok ┃\n"
                     "┈┈╰┓▋▋┏╯╯╰━━━━╯\n"
                     "┈╭━┻╮╲┗━━━━╮╭╮┈\n"
                     "┈┃▎▎┃╲╲╲╲╲╲┣━╯┈\n"
                     "┈╰━┳┻▅╯╲╲╲╲┃┈┈┈\n"
                     "┈┈┈╰━┳┓┏┳┓┏╯┈┈┈\n"
                     "┈┈┈┈┈┗┻┛┗┻┛┈┈┈┈\n")


@register(outgoing=True, pattern='^.ajg(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("╥━━━━━━━━╭━━╮━━┳\n"
                     "╢╭╮╭━━━━━┫┃▋▋━▅┣\n"
                     "╢┃╰┫┈┈┈┈┈┃┃┈┈╰┫┣\n"
                     "╢╰━┫┈┈┈┈┈╰╯╰┳━╯┣\n"
                     "╢┊┊┃┏┳┳━━┓┏┳┫┊┊┣\n"
                     "╨━━┗┛┗┛━━┗┛┗┛━━┻\n")


@register(outgoing=True, pattern='^.chill(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**Admin Chill (ง˙o˙)ว**")
    sleep(2)
    await typew.edit("**Owner Cewe**")
    sleep(1)
    await typew.edit("**Om aam**")
    sleep(1)
    await typew.edit("**pedofil**")
    sleep(1)
    await typew.edit("**Anjas Ngentod**")
    sleep(1)
    await typew.edit("**Alvian Cabul**")
    sleep(1)
    await typew.edit("**Nabila ga ada adab**")
    sleep(1)
    await typew.edit("**Jul Ngentod**")
    sleep(1)
    await typew.edit("**Raka Sange**")
    sleep(1)
    await typew.edit("**Amah jelek hehehe**")
    sleep(1)
    await typew.edit("**Shadow Ganteng☠️ **")
    sleep(1)
    await typew.edit("**xixixix**")
    sleep(1)
    await typew.edit("**eh betewe lu semua kontol**")
    sleep(1)
    await typew.edit("**Satu lagi,Otan Ajg**")
    sleep(1)
    await typew.edit("**Hehehe yang liat ini ajg⚡️**")


@bot.on(events.NewMessage(pattern=r"\.(.*)", outgoing=True))
async def _(event):

    if event.fwd_from:

        return

    animation_interval = 0.1

    animation_ttl = range(117)

    input_str = event.pattern_match.group(1)

    if input_str == "sahur":

        await event.edit(input_str)

        animation_chars = [
            "SAHURRRR🙈",
            "SAHUURRR🙉",
            "BANGUNN SAYANGG",
            "YU SAHUR SAHURRR",
            "SAHURRR SAHURRR",
            "YUU SAHURRRR",
            "BANGUN BURUAN IHH ❤️",
            "🙈",
            "🙉",
            "🙈",
            "🙉",
            "🙈",
            "🙉",
            "🙈",
            "🙉",
            "🙈",
            "🙉",
            "BANGUNN YUU SAYANGG",
            "JANGAN LUPA SAHURRR YAAAA",
            "MUAAHHHH",
            "❤️",
            "🖤",
            f"❤️"]

        for i in animation_ttl:

            await asyncio.sleep(animation_interval)

            await event.edit(animation_chars[i % 32])


@register(outgoing=True, pattern='^.titid(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit(
        "⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡤⠖⠲⢄\n"
        "⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡠⠞⠁⠀⠀⠀⠀⢱\n"
        "⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⠎⠀⠀⠀⠀⠀⠀⠀⣸\n"
        "⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣄⠀⠀⠀⠀⢀⡠⠖⠁\n"
        "⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⣿⣿⣿⣿⣿⠁⠀⠀\n"
        "⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣯⣿⣿⣿⣿⣿⠇⠀⠀⠀\n"
        "⠀⠀⠀⠀⠀⠀⠀⠀⠀⡴⣻⣿⣿⣿⣿⣯⠏⠀⠀⠀⠀\n"
        "⠀⠀⠀⠀⠀⠀⠀⣠⠾⣽⣿⣿⣿⣿⣿⠏⠀⠀⠀⠀⠀\n"
        "⠀⠀⠀ ⠀⠀.⣿⣿⣿⣿⣿⣿⣿⠋⠀⠀⠀⠀⠀⠀\n"
        "⠀⠀⠀⠀⣴⣻⣿⣿⣿⣿⣿⣿⡿⠁⠀⠀⠀⠀⠀⠀⠀\n"
        "⠀⠀⣠⢾⣿⣿⣿⣿⣿⣿⡿⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀\n"
        "⠀⣼⣷⣿⣿⣿⣿⣿⣿⣟⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n"
        " ⢸⢿⣿⣿⣿⣿⣿⣿⣿⣯⣻⡟⡆⠀⠀⠀⠀⠀⠀⠀"
        "⠸⣿⣿⣿⣿⣿⣿⣿⣿⣹⣿⡿⡇⠀⠀⠀⠀⠀⠀⠀⠀\n"
        "⠀⠹⣟⣿⣿⣿⣿⡿⣷⡿⣿⡿⠁⠀⠀⠀⠀⠀⠀⠀⠀\n"
        "⠀⠀⠈⠛⠯⣿⡯⠟⠛⠛⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n")


@register(outgoing=True, pattern='^.ily(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("✨ ✨ ✨ ✨ ✨ ✨ ✨ ✨ ✨\n"
                     "✨ ✨ ☁ ☁ ☁ ☁ ☁ ✨ ✨\n"
                     "✨ ✨ ✨ ✨ ☁ ✨ ✨ ✨ ✨\n"
                     "✨ ✨ ✨ ✨ ☁ ✨ ✨ ✨ ✨\n"
                     "✨ ✨ ✨ ✨ ☁ ✨ ✨ ✨ ✨\n"
                     "✨ ✨ ✨ ✨ ☁ ✨ ✨ ✨ ✨\n"
                     "✨ ✨ ✨ ✨ ☁ ✨ ✨ ✨ ✨\n"
                     "✨ ✨ ☁ ☁ ☁ ☁ ☁ ✨ ✨\n"
                     "✨ ✨ ✨ ✨ ✨ ✨ ✨ ✨ ✨\n"
                     "✨ ✨ ✨ ✨ ✨ ✨ ✨ ✨ ✨\n"
                     "✨ ✨ ☁ ☁ ✨ ☁ ☁ ✨ ✨\n"
                     "✨ ☁ ✨ ✨ ☁ ✨ ✨ ☁ ✨\n"
                     "✨ ☁ ✨ ✨ ✨ ✨ ✨ ☁ ✨\n"
                     "✨ ☁ ✨ ✨ ✨ ✨ ✨ ☁ ✨\n"
                     "✨ ✨ ☁ ✨ ✨ ✨ ☁ ✨ ✨\n"
                     "✨ ✨ ✨ ☁ ✨ ☁ ✨ ✨ ✨\n"
                     "✨ ✨ ✨ ✨ ☁ ✨ ✨ ✨ ✨\n"
                     "✨ ✨ ✨ ✨ ✨ ✨ ✨ ✨ ✨\n"
                     "✨ ✨ ✨ ✨ ✨ ✨ ✨ ✨ ✨\n"
                     "✨ ✨ ☁ ✨ ✨ ✨ ☁ ✨ ✨\n"
                     "✨ ✨ ☁ ✨ ✨ ✨ ☁ ✨ ✨\n"
                     "✨ ✨ ☁ ✨ ✨ ✨ ☁ ✨ ✨\n"
                     "✨ ✨ ☁ ✨ ✨ ✨ ☁ ✨ ✨\n"
                     "✨ ✨ ☁ ✨ ✨ ✨ ☁ ✨ ✨\n"
                     "✨ ✨ ☁ ✨ ✨ ✨ ☁ ✨ ✨\n"
                     "✨ ✨ ✨ ☁ ☁ ☁ ✨ ✨ ✨\n"
                     "✨ ✨ ✨ ✨ ✨ ✨ ✨ ✨ ✨\n")


@register(outgoing=True, pattern='^.pakyu(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit(".                       /¯ )\n"
                     "                      /¯  /\n"
                     "                    /    /\n"
                     "              /´¯/'   '/´¯¯`•¸\n"
                     "          /'/   /    /       /¨¯\\ \n"
                     "        ('(   (   (   (  ¯~/'  ')\n"
                     "         \\                        /\n"
                     "          \\                _.•´\n"
                     "            \\              (\n"
                     "              \\  ")


@bot.on(events.NewMessage(pattern=r"\.(.*)", outgoing=True))
async def _(event):

    if event.fwd_from:

        return

    animation_interval = 0.1

    animation_ttl = range(117)

    input_str = event.pattern_match.group(1)

    if input_str == "setan":

        await event.edit(input_str)

        animation_chars = [
            "EHH BUAT LO",
            "IYA TAU GUA IYAAAA",
            "TAU GUA LU GA PUASA",
            "TAPI PEKA LA NGEN😠",
            "HARGAIN GUA YANG PUASA",
            "ASTAGA PEN TAK HIHIIH",
            "SYALAN LOE",
            "😠",
            "😭",
            "😠",
            "😭",
            "AWAS BAE DAH LU YA",
            "BATAL PUAS GUA😡",
            "TABOKIN PALALU☺️",
            "EM",
            "MAKASIH YA SAYANG UDAH PENGERTIAN☺️",
            "OKE GUA PAMIT BICARA",
            "Assalamu'alaikum",
            f"❤️"]

        for i in animation_ttl:

            await asyncio.sleep(animation_interval)

            await event.edit(animation_chars[i % 32])


CMD_HELP.update({
    "sabo":
    "`.bulan` ; `.hati` ; `.sahur` ; `.chill` ; `.titid` ; `.pakyu`\
    \nUsage: liat aja.\
    \n\n`.helikopter` ; `.tank` ; `.tembak`\n`.bundir`\n `.ily\
    \nUsage: liat sendiri\
    \n\n`.y`\
    \nUsage: jempol\
    \n\n`.awkwok`\
    \nUsage: ketawa lari.\
    \n\n`.ular` ; `.babi` ; `.ajg`\
    \nUsage: liat sendiri."
})
