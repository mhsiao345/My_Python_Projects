#Manages the inventory of fruits in the database fruit.txt

#***Initial database entry code starts here
f = open("fruit.txt", "w")
item1 = [" 1", "apple", 2, 1.5, "\n"]
item2 = ["2", "banana", 3, 1, "\n"]
item3 = ["3", "orange", 4, 1.5, "\n"]
item4 = ["4", "watermelon", 2, 5, "\n"]
item5 = ["5", "mango", 5, 3, "\n"]
item6 = ["6", "kiwi", 6, 2]
for item in item1:
  f.write("%s " % item)
for item in item2:
  f.write("%s " % item)
for item in item3:
  f.write("%s " % item)
for item in item4:
  f.write("%s " % item)
for item in item5:
  f.write("%s " % item)
for item in item6:
  f.write("%s " % item)
f.close()
#***If fruit.txt database already exists, delete above code

#Print out current database
print("Here is the current inventory details.\n")
print("Item ID:\tName:\tQuantity:\tPrice:\n")
f = open("fruit.txt", "r")
for n in f:
  a = n.split()
  print(a)
f.close()

item_id = input("Enter the Item ID to update the quantity: ")
while item_id not in ["1", "2", "3", "4", "5", "6"]:
  item_id = input("Item not found. Enter Item ID again: ")
item_id = int(item_id)
count = 1
f = open("fruit.txt", "r")
for n in f:
  a = n.split()
  if count == item_id:
    print("\nFruit item:", a[1] + "\n")
  count += 1
f.close()

x = input("Enter 'add' or 'subtract' quantity in inventory: ")
while x not in ["add", "subtract"]:
  x = input("Invalid entry. Enter add or subtract: ")
temp = False
while temp == False:
  y = int(input("Enter quantity: "))
  if type(y) == int and y >= 0:
    break
  print("That's not a positive whole number. Try again: ")
print("\nok", x, "quantity", y)

new_value = 0

if x == "add":
  new = ""
  count = 1
  f = open("fruit.txt", "r+")
  for n in f:
    a = n.split()
    if count == item_id:
      a[2] = int(a[2]) + y
      new = new + str(a) + "\n"
    if count != item_id:
      new = new + str(a) + "\n"
    count += 1
  f.close()

if x == "subtract":
  new = ""
  count = 1
  f = open("fruit.txt", "r+")
  for n in f:
    a = n.split()
    if count == item_id:
      a[2] = int(a[2]) - y
      new = new + str(a) + "\n"
    if count != item_id:
      new = new + str(a) + "\n"
    count += 1
  f.close()

new = new.replace('[', "")
new = new.replace("'", "")
new = new.replace("]", "")
new = new.replace(",", "")

f = open("fruit.txt", "w+")
count = 0
for item in new.split():
  f.write("%s " % item)
  count += 1
  if count % 4 == 0:
    f.write("\n")
f.close()

print("\nHere is the updated inventory details.")
print("Item ID:\tName:\tQuantity:\tPrice:\n")
f = open("fruit.txt", "r")
for n in f:
  a = n.split()
  print(a)
f.close()