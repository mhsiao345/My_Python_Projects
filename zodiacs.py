#Outputs chinese zodiac and western astrology signs for a given birth date

print("Find out the Chinese Zodiac and Western Astrology signs for a given birth date! \n")

month = int(input("Enter the two digits birth month: "))
while month not in {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12}:
  month = int(input("Out of range. Re-enter two digits between 01 and 12: "))

day = int(input("Enter the two digits birth day: "))
while day not in range(1, 32):
  day = int(input("Out of range. Re-enter two digits between 01 and 31: "))

year = int(input("Enter the four digits birth year: "))

print("\nThe given birth date is " + str(month) + "/" + str(day) + "/" + str(year))

zodiacs = ["Monkey", "Rooster", "Dog", "Pig", "Rat", "Ox", "Tiger", "Rabbit", "Dragon", "Snake", "Horse", "Sheep"]

z = year % 12 #Chinese zodiac Monkey for years divisible by 12

print("The Chinese Zodiac sign for the given birth year is", zodiacs[z] + ".")

astrology = ["Aries", "Taurus", "Gemini", "Cancer", "Leo", "Virgo", "Libra", "Scorpio", "Sagittarius", "Capricorn", "Aquarius", "Pisces"]

birth_day = month * 100 + day
count = 0
if 321 <= birth_day <= 420: pass
elif 421 <= birth_day <= 520: count = 1
elif 521 <= birth_day <= 620: count = 2
elif 621 <= birth_day <= 721: count = 3
elif 722 <= birth_day <= 821: count = 4
elif 822 <= birth_day <= 921: count = 5
elif 922 <= birth_day <= 1021: count = 6
elif 1022 <= birth_day <= 1121: count = 7
elif 1122 <= birth_day <= 1221: count = 8
elif 1222 <= birth_day <= 1231: count = 9
elif 101 <= birth_day <= 120: count = 9
elif 121 <= birth_day <= 219: count = 10
elif 220 <= birth_day <= 320: count = 11

print("The Western Astrology for the given birth date is", astrology[count] + ".")