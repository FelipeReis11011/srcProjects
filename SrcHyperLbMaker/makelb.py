import requests
import datetime
import csv

def percent(number):
    number = str(number*100)
    if number == 100:
        return "100.00%"
    if number.find(".")==-1:
        number += ".0000"
    if number.find(".")==1:
        number = "0" + number
    if len(number) > 5:
        number = number[:5]
    number += "%"
    return "0" + number

def prettifyTime(tempo):
    minutos=int(tempo/60)
    segundos=tempo-60*minutos
    horas=int(minutos/60)
    minutos=minutos-60*horas
    dias=int(horas/24)
    horas=horas-24*dias
    retorno=""
    if(dias>0):
        retorno+=str(dias)+" day"+("s, " if dias>1 else ", ")
    if(horas>0):
        retorno+=str(horas)+" hour"+("s, " if horas>1 else ", ")
    if(minutos>0):
        retorno+=str(minutos)+" minute"+("s, " if minutos>1 else ", ")
    retorno+=str(segundos)+" seconds"
    return(retorno)

FEDATA = "https://ds.speedrun.com/_fedata/user/runs?"

result = []

with open("data.csv", "w", newline="") as csvOutput:
    output = csv.writer(csvOutput, delimiter = ";")
    output.writerow(['name','id','wrs','wrsIL',
            'wrsFG','runs','runsIL','runsFG',
            'podiums','games','ILs games','full games',
            'categories','categories ILs','categories Full Game','levels played',
            'Games with at least 1 wr','Games with at least 1 podium',
            'Percentage Of Games with at least 1 wr',
            'Personal Bests','Obsolete Runs','Second Places','Third Places',
            'Fourth Places','ratio Wrs/pbs','ratio Wrs/runs','Biggest Run Description',
            'Run Description Size on Average','Sum Of Runs Times in seconds (Very innacurate)',
            'Sum Of Runs Times Edited','platforms played','Runs Emulated'])
    with open("runners.csv", 'r') as csvRunners:
        file = csv.reader(csvRunners)
        for i in file:
            runner = {}
            runner['name'],runner['id']= i
            idd = runner['id']
            strike = 0
            while True:
                try:
                    data = requests.get(f"{FEDATA}userId={idd}&vary=1654385324&ver=4").json()
                    break
                except:
                    strike += 1
                    print(runner['id'])
                    if strike > 5 :
                        print(f"does {runner['name']} deleted their account? [y/n]")
                        if input().lower() in ('yes','y','yeah'):
                            data = False
                            break
            if not data:
                continue
            runner['banned'] = data['user']['powerLevel']==0
            runner['name'] = data['user']['name']
            name = runner['name']
            if data['user']['country']:
                runner['flag'] = ":flag_" + data['user']['country'] + ":"
            else:
                runner['flag'] = ":united_nations:"
            runs = len(data['runs'])
            runner['runs'] = runs
            games = len(data['games'])
            runner['games'] = games
            categories = len(data['categories'])
            runner['categories'] = categories
            if 'levels' in data:
                levels = len(data['levels'])
            else:
                levels = 0
            platforms = len(data['platforms'])
            wrs,wrsIL,wrsFG = [0,0,0]
            runsIL,runsFG,runsEM = [0,0,0]
            podiums,seconds,thirds,fourths = [0,0,0,0]
            PBs,obs = [0,0]
            biggestDescription,allDescription,SumOfTimes = [0,0,0]
            gamesIL,gamesFG,games1Wr,games1Pd = [set(),set(),set(),set()]
            catsIL,catsFG = [set(),set()]
            for run in data['runs']:
                isLevel = 'levelId' in run
                if isLevel:
                    runsIL += 1
                    catsIL.add(run['categoryId'])
                    gamesIL.add(run['gameId'])
                else:
                    runsFG += 1
                    catsFG.add(run['categoryId'])
                    gamesFG.add(run['gameId'])
                try:
                    if 'igt' in run:
                        SumOfTimes += run['igt']
                    elif 'time' in run:
                        SumOfTimes += run['time']
                    else:
                        SumOfTimes += run['timeWithLoads']
                except:
                    print(run)
                if 'comment' in run:
                    comment = len(run['comment'])
                    allDescription += comment
                    if comment > biggestDescription:
                        biggestDescription = comment
                if run['emulator']:
                    runsEM += 1
                if 'place' in run:
                    PBs += 1
                    if run['place'] == 1:
                        wrs += 1
                        if isLevel:
                            wrsIL += 1
                        else:
                            wrsFG += 1
                        games1Wr.add(run['gameId'])
                    if run['place'] in [1,2,3]:
                        podiums += 1
                        games1Pd.add(run['gameId'])
                    if run['place'] == 2:
                        seconds += 1
                    if run['place'] == 3:
                        thirds += 1
                    if run['place'] == 4:
                        fourths += 1
                else:
                    obs += 1
            runner['wrs'] = wrs
            runner['wrsIL'] = wrsIL
            runner['wrsFG'] = wrsFG
            runner['runsIL'] = runsIL
            runner['runsFG'] = runsFG
            runner['podiums'] = podiums
            runner['obs'] = obs
            runner['PBs'] = PBs
            runner['levels'] = levels
            games1Wr = len(games1Wr)
            runner['wrsGames'] = games1Wr
            catsIL = len(catsIL)
            catsFG = len(catsFG)
            gamesIL = len(gamesIL)
            gamesFG = len(gamesFG)
            games1Pd = len(games1Pd)
            descriptionAvg = allDescription/runs
            games1WrPc = percent(games1Wr/games).replace(".",",")
            ratioPbs = percent(wrs/PBs)
            runner['ratio'] = ratioPbs
            ratioRuns = percent(wrs/runs).replace(".",",")
            info = [name,idd,wrs,wrsIL,wrsFG,runs,runsIL,runsFG,
                    podiums,games,gamesIL,gamesFG,categories,
                    catsIL,catsFG,levels,games1Wr,
                    games1Pd,games1WrPc,PBs,obs,seconds,thirds,
                    fourths,ratioPbs,ratioRuns,biggestDescription,
                    descriptionAvg,str(SumOfTimes),prettifyTime(SumOfTimes),
                    platforms,runsEM]
            output.writerow(info)
            result.append(runner)
            print(str(runner) + ',')
