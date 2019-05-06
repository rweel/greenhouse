"""
temperatuur ophalen van internet, en opslaan in database voor maken grafiek
"""
# voorbeeld gevonden op internet
# https://gathering.tweakers.net/forum/list_messages/1654993

import urllib.request
import json
import datetime
import time
    
# set parameters
date = (datetime.datetime.now().strftime("%d-%m-20%y"))
time = (datetime.datetime.now().strftime("%H:%M"))

# key ophalen bij https://home.openweathermap.org/api_keys
key = "233701779ae96b795e27bee825342a90"

# plaats
place = "Lutjebroek"

# bron is openweathermap.org
url = "http://api.openweathermap.org/data/2.5/weather?q=" + place + "&appid=" + key + "&units=metric"

response = urllib.request.urlopen(url)
data = json.loads(response.read())

# temperatuur variable
temp = data['main']['temp']
humidity = data['main']['humidity']
temp_min = data['main']['temp_min']
temp_max = data['main']['temp_max']

# uitlezen waarden
print ("Op " + date + " om " + time + " uur, was het in " + (place) + " " + str(temp) + " graden.")
print ("De luchtvochtigheid was " + str(humidity) + "%.")
print ("De minimum temperatuur vandaag is " + str(temp_min) + " graden.")
print ("De maximum temperatuur vandaag is " + str(temp_max) + " graden.")