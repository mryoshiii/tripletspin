friend_count = 16

gamesplayed = 108
gameswon = 61
winrate = (gameswon / gamesplayed) * 100

glicko = 1285.62141
rd = 62.3123
tetrarating = 6410.41442

rank = "B"
bestrank = "B"
nextRank = "B+"
standing = "18382"
numberwins = "7.33"

apm = 25.04
pps = 1.37
vs = 50.92

flag = "KZ"


level = 265
xp = 878014

fortylines = "00:58.763"
blitz = 115947
levelZen = 57
xpZen = 2592270

playtime = 56.2

latestgame_1 = "JJSSBU (1-3) — DEFEAT 28.04"
latestgame_2 = "THISISAGUEST (3-1) — VICTORY 28.04"
latestgame_3 = "EQIN (0-3) — DEFEAT 28.04"

regDate = "April 13, 2025"

def printStatsLogs():
    print("TETRA LEAGUE STATS")
    print(f"nickname: {username} | {friend_count}")
    print(f"> Rank: {rank} | PB: {bestrank} | TR: {tetrarating}")
    print(f"> Glicko: {glicko} ± {rd}")
    print(f"> APM: {apm} | PPS: {pps} | VS: {vs}")
    print(f"> TL Games: {gamesplayed}/{gameswon} | Win Rate: {round(winrate, 1)}")
    print(f"> Leaderboard: #{standing}")



def printStatsLogsPretty():
    print("=-= USER STATS =-=")
    print(f"{flag} {username}")
    print(f"> Level: {level} ({xp} XP)")
    print(f"> Join date: {regDate}")
    print(f"> Time WASTED: {playtime} hours")
    print(f"=-= MODES STATS =-=")
    print(f"> 40L: {fortylines}")
    print(f"> Blitz: {blitz}")
    print(f"> Zen: Level {levelZen} ({xpZen})")
    print(f"=-= TETRA LEAGUE =-=")
    print(f"> Rank: {rank} ({tetrarating} TR) | PB: {bestrank} Glicko: {glicko} ± {rd}")
    print(f"> To next rank: {numberwins} wins {nextRank})")
    print(f"> APM: {apm} | PPS: {pps} | VS: {vs}")
    print(f"> {gamesplayed} / {gameswon} | Winrate: {winrate}")
    print("")
    print(f"=-= LATEST TETRA LEAGUE GAMES =-=")
    print(f"{latestgame_1}")
    print(f"{latestgame_2}")
    print(f"{latestgame_3}")


username = input("Put your username there:")
printStatsLogs()
print("prettier logs")
printStatsLogsPretty()
