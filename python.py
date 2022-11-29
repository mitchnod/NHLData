from bs4 import BeautifulSoup
import requests
import pandas as pd

info = []
for i in range (1,51):
    url = f"https://www.scrapethissite.com/pages/forms/?page_num={i}"
    page = requests.get(url)

    document = BeautifulSoup(page.content, 'html.parser')
    table = document.find_all('tr', class_ = 'team')

    for row in table:
        team = row.find('td', class_ = "name").text.replace('\n','')
        year = row.find('td', class_ = "year").text.replace('\n','')
        wins = row.find('td',  class_ = 'wins').text.replace('\n','')
        losses = row.find('td',  class_ = 'losses').text.replace('\n','')
        win_percent = row.find('td',  class_ = 'pct').text.replace('\n','')
        goals_scored = row.find('td',  class_ = 'gf').text.replace('\n','')
        
        info.append([team, year, wins, losses, win_percent, goals_scored])

df = pd.DataFrame(info, columns = ['Team', 'Year', 'Wins', 'Losses', 'Win Percentage', 'Goals Scored'])
df.to_csv('NHLData.csv')