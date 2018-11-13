import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

nfl = pd.read_csv('NFL Play by Play 2017.csv', low_memory=False)
fix = input('Do you want to see the fixtures? (y/n): ')
fixtures = nfl[['HomeTeam','AwayTeam','Date']].drop_duplicates()

def player_stats():
    player = input('Player: ')
    plays = every_play[(every_play.Receiver == player)|(every_play.Rusher==player)]
    receiving_yards = plays[(plays['Reception']==1)&(plays['PlayType']=='Pass')]['Yards.Gained'].sum()
    targets = len(plays[plays['PlayType']=='Pass'].index)
    receptions = len(plays[(plays.Reception==1)&(plays.PlayType=='Pass')].index)
    rushing_yards = plays[(plays['RushAttempt']==1)&(plays['PlayType']=='Run')]['Yards.Gained'].sum()
    rushing_attempts = len(plays[plays['PlayType']=='Run'].index)
    if targets == 0:
        catch_percent = 0
    else:
        catch_percent =(receptions/targets)*100
    stats = pd.DataFrame(data = {'Targets': [targets],
                                 'Receptions': [receptions],
                                 'Receiving Yards': [receiving_yards],
                                 'Catch %': [catch_percent],
                                 'Rushing Attempts':[rushing_attempts],
                                 'Rushing Yards':[rushing_yards]},index=[player])
    print(stats)

def play_breakdown():
    team = input('{} or {}: '.format(hometeam, awayteam))
    offense = every_play[every_play['OffensiveTeam']==team]
    o = offense.groupby('PlayType').count().Date
    o.columns=['Count']
    o.plot(kind='pie', legend=True)
    print(o)
    plt.tight_layout()
    plt.show()


if fix =='y':
    dat = input('Filter by Date? (y/n): ')
    if dat=='y':
        date = input('Date: ')
        print(fixtures[fixtures['Date']==date])
    else:
        print(fixtures)

hometeam = input('Home Team: ')
awayteam = input('Away Team: ')
every_play = nfl[(nfl['HomeTeam'] == hometeam) & (nfl['AwayTeam'] == awayteam)]
x = input('player stats (p) or team stats (t)?: ')

if x  == 'p':
    player_stats()
elif x == 't':
    play_breakdown()
