from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup 


Menu = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="🌎 Menu", callback_data="Menu"),
            InlineKeyboardButton(text="⬅️ Ortga", callback_data="1ortga"),
        ],
    ],row_width=True
)

menu = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="📜 About", callback_data="about"),
            InlineKeyboardButton(text="📊 Kurslar", callback_data="kurslar"),
        ],
        [
            InlineKeyboardButton(text="👨‍💻 Xodimlar", callback_data="xodimlar"),
            InlineKeyboardButton(text="🧾 Vakansiya", callback_data="vakansiya"),
        ],
        [
            InlineKeyboardButton(text="📞 Bog'lanish uchun", url="https://t.me/tramplin_uz" ),
        ],
        [
            InlineKeyboardButton(text="⬅️ Ortga", callback_data="menuortga"),
        ],
    ],row_width=True
)

aboutmenu = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="🎦 Video", url="https://youtube.com/shorts/qsHai1S7wKg?si=GnAz1KR9ukhCDiNB"),
            InlineKeyboardButton(text="⬅️ Ortga", callback_data="aboutortga"),
        ],
    ],row_width=True
)

kurslarmenu =InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="📘 Front-End",callback_data="frontend"),
            InlineKeyboardButton(text="📕 Back-End", callback_data="backend"),
        ],
        [
            InlineKeyboardButton(text="📙 Cyber-Security",callback_data="kibr"),
            InlineKeyboardButton(text="📗 Graphic",callback_data="grafik"),
        ],
        [
            InlineKeyboardButton(text="⬅️ Ortga", callback_data="kurslarortga"),
        ],
    ],row_width=True
)

informatsiya = InlineKeyboardMarkup(
    inline_keyboard = [
        [
            InlineKeyboardButton(text="⤴️ Ortga", callback_data='2ortga')
        ]
    ]
)

anketa1 = InlineKeyboardMarkup(
    inline_keyboard = [
        [
            InlineKeyboardButton(text="⤴️ Ortga", callback_data='3ortga')
        ]
    ]
)

kurslar1= InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="✍️ Kurslarga yozilish", callback_data="anketa"),
            InlineKeyboardButton(text="⬅️ Ortga", callback_data="ortga2"),
        ],
    ],)


xodimlarmenu = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="👤 Otajon Bozorboyev", callback_data="otajon"),
            InlineKeyboardButton(text="👤 Isroilov Rustamjon", callback_data="rustamjon"),
        ],
        # [
        #     InlineKeyboardButton(text="👤 Xalilov Xusan", callback_data="xusan"),
        # ],
        # [
        #     InlineKeyboardButton(text="👤 Otabek", callback_data="otabek"),
        #     InlineKeyboardButton(text="👤 Xurshid", callback_data="xurshid"),
        # ],
        # [
        #     InlineKeyboardButton(text="👤 Miraziz Dev", callback_data="miraziz"),
        # ],
        [
            InlineKeyboardButton(text="⬅️ Ortga", callback_data="xodimlarortga"),
        ],
    ],
)

otajon =InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="⬅️ Ortga", callback_data="otajonortga"),
            InlineKeyboardButton(text="🔗 Link", url="https://t.me/otajonbozorboyev"),
        ],
    ],row_width=True
)

rustam = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="⬅️ Ortga", callback_data="rustamortga"),
            InlineKeyboardButton(text="🔗 Link",url="https://youtube.com"),
        ],
    ],row_width=True
)