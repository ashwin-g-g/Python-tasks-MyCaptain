initialMonthName = input("Name of the Month : ")
lowercaseMonthName = initialMonthName.lower()
if lowercaseMonthName == "january":
    print("31 days")
elif lowercaseMonthName == "february":
    print("28/29 days")
elif lowercaseMonthName == "march":
    print("31 days")
elif lowercaseMonthName == "april":
    print("30 days")
elif lowercaseMonthName == "may":
    print("31 days")
elif lowercaseMonthName == "june":
    print("30 days")
elif lowercaseMonthName == "july":
    print("31 days")
elif lowercaseMonthName == "august":
    print("31 days")
elif lowercaseMonthName == "september":
    print("30 days")
elif lowercaseMonthName == "october":
    print("31 days")
elif lowercaseMonthName == "november":
    print("30 days")
elif lowercaseMonthName == "december":
    print("31 days")
else: print("Invalid month")