result.sort(key=lambda x: x['ratio'], reverse=True)
boards = ['ratio',str(datetime.datetime.now().date())]
for n, i in enumerate(result):
    if i['banned']:
        boards.append(f"{i['flag']}`(Banned User)            {i['ratio']}`")
    else:
        boards.append(f"{i['flag']}`{i['name']} {' ' * (23-len(i['name']))} {i['ratio']}`")
    if n%50 == 49:
        boards.append("")
for lbType in ('wrs','wrsFG','wrsIL','runs','games','categories','runsIL','runsFG','podiums','wrsGames','obs','PBs','levels'):
    result.sort(key=lambda x: x[lbType], reverse=True)
    boards.append(lbType)
    boards.append(str(datetime.datetime.now().date()))
    banned = 0
    position = 0
    lastValue = float('inf')
    for n, i in enumerate(result):
        if i['banned']:
            banned += 1
            boards.append(f"`{'-' * len(str(position))}.`{i['flag']}`(Banned User) {' ' * (10-len(str(n+1)))} {i[lbType]}`")
        else:
            if i[lbType] != lastValue:
                position = n + 1 - banned
            if position > 100:
                break
            lastValue = i[lbType]
            boards.append(f"`{position}.`{i['flag']}`{i['name']} {' ' * (23-len(str(n+1))-len(i['name']))} {i[lbType]}`")
print("\n".join(boards))
with open("backup.txt", 'w') as backup:
    backup.write("\n".join(boards))
result.sort(key=lambda x: x['runs'], reverse=True)
with open("runners.csv", 'w',newline="") as csvRunners:
    writer = csv.writer(csvRunners)
    for i in result:
        writer.writerow([i['name'],i['id']])
