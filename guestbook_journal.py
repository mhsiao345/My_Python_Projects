#Stores date and guest entry in journal.txt file

from datetime import date
today = date.today()

my_journal = open("journal.txt", "a")

# Add textual month, day and year	
d = today.strftime("%B %d, %Y")
print("Date of entry: ", d)

x = input("Provide your entry below to add into the guestbook. Thanks! \n \n")

my_journal.write("Date of entry: " + d + "\n")
my_journal.write("Guest entry: " + x + "\n \n")

my_journal.close()