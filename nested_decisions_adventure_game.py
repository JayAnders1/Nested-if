#question 1 task 1

place = input("Choose a place: forest or cave? ")

if place == "forest":
    action = input("climb a tree or cross a river?")
    if action == "climb a tree":
        print("You found a bird's nest!")
    else:
        action = "cross a river"
        print("You found a boat!")
elif place == "cave":
    print("You find a hidden treasure!")

#question 1 task 2
    action = input("light a torch or proceed in the dark?")
    if action == "light a torch":
        print("You can now see your path to treasure!")
    elif action == "proceed in the dark":
        print("You cannot see, you better turn back...")
 
 #question 1 task 3   
    else:
        pass #not 100% sure if this is all I need to do here
