#! python3
# anime_ranking.py - Webscrapes MyAnimeList.net's Anime ranking using bs4, then redirects User to link to watch online the anime of their choice.

# Imports #
import requests, re, pyperclip
from bs4 import BeautifulSoup


top_how_many = input('\nType the amount of animes you would like to see ranked - according to MyAnimeList.net\n Example: \n "100" would show the top 100 animes\n') 
anime_list = [] # List of anime names to be selected by user

print('\nRank | Score | Anime')

# Fetching data from website 
for count in range(0,int(top_how_many),50): # Loop created to change the URL according to the amount of animes required
    url = 'https://myanimelist.net/topanime.php?limit=' + str(count) 
    website = requests.get(url)
    content = website.content
    soup = BeautifulSoup(content,'lxml')
    anime_https://www1.putlocker.digital/search/Hotaru%20no%20Hakanames = soup.find_all('tr', {'class':'ranking-list'})

    # Printing each anime on page with Rank Position | Score | Anime Name
    for anime in anime_names:
        name_data = anime.find(class_='lazyload') # CSS selector for the anime name
        name = name_data.attrs['alt']
        rank_data = anime.find('td', {'class':'rank ac'}) # CSS selector for the rank position
        rank = rank_data.text.strip()
        score_data = anime.find('td', {'class':'score ac fs14'}) # CSS selector of the Review Score
        score = score_data.text.strip()
        anime_str = rank.center(4)+ ' | '  + score + '  | ' + name[7:]
        if int(rank) < 10: # Alternate formatting TODO Improve formatting for multiple digits
            anime_str = rank.center(4) + ' | ' + score + '  | ' + name[7:]
        print(anime_str)
        anime_list.append(name[7:])

# User input, picking the anime to watch 
chosen_anime = input('\nNow type the number of the anime you would like to watch:\n')
anime_to_watch = anime_list[int(chosen_anime)-1]

# Redirecting based on User's input
watch_link = 'https://www1.putlocker.digital/search/' + '%20'.join(anime_to_watch.split())
print('\nYou chose: ' + anime_to_watch + '\n To watch the anime, paste this URL into your browser. For your convenience it has been saved to your clipboard. \n'+watch_link)
pyperclip.copy(watch_link)