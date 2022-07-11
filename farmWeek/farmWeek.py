import requests

runners = [
{'name': '4d9r', 'id': 'x35yq46j', 'runs': {'initial': {'verified': 634, 'rejected': 14, 'new': 243, 'total': 877}, 'today': {'verified': 648, 'rejected': 15, 'new': 242, 'total': 890}, 'total': 13, 'yesterday': {'verified': 636, 'rejected': 15, 'new': 243, 'total': 879}}},
{'name': 'zir0nic', 'id': '98rv0dqj', 'runs': {'initial': {'verified': 998, 'rejected': 36, 'new': 1, 'total': 999}, 'today': {'verified': 1007, 'rejected': 36, 'new': 6, 'total': 1013}, 'total': 14, 'yesterday': {'verified': 1002, 'rejected': 36, 'new': 6, 'total': 1008}}},
{'name': 'stathx', 'id': 'jn36q61x', 'runs': {'initial': {'verified': 1439, 'rejected': 21, 'new': 0, 'total': 1439}, 'today': {'verified': 1705, 'rejected': 22, 'new': 0, 'total': 1705}, 'total': 266, 'yesterday': {'verified': 1705, 'rejected': 22, 'new': 0, 'total': 1705}}},
{'name': 'Astrolite', 'id': 'j0n55mr8', 'runs': {'initial': {'verified': 1205, 'rejected': 162, 'new': 86, 'total': 1291}, 'today': {'verified': 1230, 'rejected': 175, 'new': 1274, 'total': 2504}, 'total': 1213, 'yesterday': {'verified': 1219, 'rejected': 171, 'new': 538, 'total': 1757}}},
{'name': 'Otterstone_Gamer', 'id': 'qjn1wzw8', 'runs': {'initial': {'verified': 8240, 'rejected': 454, 'new': 615, 'total': 8855}, 'today': {'verified': 8416, 'rejected': 455, 'new': 1234, 'total': 9650}, 'total': 795, 'yesterday': {'verified': 8324, 'rejected': 455, 'new': 1276, 'total': 9600}}},
{'name': 'felipereis11011', 'id': 'x7q9g1v8', 'runs': {'initial': {'verified': 1216, 'rejected': 1, 'new': 0, 'total': 1216}, 'today': {'verified': 1217, 'rejected': 2, 'new': 0, 'total': 1217}, 'total': 1, 'yesterday': {'verified': 1216, 'rejected': 1, 'new': 0, 'total': 1216}}},
{'name': 'felipenascimento83', 'id': '68wne448', 'runs': {'initial': {'verified': 2019, 'rejected': 0, 'new': 3, 'total': 2022}, 'today': {'verified': 2129, 'rejected': 1, 'new': 7, 'total': 2136}, 'total': 114, 'yesterday': {'verified': 2091, 'rejected': 0, 'new': 16, 'total': 2107}}},
{'name': 'JDMI', 'id': 'j92266v8', 'runs': {'initial': {'verified': 997, 'rejected': 18, 'new': 0, 'total': 997}, 'today': {'verified': 1052, 'rejected': 18, 'new': 0, 'total': 1052}, 'total': 55, 'yesterday': {'verified': 1052, 'rejected': 18, 'new': 0, 'total': 1052}}},
{'name': 'ComicBlue', 'id': '68wvldlx', 'runs': {'initial': {'verified': 2356, 'rejected': 59, 'new': 3, 'total': 2359}, 'today': {'verified': 2664, 'rejected': 59, 'new': 23, 'total': 2687}, 'total': 328, 'yesterday': {'verified': 2631, 'rejected': 59, 'new': 18, 'total': 2649}}},
{'name': 'reni', 'id': '8l0rl9v8', 'runs': {'initial': {'verified': 1540, 'rejected': 2, 'new': 0, 'total': 1540}, 'today': {'verified': 1557, 'rejected': 2, 'new': 64, 'total': 1621}, 'total': 81, 'yesterday': {'verified': 1555, 'rejected': 2, 'new': 64, 'total': 1619}}},
{'name': 'Kkntucara', 'id': 'xz9nv648', 'runs': {'initial': {'verified': 1379, 'rejected': 52, 'new': 12, 'total': 1391}, 'today': {'verified': 1388, 'rejected': 52, 'new': 31, 'total': 1419}, 'total': 28, 'yesterday': {'verified': 1379, 'rejected': 52, 'new': 21, 'total': 1400}}},
{'name': 'VyPr', 'id': '8e913qdj', 'runs': {'initial': {'verified': 1634, 'rejected': 2, 'new': 22, 'total': 1656}, 'today': {'verified': 1716, 'rejected': 0, 'new': 40, 'total': 1756}, 'total': 100, 'yesterday': {'verified': 1698, 'rejected': 0, 'new': 36, 'total': 1734}}},
{'name': 'killerkun...', 'id': '8qr5kvwj', 'runs': {'initial': {'verified': 1978, 'rejected': 0, 'new': 6, 'total': 1984}, 'today': {'verified': 2348, 'rejected': 0, 'new': 374, 'total': 2722}, 'total': 738, 'yesterday': {'verified': 2245, 'rejected': 0, 'new': 390, 'total': 2635}}},
{'name': 'Toxcien', 'id': 'jn36qqqx', 'runs': {'initial': {'verified': 430, 'rejected': 4, 'new': 1, 'total': 431}, 'today': {'verified': 661, 'rejected': 4, 'new': 123, 'total': 784}, 'total': 353, 'yesterday': {'verified': 592, 'rejected': 4, 'new': 119, 'total': 711}}},
{'name': 'JeelSpeed', 'id': 'jpre35y8', 'runs': {'initial': {'verified': 893, 'rejected': 24, 'new': 23, 'total': 916}, 'today': {'verified': 978, 'rejected': 25, 'new': 69, 'total': 1047}, 'total': 131, 'yesterday': {'verified': 977, 'rejected': 25, 'new': 70, 'total': 1047}}},
{'name': 'AslanTZ', 'id': '816q54lx', 'runs': {'initial': {'verified': 1447, 'rejected': 24, 'new': 0, 'total': 1447}, 'today': {'verified': 1489, 'rejected': 24, 'new': 0, 'total': 1489}, 'total': 42, 'yesterday': {'verified': 1484, 'rejected': 24, 'new': 5, 'total': 1489}}},
{'name': 'Elims', 'id': 'qjoqz4e8', 'runs': {'initial': {'verified': 1282, 'rejected': 86, 'new': 1, 'total': 1283}, 'today': {'verified': 1284, 'rejected': 86, 'new': 122, 'total': 1406}, 'total': 123, 'yesterday': {'verified': 1283, 'rejected': 86, 'new': 100, 'total': 1383}}},
{'name': 'Merl_', 'id': 'jn39e4dx', 'runs': {'initial': {'verified': 248, 'rejected': 1, 'new': 0, 'total': 248}, 'today': {'verified': 249, 'rejected': 1, 'new': 2, 'total': 251}, 'total': 3, 'yesterday': {'verified': 248, 'rejected': 1, 'new': 2, 'total': 250}}},
{'name': 'Walgrey', 'id': '8ge6w47j', 'runs': {'initial': {'verified': 661, 'rejected': 2, 'new': 0, 'total': 661}, 'today': {'verified': 682, 'rejected': 2, 'new': 0, 'total': 682}, 'total': 21, 'yesterday': {'verified': 664, 'rejected': 2, 'new': 0, 'total': 664}}},
{'name': 'hahhah42', 'id': 'jmoqknn8', 'runs': {'initial': {'verified': 285, 'rejected': 1, 'new': 0, 'total': 285}, 'today': {'verified': 315, 'rejected': 1, 'new': 2, 'total': 317}, 'total': 32, 'yesterday': {'verified': 315, 'rejected': 1, 'new': 2, 'total': 317}}},
{'name': 'Zambrini', 'id': '1xyylnyx', 'runs': {'initial': {'verified': 1670, 'rejected': 8, 'new': 20, 'total': 1690}, 'today': {'verified': 1981, 'rejected': 8, 'new': 12, 'total': 1993}, 'total': 303, 'yesterday': {'verified': 1925, 'rejected': 8, 'new': 14, 'total': 1939}}},
{'name': 'Kkspeed', 'id': 'xz7m6knj', 'runs': {'initial': {'verified': 157, 'rejected': 17, 'new': 32, 'total': 189}, 'today': {'verified': 186, 'rejected': 34, 'new': 103, 'total': 289}, 'total': 100, 'yesterday': {'verified': 180, 'rejected': 32, 'new': 102, 'total': 282}}},
{'name': 'Ivory', 'id': 'v8lqkv7x', 'runs': {'initial': {'verified': 38, 'rejected': 31, 'new': 1, 'total': 39}, 'today': {'verified': 38, 'rejected': 31, 'new': 1, 'total': 39}, 'total': 0, 'yesterday': {'verified': 38, 'rejected': 31, 'new': 1, 'total': 39}}},
{'name': 'Bob-chicken', 'id': 'x7q6qy08', 'runs': {'initial': {'verified': 380, 'rejected': 28, 'new': 1, 'total': 381}, 'today': {'verified': 380, 'rejected': 28, 'new': 1, 'total': 381}, 'total': 0, 'yesterday': {'verified': 380, 'rejected': 28, 'new': 1, 'total': 381}}},
{'name': 'wrap', 'id': 'xz79gdej', 'runs': {'initial': {'verified': 81, 'rejected': 10, 'new': 0, 'total': 81}, 'today': {'verified': 119, 'rejected': 10, 'new': 54, 'total': 173}, 'total': 92, 'yesterday': {'verified': 119, 'rejected': 10, 'new': 54, 'total': 173}}},
{'name': 'Act7', 'id': 'j51p0268', 'runs': {'initial': {'verified': 856, 'rejected': 100, 'new': 8, 'total': 864}, 'today': {'verified': 917, 'rejected': 101, 'new': 49, 'total': 966}, 'total': 102, 'yesterday': {'verified': 884, 'rejected': 101, 'new': 25, 'total': 909}}},
{'name': 'Fioresa', 'id': '1xy3wpwj', 'runs': {'initial': {'verified': 5269, 'rejected': 16, 'new': 58, 'total': 5327}, 'today': {'verified': 5345, 'rejected': 16, 'new': 57, 'total': 5402}, 'total': 75, 'yesterday': {'verified': 5345, 'rejected': 16, 'new': 57, 'total': 5402}}},
{'name': 'TRlittleToaster', 'id': '8qzo95o8', 'runs': {'initial': {'verified': 1971, 'rejected': 1, 'new': 10, 'total': 1981}, 'today': {'verified': 2032, 'rejected': 1, 'new': 11, 'total': 2043}, 'total': 62, 'yesterday': {'verified': 2006, 'rejected': 1, 'new': 30, 'total': 2036}}},
{'name': 'daff', 'id': '8grm677x', 'runs': {'initial': {'verified': 3508, 'rejected': 45, 'new': 57, 'total': 3565}, 'today': {'verified': 3680, 'rejected': 45, 'new': 1, 'total': 3681}, 'total': 116, 'yesterday': {'verified': 3603, 'rejected': 45, 'new': 1, 'total': 3604}}},
{'name': 'Slothboy78YT', 'id': '8grk0zyx', 'runs': {'initial': {'verified': 152, 'rejected': 35, 'new': 62, 'total': 214}, 'today': {'verified': 194, 'rejected': 40, 'new': 41, 'total': 235}, 'total': 21, 'yesterday': {'verified': 185, 'rejected': 36, 'new': 39, 'total': 224}}},
{'name': 'jackzfiml', 'id': '8ge265yj', 'runs': {'initial': {'verified': 463, 'rejected': 3, 'new': 0, 'total': 463}, 'today': {'verified': 464, 'rejected': 3, 'new': 0, 'total': 464}, 'total': 1, 'yesterday': {'verified': 464, 'rejected': 3, 'new': 0, 'total': 464}}},
{'name': 'shinboy', 'id': '8wl7yovj', 'runs': {'initial': {'verified': 1736, 'rejected': 0, 'new': 0, 'total': 1736}, 'today': {'verified': 1915, 'rejected': 0, 'new': 0, 'total': 1915}, 'total': 179, 'yesterday': {'verified': 1848, 'rejected': 0, 'new': 0, 'total': 1848}}},
]

