#Get current time for US time zone via api
#World Time API http://worldtimeapi.org/api/timezone

time_zone = input("Enter Eastern, Central, Mountain, or Pacific\nand get the current timestamp info: ")
temp = ""

while time_zone not in ["Eastern", "Central", "Mountain", "Pacific"]:
  time_zone = input("Incorrect entry. Enter again: ")

if time_zone == "Eastern":
  temp = "New_York.txt"
elif time_zone == "Central":
    temp = "Chicago.txt"
elif time_zone == "Mountain":
    temp = "Denver.txt"
elif time_zone == "Pacific":
    temp = "Los_Angeles.txt"
    
import requests

link = "http://worldtimeapi.org/api/timezone/America/" + temp
f = requests.get(link)
f_text = f.text
for n in f_text.split(","):
  print(n),