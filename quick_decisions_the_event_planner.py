# Question 2 task 1

attendees = int(input("Enter number of attendees: "))
venue = "large hall" if attendees > 100 else "conference room"
print(venue)

#Question 2 task 2

audio_system = "television" if attendees <= 10 else "surround sound speakers"
print(audio_system)

food = input("Would you like vegetarian food? (yes/no) ")
if food == "yes":
    print("Try Veggie Caterers!") 
else:
    print("Try Gourmet Meals Caterers!")