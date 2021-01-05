#Checks input against zip code api and outputs the city and state
#Api at https://api.zippopotam.us/us/(5-digits zip code)

zip_lookup = input("Enter a valid 5-digits USA zip code to get the city and state: ")

import requests

link = "https://api.zippopotam.us/us/" + zip_lookup
f = requests.get(link)
f_text = f.text
f_text = f_text.replace('"', "")
f_text = f_text.replace(':', "")
f_text = f_text.replace(',', "")

count = 0

for n in f_text.split():
  if n == "{}":
    print("Zip code", zip_lookup, "not found. Run program again and enter a valid zip code.")
    break
  if count == 1: #print when count is at 1
    print("City for zip code given is", end=" ")
    count += 1 #count is now at 2
  if n == "name":
    count += 1 #count starts at 0 and becomes 1
  if n == "longitude":
    count += 1 #count becomes 3 if city name is only 1 word
  if count == 2:
    print(n, end=" ") #if count is at 2 continue to print city name
  if count == 4: #print when count is at 4
    print("\nState for zip code given is", end=" ")
    count += 1
  if n == "state": #count is now at 4
    count += 1 #count is now at 5
  if n == "state abbreviation":
    count += 1 #count becomes 6 if state name is only 1 word
  if count == 5:
    print(n, end=" "), #if count is at 5 continue to print city name
print("\n")