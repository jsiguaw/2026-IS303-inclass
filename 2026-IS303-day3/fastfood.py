name = "Joel" 
food = input("What is your favorite food? ")

form_complete = False
if food and name:
    form_complete = True

if form_complete:
    print(f"{name}'s favorite food is {food}")
else:  
    print("Form is incomplete")
    