#Counts the number of vowels in the text entered (Y is not considered a vowel)

x = input("Enter some text and get the count for the number of vowels in the text: ")
count = 0

for n in x:
  if n in ["A","a","E","e","I","i","O","o","U","u"]:
    count += 1

print(count)