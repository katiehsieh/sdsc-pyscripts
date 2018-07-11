# Zeller's Congruence finds the day of the week a date occurs

# Step 1: Get month, date, and year from user
month = int(input("Enter a month (Jan = 1, Feb = 2... Dec = 12) -> "))
date = int(input("Enter a date (1... 31) -> "))
year = int(input("Enter a year #### -> "))

print("Date: " + str(month) + "/" + str(date) + "/" + str(year))

# Step 2
if month <= 2:
    adjustedMonth = month + 10
    adjustedYear = year - 1
else:
    adjustedMonth = month - 2
    adjustedYear = year

# Step 3
monthCorrection = (adjustedMonth * 26 - 2) // 10

# Step 4
century = adjustedYear // 100

# Step 5
centuryRemainder = adjustedYear % 100

# Step 6
yearCorrection = century * 5 + (centuryRemainder + centuryRemainder // 4 + century // 4)

# Step 7
weekDay = (date + monthCorrection + yearCorrection) % 7

# If the result in step 7 is '0', then the day is "Sunday", '1' is "Monday", etc...
days = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
print("Day of Week: " + days[weekDay])
