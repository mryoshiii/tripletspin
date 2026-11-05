import requests
import json
import telebot

token = "_no_" # PUT LATER IN .ENV FILE
bot = telebot.TeleBot(token)


nextRank = "TEMPLATE"
numberwins = "TEMPLATE"
latestgame_1 = "hewwo"
latestgame_2 = "i fix this later"
latestgame_3 = "okk byyeee :333" # я точно это сделаю!!!
username = "mryoshii"

startupMessage = "Привет! Для проверки статистики напиши свой никнейм"

# блин у меня ж тогда фикс на mind electric был аыхвахывах
def getUsersStats(username): # SOME-ONE HELP ME. Understand what's going on, inside my mind. Doctor, i can't tell if i'm me?
    global gamesplayed, gameswon, winrate, glicko, rd, tetrarating, rank, bestrank, standing, apm, pps, vs, flag, regDate, level, xp, playtime, xpZen, levelZen, fortylines, blitz
    link = "https://ch.tetr.io/api/users/" + username
    headers = { 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36' }

    respSummary = requests.get(url = link, headers = headers)
    dataSummary = respSummary.json()
    userSummary = dataSummary.get("data", {})

    respLeague = requests.get(url = link + "/summaries/league", headers = headers)
    dataLeague = respLeague.json()
    userLeague = dataLeague.get("data", {})

    respFortyLines = requests.get(url = link + "/summaries/40l", headers = headers)
    dataFortyLines = respFortyLines.json()
    userFortyLines = dataFortyLines.get("data", {})

    respBlitz = requests.get(url = link + "/summaries/blitz", headers = headers)
    dataBlitz = respBlitz.json()
    userBlitz = dataBlitz.get("data", {})

    respZen = requests.get(url = link + "/summaries/zen", headers = headers)
    dataZen = respZen.json()
    userZen = dataZen.get("data", {})


    regDate = userSummary.get('ts', None)
    playtime = userSummary.get('gametime', None)
    friend_count = userSummary.get('friend_count', None)
    flag = userSummary.get('country', None)

    xp = userSummary.get('xp', None)
    level = (xp / 500) ** 0.6 + xp / 5000 + max(0, xp - 4000000) / 5000 + 1

    gamesplayed = userLeague.get('gamesplayed', None)
    gameswon = userLeague.get('gameswon', None)
    winrate = (gameswon / gamesplayed) * 100

    glicko = userLeague.get('glicko', None)
    rd = userLeague.get('rd', None)
    tetrarating = userLeague.get('tr', None)

    rank = userLeague.get('rank', None)
    bestrank = userLeague.get('bestrank', None)
    standing = userLeague.get('standing', None)

    apm = userLeague.get('apm', None)
    pps = userLeague.get('pps', None)
    vs = userLeague.get('vs', None)

    fortylines = userFortyLines.get('records', None)
    blitz = "TEMPLATE"
    # blitz = userBlitz.get('record', None)
    levelZen = userZen.get('level', None)
    xpZen = userZen.get('score', None)

@bot.message_handler(commands=['start']) # for starting bot + making funny buttons
def start(message):
    bot.send_message(message.from_user.id, startupMessage)

def getCountryFlag():
    global countryFlag
    if flag == "KZ":
        countryFlag = "🇰🇿"
    elif flag == "RU":
        countryFlag = "🇷🇺"
    elif flag == "UA":
        countryFlag = "🇺🇦"
    elif flag == "US":
        countryFlag = "🇺🇸"
    elif flag == "UK":
        countryFlag = "🇬🇧"
    elif flag == "CN":
        countryFlag = "🇨🇳"
    elif flag == "LV":
        countryFlag = "🇱🇻"
    else:
        countryFlag = " "





def printStatsLogs():
    print("TETRA LEAGUE STATS")
    print(f"nickname: {username}")
    print(f"> Rank: {rank} | PB: {bestrank} | TR: {tetrarating}")
    print(f"> Glicko: {glicko} ± {rd}")
    print(f"> APM: {apm} | PPS: {pps} | VS: {vs}")
    print(f"> TL Games: {gamesplayed}/{gameswon} | Win Rate: {round(winrate, 1)}")
    print(f"> Leaderboard: #{standing}")


@bot.message_handler(content_types=['text']) # for text
def get_text_messages(message):
    print(f"ВЫЗВАНА КОМАНДА НА ПОЛУЧЕНИЯ ИНФЫ! ЮЗЕРНЕЙМ TETR.IO {message.text} Айди: {message.from_user.id}, первое имя: {message.from_user.first_name}, фамилия: {message.from_user.last_name}, юзернейм: {message.from_user.username}")
    username = message.text
    getUsersStats(message.text)
    printStatsLogs()
    getCountryFlag()
    # bot.send_message(message.from_user.id, f"+=+ TETRA LEAGUE STATS +=+\nNickname: {username}\nRank: {rank} | PB: {bestrank} | TR: {round(tetrarating, 1)}\nGlicko: {round(glicko, 1)} ± {round(rd, 1)}\nAPM: {apm} | PPS: {pps} | VS: {vs}\nTL Games: {gamesplayed}/{gameswon} | Winrate: {round(winrate, 1)}\nLeaderboard: #{standing}\n \n⚠️⚠️⚠️ CURRENTLY BOT IS ONLY OUTPUTING MY STATS, WILL FIX THIS SOON")
    bot.send_message(message.from_user.id, f"<b><u>=-= USER STATS =-=</u></b>\n{countryFlag} {username} | <b>Join date:</b> {regDate[0:10]}\n> <b>Level: {round(level, 2)} ({round(xp, 2)} XP)</b>\n> <b>Time WASTED:</b> {round(playtime/3600, 1)} hours\n<b><u>=-= MODES STATS =-=</u></b>\n> 40L: {fortylines}\n> Blitz: {blitz}\n> Zen: Level {levelZen} ({xpZen})\n<b><u>=-= TETRA LEAGUE =-=</u></b>\n> <b>Rank: {rank} ({round(tetrarating, 1)} TR) | PB: {bestrank} Glicko: {round(glicko, 0)} ± {round(rd, 0)}</b>\n> <b>To next rank</b> ({nextRank}): {numberwins} wins\n> <b>APM:</b> {apm} | <b>PPS:</b> {pps} | <b>VS:</b> {vs}\n<b>TL Games:</b> {gamesplayed} / {gameswon} | <b>Winrate:</b> {round(winrate, 1)}%\n\n<b><u>=-= LATEST TETRA LEAGUE GAMES =-=</u></b>\n{latestgame_1}\n{latestgame_2}\n{latestgame_3}", parse_mode="HTML")

bot.polling(none_stop=True, interval=0)



