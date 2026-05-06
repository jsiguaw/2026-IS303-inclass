hook = "You are walking through the woods with the queens precious cargo. " \
"You hear a loud thump in teh trail in front of you . " \
"What do you do? A) Run and hide B) Turn Around couragously C) Investigate the noise?"

decision_a = "You hide behind a tree and fall into a reality warping hole. " \
"You land on Tatooine. What do you do? D. Get on the pod racer E. Call for help F. Cry"

decision_b = "You face a giant snaggletoothed rat. It is hungry. What do you do? G. " \
"Fight the rat H. Run and hide I. Befriend the rat."

decision_c = "You find a kind old man who tripped. He offers you a wish. What do you do? J. " \
"Run and hide k. Ask about the conditions of the wish L. Wish for BYU choclate milk"

decision_d = "You are challenged to a race. What do you do? M. Win the race N. Lose the race."

decision_e = "Sand people come to eat you. What do you do? O. Fight. P. Run and hide"

decision_f = "You keep crying. What do you do? Q. Cry harder R. Stop crying"

decision_g = "You die from the rat. You lose."

decision_h = decision_a

decision_i = "The rat is now your bestfriend. You win."

decision_j = decision_a

decision_k = "The old man gets angry. You die."

decision_l = "You recieve a nice cold class of BYU chocolate milk. You win."

decision_m = "You win."

decision_n = "You die."

decision_o = decision_n

decision_p = decision_a

decision_q = decision_n

decision_r = decision_n

decision = input(hook) # Collect the decision from the user
decision = decision.upper() # Convert the decision to uppercase


# Write what happens when you choose...
decision2 = ""
if decision == "A":
    decision2 = input(decision_a)
elif decision == "B":
    decision2 = input(decision_b)
elif decision == "C":
    decision2 = input(decision_c)
else:
    print("You are dead")

if decision == "A" or decision == "B" or decision == "C":
    decision2 = decision2.upper()

    if decision2 == "D":
        decision3 = input(decision_d)
    elif decision2 == "E":
        decision3 = input(decision_e)
    elif decision2 == "F":
        decision3 = input(decision_f)
    elif decision2 == "G":
         decision3 = input(decision_g)
    elif decision2 == "H":
        decision3 = input(decision_h)
    elif decision2 == "I":
        decision3 = input(decision_i)
    elif decision2 == "J":
        decision3 = input(decision_j)
    elif decision2 == "K":
        decision3 = input(decision_k)
    elif decision2 == "L":
        decision3 = input(decision_l)
    elif decision2 == "M":
        decision3 = input(decision_m)
    elif decision2 == "N":
        decision3 = input(decision_n)
    elif decision2 == "O":
        decision3 = input(decision_o)
    elif decision2 == "P":
        decision3 = input(decision_p)
    elif decision2 == "Q":
        decision3 = input(decision_q)
    elif decision2 == "R":
        decision3 = input(decision_r)
    else:    
        print("You are dead")