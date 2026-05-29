# rl_number = 64
# ent_number = int(input('Enter the number from 1 to 100: '))
# while ent_number != rl_number:
#     print("Please, try again")
#     ent_number = int(input("Enter the number from 1 to 100: "))
# print("Congratulations, you win")

rl_number = 99
while True:
    ent_number = int(input("Enter the number from 1 to 100: "))
    if ent_number > 100 or ent_number < 1:
        print("PLEASE PLEASE, use the correct one, or die.")
        continue
    elif ent_number > rl_number:
        print("t2 much")
        continue
    elif ent_number < rl_number:
        print("t2 little")
    elif ent_number == rl_number:
        print("Congratulations, you win")
        break
    else:
        print("Wrong Number!")