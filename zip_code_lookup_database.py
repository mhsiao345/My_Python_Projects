#Checks input against zip code database and outputs the city and state
#zip_code_database.csv file needed

zip_lookup = input("Enter a valid USA zip code to get the city and state: ")

count = 0
import csv

with open("zip_code_database.csv", 'r') as f:
  for read_file in csv.reader(f):
    if zip_lookup == read_file[0]:
      print("Zip code", zip_lookup, "corresponds to", read_file[3] + ",", read_file[6] + ".")
      count += 1

  if count == 0:
    print("Zip code", zip_lookup, "not found. Run program again and enter a valid zip code.")

f.close()