API = "https://www.speedrun.com/api/v1/"

def getRuns(runner,status):
    offset = 0
    while True:
        data = requests.get(
            f"{API}runs?user={runner['id']}&max=200&offset={offset * 200}&status={status}"
        ).json()
        offset += 1
        if data["pagination"]["size"] < 200:
            break
    return data["pagination"]["offset"] + data["pagination"]["size"]

print('[')

for runner in runners:
    runner['runs']['today']['total'] = runner['runs']['today']['verified'] + runner['runs']['today']['new']
    runner['runs']['yesterday'] = runner['runs']['today'].copy()
    for status in runner['runs']['today']:
        if status == 'total':
            continue
        runner['runs']['today'][status] = getRuns(runner,status)
    runner['runs']['initial']['total'] = runner['runs']['initial']['verified'] + runner['runs']['initial']['new']
    runner['runs']['today']['total'] = runner['runs']['today']['verified'] + runner['runs']['today']['new']
    runner['runs']['total'] = runner['runs']['today']['total'] - runner['runs']['initial']['total']
    print(str(runner))
print(']')

text0 = ''

print('today total')
for runner in runners:
    print(runner['runs']['today']['total'])
    text0 += str(runner['runs']['today']['total'] - runner['runs']['yesterday']['total']) + '\n'

print('today now')
print(text0)

import datetime

runners.sort(key=lambda x: x['runs']['total'], reverse=True)

print('runs')

position = 0
lastValue = float('inf')
text0 = ''
text1 = ''
text2 = ''
for n, i in enumerate(runners):
    if i['runs']['total'] != lastValue:
        position = n+1
    lastValue = i['runs']['total']
    print(f"`{position}.{i['name']} {' ' * (23-len(str(n+1))-len(i['name']))} {i['runs']['total']}`")
    text0 += f"#{position}\n"
    text1 += f"{i['name']}\n"
    text2 += f"{i['runs']['total']}\n"
print(text0)
print(text1)
print(text2)
