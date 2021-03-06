import time
import requests
from bs4 import BeautifulSoup

# Get steam user id from wiki.teamfortress.com
URL = 'https://wiki.teamfortress.com/wiki/Template:Dictionary/steam_ids/id_list'
r = requests.get(URL)
soup = BeautifulSoup(r.text, 'lxml')
id_string = soup.p.next_sibling.string
steam_user_id_1 = set(id_string.split('\n')[::-1])

# Expand SteamID using Steam API's GetFriendList
API_KEY = '' ##hidden for security reason
URL = 'http://api.steampowered.com/ISteamUser/GetFriendList/v0001/?key='+ API_KEY

steam_user_id_2 = set()
PAUSE = 5
for steam_id in steam_user_id_1:
    params = {
    'steamid': steam_id, \
    'relationship': 'all', \
    'format': 'json'}

    r = requests.get(URL, params)

    if r.json() != {}:
        friends = r.json()['friendslist']['friends']
        time.sleep(PAUSE)
        for friend in friends:
            steam_user_id_2.add(list(friend.values())[0])
            print ('number of steamId: {}'.format(len(steam_user_id_2)))

steam_user_id_combine = list(steam_user_id_1) + list(steam_user_id_2)
with open("steam_user_id.txt", "a") as text_file:
    for c in steam_user_id_combine:
        text_file.write(str(c)+ "\n")
