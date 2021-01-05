#Grade book for current class - add student and scores and get grades and averages

print("\nExisting grade book loaded.\n")
action = input("Enter corresponding number for desired function.\n"
               "1 add student and scores\n"
               "2 add new score for every student\n"
               "3 get average and grade for student\n"
               "4 get averages for the class\n"
               "5 View current grade book\n"
               "--> ")
while action not in ["1", "2", "3", "4", "5"]:
  action = input("Invalid entry. Enter again: ")

"""Section for action 1"""
def name(): #get new student name
  x = input("Enter new student name: ")
  check = input("Is name " + x + " as entered correct? yes or no: ")
  if check != "yes":
    name()
  return x

def add_scores(): #get all existing assignment scores
  score = []
  f = open("grade_book.txt", "r")
  for n in f:
    m = n.split(",")
    for i in range(1, len(m)):
      score.append(input("Enter score for " + m[i] + ": "))
    f.close()
    break
  print("\n")
  return score

def update_grade_book(): #append grade_book.text with new student name and assignment scores
  f = open("grade_book.txt", "a")
  f.write("\n" + str(new_name))
  for item in new_scores:
    f.write("," + str(item))
  f.close()

new_name = ""
new_scores = []

if action == "1":
  new_name = name()
  print("Next add existing scores.")
  new_scores = add_scores()
  update_grade_book()
  print("New student name and scores added. Exiting.")
"""Action 1 section ends"""

"""Section for action 2"""
def new_entry(): #get new assignment name
  x = input("Enter new score entry name: ")
  check = input("Is " + x + " as entered correct? yes or no: ")
  if check != "yes":
    new_entry()
  return x

def save_score(temp): #save scores of new assignment for each student
  for line in fileinput.FileInput("grade_book.txt", inplace=1):
    if temp in line:
      line = line.rstrip()
      line = line.replace(line,line + "," + entry + "\n")
    print(line)
  for line_number, line in enumerate(fileinput.input("grade_book.txt", inplace=1)):
    if len(line) > 1:
      sys.stdout.write(line)

if action == "2":
  import fileinput
  import sys
  #from pathlib import Path
  entry = new_entry()
  entry2 = entry
  save_score("Name")

  with open("grade_book.txt", "r") as myfile:
    f = myfile.read().splitlines()
  count = 1
  for n in f: #get scores of new assignment for each student
    n = n.split(",")
    if count > 1:
      entry = input("Enter " + entry2 + " score for " + n[0] + ": ")
      save_score(n[0])
    count += 1
  print("New score added for all students. Exiting.")
"""Action 2 section ends"""

"""Section for action 3"""
def get_avg_grade():
  x = input("\nEnter student name: ")
  f = open("grade_book.txt", "r")
  count = 1
  total = 0
  result = False
  for n in f:
    if count == 1:
      print("\n" + n)
    m = n
    n = n.split(",")
    if count > 1:
      if n[0] == x: #match student name and does calculation for the row
        print(m)
        for i in range(1, len(n)):
          total += int(n[i])
        print("Sum total of all scores is " + str(total))
        print("Grade average for " + n[0] + " is " + str(total/(len(n)-1)))
        result = True
    count += 1
  if result == False: #reiterate if entered student name not found
    f.close()
    print("Student name not found. Try again.")
    get_avg_grade()
  f.close()

if action == "3":
  get_avg_grade()
"""Action 3 section ends"""

"""Section for action 4"""
def get_avg_all():
  list = []

  f = open("grade_book.txt", "r")
  for n in f: #get all assignment names and saves to list
    m = n.split(",")
    print(m)
    for i in range(1, len(m)):
      list.append(m[i])
    f.close()
    break

  running_total = 0
  for i in range(len(list)): #add and average all assignments
    count = 0
    total = 0
    f = open("grade_book.txt", "r")
    for n in f:
      if count > 0:
        m = n.split(",")
        total += int(m[i+1])
      count += 1
    print("Total class average for " + list[i] + " is " + str(round(total/(count-1), 1)))
    f.close()
    running_total += total/count #sums up all averages
  print("Total class average for everything is " + str(round(running_total/(len(list)-1), 1)))
  return

if action == "4":
  get_avg_all()
"""Action 4 section ends"""

"""Section for action 5"""
if action == "5":
  print("\n")
  f = open("grade_book.txt", "r")
  for n in f:
    a = n.split()
    print(a)
  f.close()
"""Action 5 section ends"""