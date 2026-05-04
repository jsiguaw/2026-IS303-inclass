"""

Inputs:
- age
- day of the week
- height
- VIP
- Signed wavier
- parent present

Processes:
- Use the variable to identify which rides are available to the user

Outputs:
- List of rides the user can go on

"""

#INPUTS
age = int(input("Age: "))
day_of_week = input("Day of the week: ").lower()
height = int(input("Height in inches: "))
vip = input("VIP? Yes/No: ").lower()
signed_wavier = input("Signed wavier? Yes/No: ").lower()
parent_present = input("Parent present? Yes/No: ").lower()
ride_found = True

#PROCESSES

# MegaDrop
# if age >= 14 and signed_wavier == "yes" and height >= 54 or (vip == "yes" and height >= 50):
#     print("You can go on the MegaDrop")

if age >= 14 and signed_wavier == "yes":
    if height >= 54:
        print("You can go on the MegaDrop")
        ride_found = True
    elif vip == "yes" and height >= 50:
        print("You can go on the MegaDrop")
        ride_found = True
else:
    print("You cannot go on the MegaDrop")
    ride_found = False

# Thunder Bolt
if age >= 10 and height >= 48 and day_of_week != "monday":
    print("You can go on the Thunder Bolt")
    ride_found = True
else:
    print("You cannot go on the Thunder Bolt")
    ride_found = False
# Kiddie Coaster
if age > 8 and parent_present == "Yes":
    print("You can go on the Kiddie Coaster")
    ride_found = True
else:
    print("You cannot go on the Kiddie Coaster")
    ride_found = False
#OUTPUTS
if not ride_found:
    print("Sorry, there are no rides available for you.")