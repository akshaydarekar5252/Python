# wheather activity suggestions 

wheather1 = "Sunny"
wheather = wheather1.lower()

if wheather == "sunny":
    activity = "go for a walk"
elif wheather == "rainy":
    activity = "read a book"
elif wheather == "snowy":
    activity = "build a snowman"
else:
    print("no season matched")
print("Activity is :", activity)