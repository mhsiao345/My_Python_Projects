#Checks if the text entered is a palindrome

x = input("Enter some text to check if it reads the same forwards as backwards: ")

if x == x[::-1]:
  print("Yes, text entered is a palindrome")
else:
  print("No, text entered is not a palindrome")

print(x + " : text entered")
print(x[::-1] + " : text backwards")