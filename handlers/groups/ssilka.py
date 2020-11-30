from aiogram import types
from loader import dp
import datetime
import bisect

links = [
    [
        [
            ('Физика лаб', ('https://us04web.zoom.us/j/73839263141?pwd=a1duMEpodU5XNSsybUFQanVKRkhtQT09', 'хз')),
            ('ВМ прак', 'https://docs.google.com/spreadsheets/d/1ClZwAO3EFZHMYTFIR3jSQi1Bg-yCuH2FoV_aXysS1I4/edit#gid=1055486101'),
            ('Физика лек', 'https://www.google.com/url?q=https://teams.microsoft.com/l/meetup-join/19%253ameeting_MGFiMDA0NTItY2VmNy00OGQ4LTgwOTgtMDk4NzJjOGVhYTAx%2540thread.v2/0?context%3D%257b%2522Tid%2522%253a%25229c36211b-3bd9-4edf-b8be-570d715f6de5%2522%252c%2522Oid%2522%253a%25229f5aba2e-6edc-4e63-b5a7-13fcc4db0daa%2522%257d&sa=D&source=calendar&usd=2&usg=AOvVaw1dYv1bRvM4t1Ikkiad1aWU\n(ну или https://classroom.google.com/c/MTQ1NjIxMTEwNTYy?cjc=v6ekesl)'),
            ('English', 'https://meet.google.com/dot-xnwc-csr'),
        ],
        [
            ('', ''),
            ('АСД лаб', ('https://teams.microsoft.com/l/meetup-join/19%3Ad5119507f5ae4485bfc288df012ab877%40thread.tacv2/1600673043344?context=%7B%22Tid%22%3A%22d595e6a1-b90f-4cc6-b12b-1db7f331d222%22%2C%22Oid%22%3A%22aaa7729f-5f32-4c2a-b228-795e6c3fcb15%22%7D', 'https://us04web.zoom.us/j/76237910629?pwd=VFdVL01NVG96NFhUdzVWZit2bEswQT09')),
            ('ОП прак', 'https://meet.google.com/tpf-vmzj-hga'),
            ('КДМ лек', 'https://us04web.zoom.us/j/78393633524?pwd=b0RzUndZUjdsR2MxLzZuQm1pVEMrUT09'),
        ],
        [
            ('', ''),
            ('', ''),
            ('ОП лек', 'https://meet.google.com/tpf-vmzj-hga'),
            ('ОП лаб', ('http://meet.google.com/tpf-vmzj-hga', 'https://teams.microsoft.com/l/meetup-join/19%3Ameeting_YWJhMjVmNjctYTY3Yy00ZDYxLTg4ZjgtZWViZmRiZjkwNWYz%40thread.v2/0?context=%7B%22Tid%22%3A%22b41b72d0-4e9f-4c26-8a69-f949f367c91d%22%2C%22Oid%22%3A%22a57dd3d1-1879-4337-a3fc-7115a2aa8bec%22%7D')),
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
            ('ВМ прак', 'https://docs.google.com/spreadsheets/d/1ClZwAO3EFZHMYTFIR3jSQi1Bg-yCuH2FoV_aXysS1I4/edit#gid=1055486101'),
            ('ВМ лек', 'https://www.youtube.com/'),
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
    [  # second week
        [
            ('', ''),
            ('', ''),
            ('Физика лек', 'https://www.google.com/url?q=https://teams.microsoft.com/l/meetup-join/19%253ameeting_MGFiMDA0NTItY2VmNy00OGQ4LTgwOTgtMDk4NzJjOGVhYTAx%2540thread.v2/0?context%3D%257b%2522Tid%2522%253a%25229c36211b-3bd9-4edf-b8be-570d715f6de5%2522%252c%2522Oid%2522%253a%25229f5aba2e-6edc-4e63-b5a7-13fcc4db0daa%2522%257d&sa=D&source=calendar&usd=2&usg=AOvVaw1dYv1bRvM4t1Ikkiad1aWU\n(ну или https://classroom.google.com/c/MTQ1NjIxMTEwNTYy?cjc=v6ekesl)'),
            ('English', 'https://meet.google.com/dot-xnwc-csr'),
        ],
        [
            ('', ''),
            ('АСД лаб', ('https://teams.microsoft.com/l/meetup-join/19%3Ad5119507f5ae4485bfc288df012ab877%40thread.tacv2/1600673043344?context=%7B%22Tid%22%3A%22d595e6a1-b90f-4cc6-b12b-1db7f331d222%22%2C%22Oid%22%3A%22aaa7729f-5f32-4c2a-b228-795e6c3fcb15%22%7D', 'https://us04web.zoom.us/j/76237910629?pwd=VFdVL01NVG96NFhUdzVWZit2bEswQT09')),
            ('', ''),
            ('КДМ лек', 'https://us04web.zoom.us/j/78393633524?pwd=b0RzUndZUjdsR2MxLzZuQm1pVEMrUT09'),
        ],
        [
            ('', ''),
            ('', ''),
            ('ОП лек', 'https://meet.google.com/tpf-vmzj-hga'),
            ('ОП лаб', ('http://meet.google.com/tpf-vmzj-hga', 'https://teams.microsoft.com/l/meetup-join/19%3Ameeting_YWJhMjVmNjctYTY3Yy00ZDYxLTg4ZjgtZWViZmRiZjkwNWYz%40thread.v2/0?context=%7B%22Tid%22%3A%22b41b72d0-4e9f-4c26-8a69-f949f367c91d%22%2C%22Oid%22%3A%22a57dd3d1-1879-4337-a3fc-7115a2aa8bec%22%7D')),
        ],
        [
            ('', ''),
            ('АСД лек', 'https://teams.microsoft.com/l/meetup-join/19%3ad5119507f5ae4485bfc288df012ab877%40thread.tacv2/1600354265198?context=%7b%22Tid%22%3a%22d595e6a1-b90f-4cc6-b12b-1db7f331d222%22%2c%22Oid%22%3a%22aaa7729f-5f32-4c2a-b228-795e6c3fcb15%22%7d'),
            ('ВМ лек', 'https://www.youtube.com/'),
            ('КДМ прак', 'https://us04web.zoom.us/j/2103234416?pwd=Mzc2OE16RHF6N2tUSGVsVEhaNlVRZz09'),
        ],
        [
            ('', ''),
            ('ВМ прак', 'https://docs.google.com/spreadsheets/d/1ClZwAO3EFZHMYTFIR3jSQi1Bg-yCuH2FoV_aXysS1I4/edit#gid=1055486101'),
            ('ВМ лек', 'https://www.youtube.com/'),
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
