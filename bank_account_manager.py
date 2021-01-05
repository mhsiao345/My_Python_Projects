#Simple bank account manager that manages credits and debits of accounts

#!!!Not completed. Action 2 & 3 not coded!!!

print("Bank account manager ver(1.0).")
action = input("Enter corresponding number for desired function.\n"
               "1 add new account\n"
               "2 credit an account\n"
               "3 debit an account\n"
               "4 view existing account details\n"
               "5 view all accounts and details\n"
               "--> ")
while action not in ["1", "2", "3", "4", "5"]:
  action = input("Invalid entry. Enter again: ")

"""Section for action 1"""
def name():  #get name for new account
  x = input("Enter name for new account: ")
  check = input("Is name " + x + " as entered correct? yes or no: ")
  if check != "yes":
    name()
  return x
def account():  #get name for new account
  x = input("Enter new account type (s) savings (c) checking (b) business: ")
  while x not in ["s", "c", "b"]:
    x = input("Invalid entry. Enter new account type: ")
  if x == "s":
    x = "Savings"
  if x == "c":
    x = "Checking"
  if x == "b":
    x = "Business"
  return x
def credit():  #amount to credit to new account
  x = input("Enter amount to deposit: ")
  if x.isdigit():
    check = input("Is amount " + str(x) + " as entered correct? yes or no: ")
    if check != "yes":
      credit()
  else:
    print("Entry is not valid.Try again.")
    credit()
  return x

if action == "1":
  new_name = name()
  new_account = account()
  new_credit = credit()
  new = [new_name, new_account, new_credit]
  print("\n" + str(new) + " entered into Bank_Account file.")
  f = open("Bank_Accounts.txt", "a") # append Bank_Accounts.txt with new account info
  f.write("\n" + str(new))
  f.close()
""""Action 1 section ends"""

"""Section for action 2, 3, & 4"""
def account_info():
  x = input("\nEnter account name: ")
  f = open("Bank_Accounts.txt", "r")
  result = False
  for n in f:
    n = n.split(",")
    a = n[0].replace("[", "")
    a = a.replace("'", "")
    if a == x: #match account name
      print("Account name: " + n[0] + "\nAccount type: " + n[1] + "\nAccount balance: " +n[2])
      return n
      result = True
  if result == False: #reiterate if entered account name not found
    f.close()
    print("Account name not found. Try again.")
    account_info()
  f.close()

if action == "2":
  print(account_info())

if action == "3":
  amount = account_info()

if action == "4":
  account_info()
"""Action 2, 3, & 4 section ends"""

"""Action 5 section ends"""
if action == "5":
  f = open("Bank_Accounts.txt", "r")
  f = sorted(f.readlines()) #sorts by account name
  new = f
  count1 = 0
  for n in f:
    print(n.rstrip()) #prints out sorted file
    count1 +=1
  f = open("Bank_Accounts.txt", "w+")
  count2 = 1
  for a in new:
    f.write(a.strip()) #writes sorted file back into Bank_Accounts.txt
    if count2 < count1:
      f.write("\n")
    count2 += 1
  f.close()
"""Section for action 5"""