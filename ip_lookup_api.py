#Checks input against zip code api and outputs the city and state
#Free IP Geolocation API at https://freegeoip.app/csv

temp = input("Hit Enter or Return to get you IP geolcation info,\nor enter a valid IP to get its geolocation info: ")

import requests

link = "https://freegeoip.app/csv/" + temp
f = requests.get(link)
f_text = f.text
for n in f_text.split(","):
  print(n),