import pygsheets
import pandas as pd
import re
import time
from Player import Player
#authorization
gc = pygsheets.authorize(service_file='creds.json')
sh = gc.open('Copy of NFL Predictions 2K19')
wks = sh.sheet1

players = []
player1 = Player("Bagel",49,30,"B")
players.append(player1)
player2 = Player("Brando",46,33,"C")
players.append(player2)
player3 = Player("Dawson",46,32,"D")
players.append(player3)
player4 = Player("Lucas",50,29,"E")
players.append(player4)
player5 = Player("Damon",46,33,"F")
players.append(player5)
player6 = Player("Payton",47,32,"G")
players.append(player6)
player7 = Player("Josh",43,36,"H")
players.append(player7)
player8 = Players("Foos",46,33,"I")
players.append(player8)

# .*(?=vs) check before vs
# (?<=vs).* check after vs

def checkCells(winners,losers,cols):
    i = 0
    j = 0
    while i < len(cols):
        if j != 0:
            time.sleep(110)
        col = cols[i]
        j = 0
        wins = 0
        loses = 0

        while j < len(winners):
            row = str(j+3)
            cell = col + row
            prediction = wks.get_value(cell)
            if prediction == winners[j]:
                wks.cell(cell).value = ""
                wks.cell(cell).color = 0,1,0,0
                wks.cell(cell).value = winners[j]
                wins += 1
            else:
                wks.cell(cell).value = ""
                wks.cell(cell).color = 1,0,0,0
                wks.cell(cell).value = losers[j]
                loses += 1
            j+=1
        i+=1


def winner(scores,matches,winners,losers):
    i = 0
    awayHome = []
    while i < len(scores):
        if int(scores[i]) > int(scores[i+1]):
            awayHome.append("Away")
        elif int(scores[i]) == int(scores[i+1]):
            awayHome.append("Tie")
        else:
            awayHome.append("Home")
        i+=2
    j = 0
    while j < len(awayHome):
        if awayHome[j] == "Away":
            string = matches[j]
            m = re.search('.*(?=vs)',string)
            m1 = re.search('(?<=vs).*',string)

            winner = m.group(0)
            winner = winner.rstrip()

            loser = m1.group(0)
            loser = loser.lstrip()

            losers.append(loser)
            winners.append(winner)
        elif awayHome[j] == "Home":
            string = matches[j]
            m = re.search('(?<=vs).*',string)
            m1 = re.search('.*(?=vs)',string)

            winner = m.group(0)
            winner = winner.lstrip()

            loser = m1.group(0)
            loser = loser.rstrip()

            losers.append(loser)
            winners.append(winner)
        else:
            team = "Tie"
            winners.append(team)
            losers.append(team)
        j+=1


def template():
    wks.update_cell("A2","Games")
    populateC("A",matches,3)
    populateR(players,2)

def file_len(fname):
    with open(fname) as f:
        for i, l in enumerate(f):
            pass
        return i + 1

def populateR(arr,row):
    for i in xrange(len(arr)):
        column = alpha[i]
        num = str(row)
        cell = column + num
        wks.update_cell(cell,arr[i])

def populateC(column,arr,rowStart):
    for i in xrange(len(arr)):
        num = rowStart + i
        num = str(num)
        cell = column + num
        wks.update_cell(cell,arr[i])

start_time = time.time()

alpha = ["B","C","D","E","F","G","H","I"]
#players = ["Bagel","Brando","Dawson","Lucas","Damon",
#       "Payton","Josh","Foos"]
length = file_len("matchup.txt")

scores = []
winners = []
losers = []
matches = []
matchup = open("format.txt","r")

#put games in array
for games in xrange(length):
    game = matchup.next()
    game = game[:-1]
    matches.append(game)
#put scores in array
with open('scores.txt','r') as f:
    for line in f:
        for score in line.split():
           scores.append(score)

# winner(scores,matches,winners,losers)
# checkCells(winners,losers,alpha)
#wks.cell('C1').color = 1,0,0,0

#template()

matchup.close()
