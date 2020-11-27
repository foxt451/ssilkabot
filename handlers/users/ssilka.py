from aiogram import types
from loader import dp
import datetime
import bisect

links = [
    [
        [
            ('', ''),
            ('', ''),
            ('', ''),
            ('', ''),
        ],
        [
            ('', ''),
            ('', ''),
            ('', ''),
            ('', ''),
        ],
        [
            ('', ''),
            ('', ''),
            ('', ''),
            ('', ''),
        ],
        [
            ('', ''),
            ('АСД лек',
             'https://teams.microsoft.com/l/meetup-join/19%3ad5119507f5ae4485bfc288df012ab877%40thread.tacv2/1600354265198?context=%7b%22Tid%22%3a%22d595e6a1-b90f-4cc6-b12b-1db7f331d222%22%2c%22Oid%22%3a%22aaa7729f-5f32-4c2a-b228-795e6c3fcb15%22%7d'),
            ('', ''),
            ('КДМ прак', 'https://us04web.zoom.us/j/2103234416?pwd=Mzc2OE16RHF6N2tUSGVsVEhaNlVRZz09'),
        ],
        [
            ('', ''),
            ('', ''),
            ('', ''),
            ('', ''),
        ],
        [
            ('', ''),
            ('', ''),
            ('', ''),
            ('', ''),
        ],
        [
            ('', ''),
            ('', ''),
            ('', ''),
            ('', ''),
        ],
    ],
    [
        [
            ('', ''),
            ('', ''),
            ('', ''),
            ('', ''),
        ],
        [
            ('', ''),
            ('', ''),
            ('', ''),
            ('', ''),
        ],
        [
            ('', ''),
            ('', ''),
            ('', ''),
            ('', ''),
        ],
        [
            ('', ''),
            ('', ''),
            ('', ''),
            ('', ''),
        ],
        [
            ('', ''),
            ('', ''),
            ('', ''),
            ('', ''),
        ],
        [
            ('', ''),
            ('', ''),
            ('', ''),
            ('', ''),
        ],
        [
            ('', ''),
            ('', ''),
            ('', ''),
            ('', ''),
        ],
    ]
]
check_date = datetime.date(2020, 11, 23)

timings = [
    '08-30', '10-05',
    '10-25', '12-00',
    '12-20', '13-55',
    '14-15', '15-50',
]


@dp.message_handler(commands=['ssilka'])
async def bot_echo(message: types.Message):
    time_cur = datetime.datetime.now()
    today = time_cur.date()
    week_number = ((today - check_date).days % 14) // 7
    weekday = today.weekday()
    time_formatted = time_cur.strftime("%H-%M")
    pair = bisect.bisect_left(timings, time_formatted) // 2
    if pair > 3:
        await message.answer('Отдыхаем')
    else:
        link = links[week_number][weekday][pair]
        if not isinstance(link[1], tuple):
            await message.answer(f'{link[0]}\n{link[1]}' if link[0] else 'Отдыхаем')
        else:
            await message.answer(f'{link[0]}\n1 группа\n{link[1][0]}\n2 группа\n{link[1][1]}' if link[0] else 'Отдыхаем')
