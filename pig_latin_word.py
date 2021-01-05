#Pig latin output for word entered

x = input("Enter a word to convert to Pig Latin: ")
new_word = ""
end = ""
count = 0

while len(x.split()) > 1: # check if input has more than 1 word
  x = input("More than one word entered. Enter a word: ")

for n in x:
  if count == 0:
    end = n + "ay" # take first letter and add ay
  else:
    new_word = new_word + n # form new word starting with 2nd letter
  count += 1

print(new_word + end)